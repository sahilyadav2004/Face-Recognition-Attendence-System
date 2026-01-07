# Face Recognition Attendance System 🎓📸

A **desktop-based Face Recognition Attendance System** built using **Python, Tkinter, OpenCV, and SQLite**. This application helps manage student records, capture face samples, train a recognition model, and mark attendance automatically using face recognition.

---

## 🚀 Features

- 🧑‍🎓 **Student Management System**  
  Add, update, delete, search, and view student records.

- 📷 **Face Dataset Generation**  
  Capture student face images using a webcam.

- 🧠 **Face Recognition Training**  
  Train the system using LBPH (Local Binary Pattern Histogram).

- 🕵️ **Face Detection & Recognition**  
  Recognize faces in real time using OpenCV.

- 🗂 **Attendance Management**  
  Automatically mark attendance using recognized faces.

- 🪟 **Single-Window Control**  
  Ensures only **one window per module** opens at a time (professional window handling).

- 💾 **SQLite Database**  
  Lightweight, file-based database for storing student data.

---

## 🛠 Technologies Used

| Technology | Purpose |
|---------|--------|
| Python | Core programming language |
| Tkinter | GUI development |
| OpenCV | Face detection & recognition |
| SQLite | Database management |
| Pillow (PIL) | Image handling |
| Haar Cascade | Face detection |

---

## 📁 Project Structure

```
face_recognition_project/
│
├── main.py                 # Main dashboard
├── student.py              # Student management module
├── train.py                # Training module
├── face_recognition.py     # Face recognition module
├── attendance.py           # Attendance module
├── developer.py            # Developer info
├── help.py                 # Help window
│
├── database/
│   └── student.db          # SQLite database
│
├── data/                   # Captured face images
│
├── images/                 # Background & UI images
│
├── haarcascade_frontalface_default.xml
│
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/face-recognition-attendance.git
cd face-recognition-attendance
```

### 2️⃣ Install Required Libraries
```bash
pip install opencv-python pillow numpy
```

> Tkinter comes pre-installed with Python.

---

## ▶️ How to Run

```bash
python main.py
```

Make sure:
- Webcam is connected
- `haarcascade_frontalface_default.xml` exists in project folder

---

## 🧑‍🎓 Student Module Workflow

1. Add student details
2. Click **Take Photo Sample** (captures 100 images)
3. Train the model
4. Detect face & mark attendance

---

## 📦 requirements.txt

This project uses a few external Python libraries. All required dependencies are listed in `requirements.txt` so the project can be set up easily on any system.

### 📄 requirements.txt
```txt
dnspython==2.8.0
numpy==2.2.6
opencv-contrib-python==4.12.0.88
opencv-python==4.12.0.88
pillow==12.0.0
pymongo==4.15.5
```txt

> **Note:** Libraries such as `tkinter`, `sqlite3`, and `os` are built into Python and do not need to be installed separately.

---

## 🐍 Virtual Environment Setup (Recommended)

Using a virtual environment keeps project dependencies isolated and avoids version conflicts.

### 1️⃣ Create Virtual Environment
```bash
python -m venv venv
```

### 2️⃣ Activate Virtual Environment

**Windows (CMD / PowerShell):**
```bash
venv\Scripts\activate
```

**Linux / macOS:**
```bash
source venv/bin/activate
```

You should see `(venv)` in your terminal after activation.

---

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🧠 Face Recognition Logic

- **Face Detection:** Haar Cascade Classifier
- **Face Recognition:** LBPH Algorithm
- **Image Storage:** `data/user.<id>.<img_no>.jpg`

---

## 🔒 Window Management Logic

- Only **one instance** of each module window opens
- Clicking again brings the window to front
- Prevents duplicate resource usage

---

## 📌 Future Enhancements

- Login & authentication system
- Export attendance to Excel/CSV
- Cloud database support
- Face mask detection
- Deploy as `.exe` using PyInstaller

---

## 👨‍💻 Developer

**Sahil Yadav**  
B.Tech Student | MERN Stack & Python Developer  

---

## 📜 License

This project is for **educational purposes**. You are free to use and modify it.

---

## ⭐ Support

If you like this project, give it a ⭐ and feel free to contribute!

Happy Coding 😊

