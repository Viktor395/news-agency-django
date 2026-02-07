# 📰 News Agency Project

A web-based news platform built with Django, featuring article management, user authentication, and a clean interface.

## 🚀 Live Demo
You can check out the deployed project here: 
[https://news-agency-django.onrender.com](https://news-agency-django.onrender.com)

A professional news agency web application built with **Django 6.0**. This project features a full content management cycle, from user authentication to automated article publishing with SEO-friendly URLs.

## ✨ Key Features

* **User Authentication**: Secure sign-up, login, and logout functionality.
* **Article Management**: User-friendly forms for creating news with image upload support.
* **Automatic Slugs**: Integrated `pytils` for automatic transliteration of Cyrillic titles into SEO-optimized URL slugs.
* **Security First**: Sensitive data (SECRET_KEY) is managed via environment variables (`.env`).
* **Responsive UI**: Fully responsive interface built with Bootstrap 5.
* **Clean Architecture**: Optimized media storage and organized project structure.

## 🛠️ Tech Stack

* **Backend**: Python 3.13, Django 6.0.1
* **Database**: SQLite (Development)
* **Frontend**: HTML5, CSS3, Bootstrap 5
* **Libraries**: `python-dotenv`, `pytils`, `Pillow`

## 🚀 Installation & Local Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Viktor395/news-agency-django.git
    cd news-agency-django
    ```

2.  **Set up virtual environment:**
    ```bash
    python -m venv .venv
    # Windows:
    .venv\Scripts\activate
    # Linux/macOS:
    source .venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install django python-dotenv pytils pillow
    ```

4.  **Environment Variables:**
    Create a `.env` file in the root directory and add:
    ```env
    SECRET_KEY=your_secret_key_here
    DEBUG=True
    ```

5.  **Run Migrations & Start Server:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
    ```

6.  **Access the App:**
    Go to `http://127.0.0.1:8000/`

## 📂 Project Structure
* `news/` - Main application logic.
* `templates/` - HTML templates with Bootstrap 5.
* `media/articles_images/` - Centralized storage for article thumbnails.

---
*Created as a portfolio project to demonstrate Django web development skills.*