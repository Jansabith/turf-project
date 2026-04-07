# 🏟️ Smart Turf Booking System

A web-based application built using **Django** that allows users to book turf slots, join games, and manage player participation efficiently.

---

## 🚀 Features

- 🔐 User Authentication (Login/Register)
- 📅 Turf Slot Booking System
- ⚽ Join / Exit Turf Matches
- 👥 View Players Joined in a Slot
- 📩 (Planned) WhatsApp Notifications for Players
- 🖼️ Image Upload for Turf (Media Handling)
- 🛠️ Admin Panel for Turf Management

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, Django Templates
- **Database:** SQLite (default) / PostgreSQL (production)
- **Deployment:** PythonAnywhere (or any cloud platform)

---

## 📁 Project Structure

```bash
Turf-project/
│
├── accounts/          # User authentication (login/register)
├── booking/           # Turf booking logic
├── matches/           # Match / player join system
├── media/             # Uploaded images (turf images)
│
├── project/           # Main Django project
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
│
├── static/            # CSS, JS, Images
├── templates/         # HTML templates
│
├── Turf/              # (Your main app / additional module if used)
│
├── venv/              # Virtual environment (not pushed to Git)
├── .env               # Environment variables
├── .gitignore
├── db.sqlite3         # Database
├── manage.py
├── requirements.txt
└── README.md
```

## 🧠 Key Functionalities

- Users can **join a turf slot**
- Joined users can **exit from the turf**
- Players can **view other players in the same slot**
- Admin can **manage turf and bookings**