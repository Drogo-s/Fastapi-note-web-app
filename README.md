# 📝 FastAPI Note Web App

A simple and clean notepad web application built with **Python**, **FastAPI**, and **Supabase**. Users can register, log in, and manage personal notes — all securely tied to their own accounts.

---

## 🚀 Features

- 🔐 User Registration & Login
- 🗒️ Create, Read personal notes
- 👤 Notes are tied to each user's account
- ⚡ Fast and lightweight REST API powered by FastAPI
- ☁️ Cloud database and authentication via Supabase

---

## 🛠️ Tech Stack

| Layer        | Technology        |
|--------------|-------------------|
| Language     | Python 3          |
| Framework    | FastAPI           |
| Database     | Supabase (PostgreSQL) |
| Auth         | Supabase Auth     |

---

## ⚙️ Getting Started

### Prerequisites

- Python 3.8+
- A [Supabase](https://supabase.com) account and project

### 1. Clone the Repository

```bash
git clone https://github.com/Drogo-s/Fastapi-note-web-app.git
cd Fastapi-note-web-app
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

Create a `.env` file in the root directory and add your Supabase credentials:

```env
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_anon_key
```

> You can find these in your Supabase project under **Settings → API**.

### 4. Run the App

```bash
uvicorn main:app --reload
```

The app will be running at `http://127.0.0.1:8000`

---

## 📡 API Endpoints

### Auth

| Method | Endpoint            | Description        |
|--------|---------------------|--------------------|
| POST   | `/auth/register`    | Register a new user |
| POST   | `/auth/login`       | Log in a user       |

### Notes

| Method | Endpoint      | Description              |
|--------|---------------|--------------------------|
| GET    | `/notes`      | Get all notes for the logged-in user |
| POST   | `/notes`      | Create a new note        |

---

## 📁 Project Structure

```
fastapi_blog/
├── main.py            # App entry point
├── requirements.txt   # Project dependencies
├── .env               # Environment variables (not committed)
└── ...
```

---

## 🔒 Security Note

Never commit your `.env` file. Make sure it's listed in your `.gitignore`:

```
.env
```

---

## 🤝 Contributing

Pull requests are welcome! Feel free to fork the repo and submit improvements.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

> Built with ❤️ using FastAPI & Supabase
