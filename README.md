# 🚀 Aashish Sharma — Portfolio Website

A modern, single-page portfolio website built with **Flask** and a fully integrated **Admin Panel** for real-time content management.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.x-lightgrey?logo=flask)
![SQLite](https://img.shields.io/badge/Database-SQLite-green?logo=sqlite)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## ✨ Features

| Feature | Description |
|---|---|
| 🏠 **Hero Section** | Dynamic name, headline, and social media links |
| 👤 **About Me** | Editable bio section with line-break support |
| 🎓 **Academic Details** | Education history displayed in card layout |
| 💼 **Experience** | Work history with role, company & description |
| 🛠️ **Technical Skills** | Skill tags with admin-managed categories |
| 📂 **Key Projects** | Project showcase with tech stack details |
| 📬 **Contact Section** | Contact form with email and phone info |
| 🔐 **Admin Panel** | Full CMS — Add, Edit, Delete all sections |
| 🔑 **Password Management** | Change admin password anytime |

---

## 🖥️ Tech Stack

- **Backend:** Python, Flask, SQLAlchemy
- **Database:** SQLite
- **Frontend:** HTML5, CSS3, JavaScript
- **Authentication:** Flask-Login
- **Fonts:** Google Fonts (Outfit, Playfair Display)
- **Icons:** Font Awesome 6

---

## 📁 Project Structure

```
Portfolio-Website/
├── app.py                  # Main Flask application & routes
├── models.py               # Database models & initial seeding
├── requirements.txt        # Python dependencies
├── .gitignore              # Git ignore rules
├── static/
│   └── css/
│       └── style.css       # All styling
├── templates/
│   ├── base.html           # Base template with navbar & footer
│   ├── index.html          # Main portfolio page
│   ├── admin.html          # Admin dashboard
│   └── login.html          # Admin login page
└── instance/
    └── portfolio.db        # SQLite database (auto-generated)
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed on your system

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Officialaashish1/Portfolio-Website.git
   cd Portfolio-Website
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Open in browser**
   ```
   http://127.0.0.1:5000
   ```

---

## 🔐 Admin Panel

Access the admin dashboard to manage all website content in real-time.

- **URL:** `http://127.0.0.1:5000/admin`
- **Default Username:** `Aashish`
- **Default Password:** `78@Aashish`

### Admin Capabilities:
- ✏️ Edit **About Me** (name, headline, bio, contact info)
- 🎓 Add / Edit / Delete **Education** entries
- 💼 Add / Edit / Delete **Work Experience**
- 🛠️ Add / Edit / Delete **Skills** with categories
- 📂 Add / Edit / Delete **Projects** with tech stack
- 🔑 **Change Password** anytime

> **Tip:** Use line breaks (press Enter) in text fields — they will render correctly on the website!

---

## 📸 Screenshots

| Portfolio Homepage | Admin Dashboard |
|---|---|
| Clean, modern single-page design | Full content management system |

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/Officialaashish1/Portfolio-Website/issues).

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👤 Author

**Aashish Sharma**
- GitHub: [@Officialaashish1](https://github.com/Officialaashish1)
- LinkedIn: [Aashish Sharma](https://linkedin.com/in/aashish-sharma-2aa057226)
- Email: aashish783078@gmail.com

---

⭐ **Star this repo if you found it useful!**
