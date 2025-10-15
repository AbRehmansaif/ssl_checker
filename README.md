# 💻 ssl_checker

![Current Version](https://img.shields.io/badge/version-v0.1-blue)
![GitHub contributors](https://img.shields.io/github/contributors/AbRehmansaif/README-Template)
![GitHub stars](https://img.shields.io/github/stars/AbRehmansaif/README-Template?style=social)
![GitHub forks](https://img.shields.io/github/forks/AbRehmansaif/README-Template?style=social)

## 🛠️ Features
🌐 Multiple Website Input – Enter one or multiple URLs (line or space separated).

⚙️ HTTP Status Check – Fetches each site and returns its status code (200, 404, 503, etc.).

🔒 SSL Certificate Expiry Check – Verifies SSL/TLS certificate and calculates days remaining before expiry.

⏰ Expiry Warnings – Highlights websites whose certificates will expire within 30 days.

💾 Database Storage – Saves every check (URL, status, expiry days, timestamp) in SQLite for history and analysis.

🧰 Admin Panel – View, search, and filter results easily using Django’s admin interface.

🎨 Bootstrap UI – Clean and responsive interface for entering URLs and viewing results.

### </> Built With
* ![Python](https://img.shields.io/badge/python-3.13.5%2B-blue?logo=python&logoColor=white)
- Backend Framework
- Django Templates for Frontend


---
## 🚀 Getting Started with the Project
## Clone the Repository:

Linux and macOS:

```bash
sudo git clone https://github.com/AbRehmansaif/ssl_checker.git
```

Windows:

```bash
git clone https://github.com/AbRehmansaif/ssl_checker.git
```

To get this project up and running you should start by having Python installed on your computer. It's advised you create a virtual environment to store your projects dependencies separately. You can install virtualenv with

## Set up a Python Virtual Environment:
Windows:
```
python -m venv env
```
Linux and macOS:
```
python3 -m venv env
```

## Activate the Virtual Environment:
That will create a new folder `env` in your project directory. Next activate it with this command on Win/linux:

Window (Command Prompt or PowerShell):
```
env\Scripts\activate
```
Linux and macOS:
```
source env/bin/active
```
## Deactivate the Virtual Environment:`env`
```
deactivate
```
## Install Project Dependencies:

```
pip install -r requirements.txt
```
## Create and Apply Database Migrations:
**Step 1: Create Migration Files for Models:**
```
python manage.py makemigrations
```

**Step 2: Apply Migrations to Update the Database Schema:**
```
python manage.py migrate
```

## Run the Project:
**Default Port (8000):**
```
python manage.py runserver
```
**Custom Port:**
To run the project on a custom port, e.g., `9000`:

```
python manage.py runserver 0.0.0.0:9000
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Notes:
- Ensure Python is installed and added to your PATH.
- Use python3 explicitly on Linux if python defaults to Python 2.
- To confirm, after activation, you can check the Python interpreter being used:
```
python --version
```

OR

```
which python
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 🤝Contributing
**We welcome contributions! Follow these steps to get started:**

**1.Fork the repository**

Click on the `Fork` button at the top-right corner of this repository to create your copy.

**2.Clone your forked repository**
```
git clone https://github.com/your-username/ssl_checker.git
```
```
cd AI-Powered-Code-Review-System
```
**3.Create a new feature branch**
```
git checkout -b feature/your-feature-name
```
**4.Make your changes**

Edit the codebase to implement your feature or fix.

**5.Commit your changes**

Use clear and concise commit messages.
```
git commit -m "Add [your feature or fix description]"
```
**6.Push your branch**
```
git push origin feature/your-feature-name
```
**7.Create a Pull Request**

Open a pull request from your feature branch to the main repository. Provide a detailed explanation of the changes made.

## 🤝 Support

**⭐ Star the repository on GitHub**

---

