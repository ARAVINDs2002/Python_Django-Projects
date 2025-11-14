# Django Blog Application

A fully functional **Django Blog Application** where users can:

- Sign up, log in, and log out  
- Create blog posts  
- Edit their own posts  
- Delete their posts  
- View posts from all users  
- Admin can manage all posts and users  

This project demonstrates essential Django features required for real-world applications and interviews.

---

## 🚀 Features

### 👤 User Features
- User registration & authentication  
- Create, read, update, delete posts  
- Secure permissions (users can edit/delete only their posts)

### 🔐 Admin Features
- View all users  
- View all posts  
- Delete any post  
- Manage user permissions  

---

## 🏗 Tech Stack

| Component | Technology |
|----------|------------|
| Backend  | Django 5.x |
| Frontend | HTML, CSS (customizable) |
| Database | SQLite (development) |
| Auth     | Django Authentication System |
| Deployment Ready | Yes |

---

## 📁 Project Structure

```
Blog-App/
│── manage.py
│── blog/               # Django app
│── Blog-App/           # Project settings
│── templates/          # HTML templates (inside app)
│── static/             # Optional static files
│── .gitignore
│── requirements.txt
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/Blog-App.git
cd Blog-App
```

### 2. Create a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate    # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run migrations
```bash
python manage.py migrate
```

### 5. Create superuser (admin)
```bash
python manage.py createsuperuser
```

### 6. Start the server
```bash
python manage.py runserver
```

---

## 🔑 Default Admin Panel
```
http://127.0.0.1:8000/admin/
```

---

## 🖼 Screenshots

(You can add screenshots here later.)

---

## 📚 Learning Outcome

From this project you will learn:

- Django Models & ORM  
- Dynamic routing  
- Templates & context  
- User authentication  
- CRUD operations  
- Permissions  
- Admin customization  
- Project structuring  
- Best GitHub practices  

---

## 📬 Contact

Feel free to reach out for improvements or suggestions.

**Author:** Aravind  
**GitHub:** https://github.com/yourusername

---
