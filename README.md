Project Overview

This project is a Django-based web application connected to a MySQL (phpMyAdmin) database.
It demonstrates how to build a dynamic blog-style platform with authentication, user management, and Django Admin Panel integration.

The goal of this project is to:

Use Django ORM for database operations.

Manage content and users via Django Admin Panel.

Store and retrieve data from a MySQL database.

Provide APIs (via Django REST Framework) for frontend integration.

⚙️ Features

🔑 User Authentication (Register, Login, Logout).

👤 Custom User Model integration with Django’s default auth.

📝 Blog / Post Management using models & slug-based navigation.

💬 Comment & Nested Reply System (infinite reply nesting supported).

🔖 Bookmark Feature to save posts.

📧 Forgot Password & Token-based Reset system.

📊 Django Admin Panel for easy database and user management.

🗄️ MySQL Database backend (managed through phpMyAdmin).

🛠️ Tech Stack

Backend: Django 4.2.2, Django REST Framework

Database: MySQL 8.0 (via mysqlclient)

Frontend: Django Templates (dynamic rendering with slug navigation)

Authentication: Django’s built-in auth + JWT (optional for APIs)

Deployment: XAMPP (for local MySQL + phpMyAdmin)
