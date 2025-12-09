# Arcanum - User Authentication System

A clean Flask-based authentication system built as a college project with modern UI features.

## 🚀 Quick Installation

### Requirements
- Python 3.7+
- Flask

### Setup Steps
1. **Download the project files**

2. **Install Flask:**
   ```bash
   pip install flask
   ```
3. **Run the application:**
   ```bash
   python main.py
   ```
4. **Open in browser:** `http://localhost:5000`

## 📁 Project Structure
```
arcanum-app/
├── main.py             # Main application
├── static/assets/      # Frontend assets
│   ├── boxicons/       # Icons
│   ├── style.css       # Modern styles
│   └── script.js       # Interactive features
├── templates/          # HTML pages
│   ├── index.html      # Index Page
│   ├── login.html      # Login Page
│   └── signup.html     # Signup Page
└── README.md
```
## 📸 Application Screenshots
1. Login Page
<img src="https://github.com/yahiaelbanna/Arcanum--college-task/blob/main/md/login.png" alt="login page">
Modern login interface with password toggle and validation

2. Signup Page
<img src="https://github.com/yahiaelbanna/Arcanum--college-task/blob/main/md/signup.png" alt="signup page">
Sleek registration form with real-time validation

3. Index Page
<img src="https://github.com/yahiaelbanna/Arcanum--college-task/blob/main/md/index.png" alt="index page">
Personalized welcome page with user information

## ✨ Key Features
- ✅ User registration & login
- ✅ Password hashing (SHA-256)
- ✅ Email validation
- ✅ Modern UI
- ✅ Password visibility toggle 👁️
- ✅ Session management

## 🎨 UI Features
- **Clean, modern design**
- **Password toggle** (show/hide)
- **Form validation**
- **Boxicons integration**

## 🔐 Security
- Passwords stored as SHA-256 hashes
- Email uniqueness validation
- Session-based authentication
- Input sanitization

## 🛠️ Usage
1. **First time?** Go to `/signup` to create account
2. **Existing user?** Login at `/login`
3. **Dashboard:** View personalized welcome page

## 📊 Database
Auto-creates `users` table:
```sql
id, name, email, password (hashed)
```

## 🎓 Project Info
**College project** demonstrating:
- Flask web development
- User authentication
- Database integration
- Frontend-backend connection

## 📄 License



This project is created for educational purposes as part of a college assignment. Feel free to use it as a learning resource.

---
>*Simple, functional, and ready to use!*

Last Updated: 5/13/2025 

Project Status: Complete & Functional

Note: This is a demonstration project for educational purposes. Not for production deployment.
