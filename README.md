# 🎸 Band Site – Django Project

This is a portfolio-level Django web application that features authentication, navigation, and dynamic content for a music band site.

---

## 🔧 Local Setup with Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate       # Windows
source venv/bin/activate      # macOS/Linux

pip install -r requirements.txt
cd my-static-site
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

## 🐳 Docker Setup

### Step 1: Build the Docker Image

```bash
docker build -t bandsite-app .
```

### Step 2: Run the Docker Container

```bash
docker run -d -p 8000:8000 bandsite-app
```

Make sure your `Dockerfile` includes the commands to expose port 8000 and run the Django server.

---

## 🗂️ Project Structure

- `my-static-site/`: Django project directory
- `requirements.txt`: Python dependencies
- `Dockerfile`: Instructions to containerize the app
- `README.md`: You're reading it!
- `docs/`: (If present) Sphinx documentation for codebase

---

## 📝 Documentation

If you're using Sphinx, navigate to your `docs/` folder and run:

```bash
sphinx-build -b html . _build/html
```

Make sure your `conf.py` includes:
```python
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon']
```

---

## 🚀 Author

Lindokuhle Nqwala  
🔗 [GitHub Portfolio](https://github.com/Lindokuhle-Nqwala)

