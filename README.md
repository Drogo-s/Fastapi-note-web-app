# 📝 FastAPI Note Web App
A simple and clean notepad web application built with **Python**, **FastAPI**, and **Supabase**. Users can register, log in, and manage personal notes — all securely tied to their own accounts.

---

## 🚀 Features
- 🔐 User Registration & Login
- 🗒️ Create, Read personal notes
- 👤 Notes are tied to each user's account
- ⚡ Fast and lightweight REST API powered by FastAPI
- ☁️ Cloud database and authentication via Supabase
- 🎙️ Offline Speech-to-Text powered by OpenAI Whisper — transcribe your voice into notes without an internet connection

---

## 🛠️ Tech Stack
| Layer          | Technology                  |
|----------------|-----------------------------|
| Language       | Python 3                    |
| Framework      | FastAPI                     |
| Database       | Supabase (PostgreSQL)       |
| Auth           | Supabase Auth               |
| Speech-to-Text | OpenAI Whisper (Offline)    |

---

## 🎙️ Offline Speech-to-Text (Whisper)

This app includes a fully **offline** voice-to-text feature powered by [OpenAI Whisper](https://github.com/openai/whisper).

### How it works
1. Click the 🎤 **Start Speaking** button on the Notes page
2. Speak your note clearly into your microphone
3. Click 🔴 **Stop Speaking** when done
4. Whisper transcribes your audio **locally on your machine** — no internet required
5. The transcribed text automatically fills into the note content field
6. Click **Add Note** to save it

### Why Whisper?
- ✅ Works completely **offline** after first install
- ✅ Supports **99+ languages**
- ✅ Handles accents, fast speech, and noisy environments
- ✅ Free and open source by OpenAI
- ✅ No data is sent to any external server — your voice stays on your machine

### Whisper Model Sizes
You can change the model size in `main.py` depending on your needs:

| Model   | Speed   | Accuracy | Recommended For        |
|---------|---------|----------|------------------------|
| `tiny`  | Fastest | Lowest   | Testing                |
| `base`  | Fast    | Good     | Light use              |
| `small` | Medium  | Better   | Daily use ✅           |
| `medium`| Slow    | Great    | Accuracy focused       |
| `large` | Slowest | Best     | Requires good hardware |

To change the model, edit this line in `main.py`:
```python
model = whisper.load_model("small")  # change to tiny, base, medium or large
```

> **Note:** On first run, Whisper will download the model weights automatically. After that, it works fully offline.

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

### 3. Install Whisper (Speech-to-Text)
Whisper runs fully offline on your machine. Install it with:
```bash
pip install openai-whisper
```

You'll also need **ffmpeg** installed on your system:
```bash
# Ubuntu / Debian
sudo apt install ffmpeg

# macOS
brew install ffmpeg

# Windows
# Download from https://ffmpeg.org/download.html and add to PATH
```

> On first use, Whisper will automatically download the required model weights. No internet connection is needed after that.

### 4. Set Up Environment Variables
Create a `.env` file in the root directory and add your Supabase credentials:
```env
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_anon_key
```

> You can find these in your Supabase project under **Settings → API**.

### 5. Run the App
```bash
uvicorn main:app --reload
```

The app will be running at `http://127.0.0.1:8000`

---

## 📡 API Endpoints

### Auth
| Method | Endpoint         | Description          |
|--------|------------------|----------------------|
| POST   | `/auth/register` | Register a new user  |
| POST   | `/auth/login`    | Log in a user        |

### Notes
| Method | Endpoint      | Description                                               |
|--------|---------------|-----------------------------------------------------------|
| GET    | `/notes`      | Get all notes for the logged-in user                      |
| POST   | `/notes`      | Create a new note                                         |
| POST   | `/transcribe` | Upload audio and convert speech to text using Whisper     |

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

> Built with ❤️ using FastAPI, Supabase & OpenAI Whisper
