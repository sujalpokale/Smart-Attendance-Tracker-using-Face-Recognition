# 🎓 Smart-Attendance-Tracker-using-Face-Recognition

A **real-time face recognition attendance tracking system** that automatically detects, recognizes, and marks attendance using webcam-based facial recognition.  
Built with **Python**, **Flask**, **OpenCV**, and **SQLite**, this system provides a modern web interface for registration, live attendance tracking, and viewing attendance records.

---

## 🚀 Features

✅ **Face Registration** – Register new users with name and roll number via webcam.  
✅ **Real-Time Recognition** – Detects and recognizes registered faces instantly.  
✅ **Auto Attendance Logging** – Marks attendance with date and timestamp automatically.  
✅ **Web Interface** – Manage everything through a clean Flask web dashboard.  
✅ **Database Integration** – Stores all data securely in a local SQLite database.  
✅ **Modular Code** – Clean structure for scalability and easy updates.

---

## 🧠 Tech Stack

| Component | Technology |
|------------|-------------|
| **Frontend** | HTML5, CSS3, JavaScript |
| **Backend** | Flask (Python) |
| **Face Recognition** | OpenCV, face_recognition |
| **Database** | SQLite |
| **Language** | Python 3.10+ |

---

## 📁 Project Structure

```
Smart-Attendance-Tracker-using-Face-Recognition/
│
├── app.py                  # Main Flask web app
├── database.py              # Database setup and utility functions
├── register.py              # Face registration logic
├── attendance.py            # Attendance marking via face recognition
│
├── templates/               # HTML templates
│   ├── index.html
│   ├── register.html
│   ├── attendance.html
│   └── records.html
│
├── static/
│   ├── css/
│   │   ├── index.css
│   │   ├── register.css
│   │   ├── attendance.css
│   │   └── records.css
│   └── images/              # (optional) logo, screenshots, etc.
│
└── attendance.db            # SQLite database (auto-created)
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/Smart-Attendance-Tracker-using-Face-Recognition.git
cd Smart-Attendance-Tracker-using-Face-Recognition
```

### 2️⃣ Install Dependencies
Make sure you have **Python 3.10+** installed.  
Then run:
```bash
pip install -r requirements.txt
```

If the file doesn’t exist yet, create one with:
```
Flask
opencv-python
face_recognition
numpy
pandas
```

### 3️⃣ Run the App
```bash
python app.py
```

Then open your browser and go to:  
👉 **http://127.0.0.1:5000**

---

## 🧍‍♂️ How It Works

1. **Register a New User**
   - Navigate to `/register`
   - Enter name and roll number
   - Capture the face via webcam

2. **Mark Attendance**
   - Go to `/attendance`
   - Webcam opens for real-time face recognition
   - Attendance is marked automatically when a face is recognized

3. **View Attendance Records**
   - Go to `/records`
   - Displays date, time, and user information in a clean table view

---

## 🖼️ Video link 
   ** https://drive.google.com/file/d/1m4eZHihT5WdgA4bg-GQgOyvcJDyhyopk/view?usp=drive_link **

> Add screenshots to the `static/images/` folder to make your README look more professional.

---

## 🔒 Security & Privacy

- All data and face encodings are stored **locally** — no cloud upload.  
- For production use, add **admin login**, **HTTPS**, and **secure database encryption**.  
- Protect the database file (`attendance.db`) if storing sensitive data.

---

## 🧩 Future Enhancements

- 🔐 Admin login and dashboard  
- ☁️ Cloud database integration (Firebase / PostgreSQL)  
- 📤 Export attendance to Excel or CSV  
- 📸 Web-based webcam streaming (via WebRTC)  
- 🌍 Online deployment (Render / Railway / Heroku)
