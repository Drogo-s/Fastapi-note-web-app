import os
from fastapi import FastAPI, Request, Form, Depends, Response
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from supabase import create_client, Client
from dotenv import load_dotenv
from itsdangerous import URLSafeSerializer
from supabase_auth.errors import AuthApiError

load_dotenv()
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)
SECRET_KEY = os.getenv("SECRET_KEY", "default-secret")
serializer = URLSafeSerializer(SECRET_KEY)

def get_current_user(request: Request):
    cookie = request.cookies.get("session")
    if not cookie:
        return None
    try:
        data = serializer.loads(cookie)
        return data.get("user_id")
    except Exception:
        return None

@app.get("/")
def home(request: Request, user_id: str = Depends(get_current_user)):
    return templates.TemplateResponse(
        "index.html", {"request": request, "user_id": user_id}
    )

@app.get("/register")
def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.post("/register")
def register(request: Request, email: str = Form(...), password: str = Form(...)):
    try:
        auth_res = supabase.auth.sign_up({"email": email, "password": password})
        if auth_res.user:
            return RedirectResponse("/login", status_code=302)
    except AuthApiError as e:
        error = str(e)
        if "already registered" in error:
            error = "This email is already registered. Please log in."
        return templates.TemplateResponse(
            "register.html", {"request": request, "error": error}
        )
    return templates.TemplateResponse(
        "register.html", {"request": request, "error": "Registration failed"}
    )

@app.get("/login")
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
def login(request: Request, email: str = Form(...), password: str = Form(...)):
    try:
        auth_res = supabase.auth.sign_in_with_password(
            {"email": email, "password": password}
        )
        if auth_res.session:
            user_id = auth_res.user.id
            cookie_data = serializer.dumps({"user_id": user_id})
            response = RedirectResponse("/notes", status_code=302)
            response.set_cookie(key="session", value=cookie_data, httponly=True)
            return response
    except AuthApiError as e:
        error = str(e)
        if "Email not confirmed" in error:
            error = "Please confirm your email first, or ask admin to disable email confirmation."
        elif "Invalid login credentials" in error:
            error = "Wrong email or password."
        return templates.TemplateResponse(
            "login.html", {"request": request, "error": error}
        )
    return templates.TemplateResponse(
        "login.html", {"request": request, "error": "Login failed"}
    )

@app.get("/logout")
def logout():
    response = RedirectResponse("/", status_code=302)
    response.delete_cookie("session")
    return response

@app.get("/notes")
def get_notes(request: Request, user_id: str = Depends(get_current_user)):
    if not user_id:
        return RedirectResponse("/login", status_code=302)
    res = supabase.table("notes").select("*").eq("user_id", user_id).execute()
    return templates.TemplateResponse(
        "notes.html", {"request": request, "notes": res.data, "user_id": user_id}
    )

@app.post("/notes")
def add_note(
    request: Request,
    title: str = Form(...),
    content: str = Form(...),
    user_id: str = Depends(get_current_user),
):
    if not user_id:
        return RedirectResponse("/login", status_code=302)
    supabase.table("notes").insert(
        {"title": title, "content": content, "user_id": user_id}
    ).execute()
    return RedirectResponse("/notes", status_code=302)

@app.post("/notes/delete")
def delete_note(note_id: str = Form(...), user_id: str = Depends(get_current_user)):
    if not user_id:
        return RedirectResponse("/login", status_code=302)
    supabase.table("notes").delete().eq("id", note_id).eq("user_id", user_id).execute()
    return RedirectResponse("/notes", status_code=302)