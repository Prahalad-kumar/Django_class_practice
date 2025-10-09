# DAY1
---
# 📘 Django & Web Fundamentals — Clean Notes

Welcome — these notes cover core software concepts, software architecture patterns, Django request/response basics, Internet protocols, and development environments. They're organized for quick studying and as a handy reference.

---

## 📑 Table of Contents
1. [What is Software?](#what-is-software)
2. [Types of Software](#types-of-software)
3. [What is an Application?](#what-is-an-application)
4. [Software Architecture](#software-architecture)
   - Purpose
   - Components
   - Common architecture patterns
5. [Django: Server, Request & Response](#django-server-request--response)
   - Request/Response cycle
   - Common code examples
6. [Internet & Protocols](#internet--protocols)
7. [Development Environments & Virtual Environments](#development-environments--virtual-environments-venv)
8. [Study Tips & Quick Cheatsheet](#study-tips--quick-cheatsheet)

---

## 🖥️ What is Software?

**Definition**
Software is the collection of programs, instructions, and data that direct a computer to perform tasks. It is the intangible (non-physical) part of a computer system.

**Examples**: Operating Systems (Windows, Linux), web browsers (Chrome, Firefox), productivity apps (MS Word), games.

---

## ⚙️ Types of Software

Software is commonly split into two main categories:

### A. System Software
- Purpose: Manages hardware and provides core services for other software.
- Examples: Operating systems (Windows, macOS, Linux), device drivers, utility programs (antivirus, disk tools).
- Role: Provides the platform that other applications run on.

### B. Application Software
- Purpose: Helps users perform specific tasks.
- Examples: Word processors, spreadsheets, web browsers, media players.
- Role: Directly used by end users to accomplish tasks.

> ✅ Tip: "All applications are software, but not all software is an application." System software supports the system; applications serve users.

---

## 📲 What is an Application?

An application (app) is software designed to perform a particular task for the user, e.g., a word processor or a mobile messaging app.

Examples:
- Desktop: MS Word, Excel, Chrome
- Mobile: WhatsApp, Instagram, Calculator, YouTube

---

## 🧠 Software Architecture

**Definition**
Software architecture is the high-level structure of a software system—how components are organized, how they interact, and how the system meets required qualities (scalability, reliability, security).

### 🏗️ Purpose
- Organize code into modules and components
- Improve performance and scalability
- Enable easier maintenance and upgrades
- Communicate design decisions to stakeholders
- Ensure reliability and security

### 🧩 Main Components
- Components: Modules, services, classes
- Connectors: APIs, messaging, function calls
- Configuration: How components and connectors are arranged

---

## 🧱 Common Architecture Patterns

### 1) Layered (n-tier)
- Structure: Presentation → Business Logic → Data Access → Database
- When to use: Traditional web apps, enterprise systems
- Pros: Clear separation, easier testing and maintenance
- Cons: Can become monolithic, harder to scale selectively

### 2) Client-Server
- Structure: Clients (browsers/mobile apps) request services from central servers
- Use: Web apps, email, many networked services
- Pros: Centralized control, simpler data consistency
- Cons: Single-server bottlenecks if not scaled

### 3) Microservices
- Structure: Small, independently deployable services communicating via APIs
- Use: Large-scale distributed systems (Netflix, Amazon)
- Pros: Independent scaling, fault isolation, polyglot stacks
- Cons: Operational complexity, network latency, distributed data challenges

---

## 🟦 Django — Server, Request & Response

This section contains essentials you need for understanding Django's request/response flow and examples you can copy-paste.

### 1) Development server
- Command to run: `python manage.py runserver`
- Purpose: Local development server; not for production use.

### 2) HttpRequest (what it holds)
Important attributes:
- `request.method` — HTTP method (GET, POST, etc.)
- `request.GET` — Query parameters (a dict-like object)
- `request.POST` — Form data (for POST requests)
- `request.path` — URL path
- `request.user` — Authenticated user (if authentication middleware is enabled)

Example view:

```python
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello, Django!")
```

Rendering templates:

```python
from django.shortcuts import render

def index(request):
    context = {"title": "Home"}
    return render(request, "index.html", context)
```

Returning JSON (useful for APIs):

```python
from django.http import JsonResponse

def api_example(request):
    data = {"status": "ok", "items": []}
    return JsonResponse(data)
```

### 3) Request → Response cycle (simplified)
1. Browser sends HTTP request to URL
2. Django URL dispatcher matches the URL
3. View function is called with `HttpRequest`
4. View processes data and returns an `HttpResponse` (or raises an error)
5. Response is sent back to the browser

### 4) Common HTTP methods used in Django
- GET — Read/retrieve data
- POST — Create/submit data
- PUT/PATCH — Update data (often used with REST frameworks)
- DELETE — Remove data (often used with REST frameworks)

---

## 🌍 Internet & Protocols — Quick Guide

**Internet**: A global network that connects devices and allows them to communicate using standardized protocols.

**Protocol**: A set of rules that define how data is transmitted and handled between devices.

### Key protocols you should know
| Protocol | Purpose | Default Port | Example Use |
|---|---:|:---:|---|
| HTTP | Transfer web pages | 80 | Web browsing (non-encrypted) |
| HTTPS | Secure web transfer (HTTP over TLS) | 443 | Secure websites |
| FTP | File transfer | 20/21 | Uploading files (legacy) |
| SMTP | Sending email | 25 | Sending mail (Django send_mail) |
| POP3 | Retrieving email (download) | 110 | Email clients that download mail |
| IMAP | Accessing email on server | 143 / 993 | Email syncing across devices |
| TCP/IP | Underlying transport & addressing | — | All internet traffic |
| DNS | Name → IP resolution | 53 | Converting example.com → 1.2.3.4 |

**Notes:**
- Use HTTPS for production web apps to protect user data.
- For file transfers, prefer SFTP over FTP for secure transfers.

---
 # DAY 2:

## 🧰 Development Environments & Virtual Environments (venv)

### What is a development environment?
- A development environment is the combination of OS, Python interpreter, libraries, and configuration you use to build and run your project. Keeping environments isolated per-project avoids dependency conflicts and makes deployments predictable.

### Why use a virtual environment?
- Isolates project dependencies from system Python.
- Prevents version conflicts between projects.
- Makes dependency management reproducible (use requirements.txt or pyproject.toml).

### Creating and using a virtual environment (recommended)

1. Create a venv in the project directory:

```bash
# Unix / macOS / Linux
python3 -m venv .venv

# or explicitly with python
python -m venv .venv
```

2. Activate the virtual environment:

```bash
# Bash / Zsh (Linux, macOS)
source .venv/bin/activate

# Fish shell
source .venv/bin/activate.fish

# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1

# Windows (cmd.exe)
.\.venv\Scripts\activate.bat
```

3. Install packages and manage dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install django
python -m pip freeze > requirements.txt

# install from requirements
python -m pip install -r requirements.txt
```

4. Deactivate when done:

```bash
deactivate
```

### Alternative tools
- `virtualenv` (older tool) — creates venvs and works on systems where venv is not available.
- `pipx` — run and install Python CLI tools globally in isolated environments.
- `poetry` or `pip-tools` — for dependency management and lock files.

### Best practices
- Use a directory name like `.venv` (hidden) so it's obvious and can be added to `.gitignore`.
- Check `sys.executable` in Python to confirm which Python is running.
- Commit `requirements.txt` (or lock file) but not the virtual environment itself.

Add to `.gitignore`:

```
.venv/
__pycache__/
*.py[cod]
```

### Small Python snippet — inspect current environment

Save the snippet below as `show_venv_info.py` and run it inside your venv to confirm activation and paths:

```python
# show_venv_info.py
import sys
import os

print("Python executable:", sys.executable)
print("Python version:", sys.version.splitlines()[0])
print("Virtual environment detected:", bool(os.environ.get('VIRTUAL_ENV')))
print("VIRTUAL_ENV:", os.environ.get('VIRTUAL_ENV'))
print("sys.path (first 5 entries):")
for p in sys.path[:5]:
    print("  -", p)

# Example usage:
# $ python show_venv_info.py
```

---

## ✅ Study Tips & Quick Cheatsheet
- Draw diagrams: map components and arrows for connectors.
- Memorize the request/response cycle steps and a few key HttpRequest attributes.
- For architecture patterns, remember the trade-offs (simplicity vs scalability).
- Keep a small code snippet file for Django view examples you can copy into projects.

---

# DAY 3:

## Basic of Django

Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. It follows the "batteries-included" philosophy: most common web development tasks are provided out of the box.

Key concepts (quick overview):

- Project vs App:
    - Project: The entire website/configuration (created with `django-admin startproject projectname`).
    - App: A reusable component that provides a specific feature (created with `python manage.py startapp appname`). A project can contain multiple apps.

- Important files and folders:
    - `manage.py` — command-line utility for running tasks (runserver, migrations, shell).
    - `settings.py` — global configuration (installed apps, DB config, middleware, templates, static files).
    - `urls.py` — URL routing table for mapping paths to views.
    - `models.py` — data models (ORM classes) for database tables.
    - `views.py` — request handlers that return responses (HTML, JSON, redirects).
    - `templates/` — HTML templates rendered by views.
    - `static/` — static assets (CSS, JS, images).

- Common development workflow:
    1. Create project and app.
    2. Define models in `models.py` and run `makemigrations` / `migrate`.
    3. Create views in `views.py` and map them in `urls.py`.
    4. Add templates and static files.
    5. Run `python manage.py runserver` and test locally.

Small example (model, view, url, template):

```python
# models.py
from django.db import models

class Item(models.Model):
        name = models.CharField(max_length=200)
        description = models.TextField(blank=True)

        def __str__(self):
                return self.name
```

```python
# views.py
from django.shortcuts import render
from .models import Item

def index(request):
        items = Item.objects.all()
        return render(request, 'myapp/index.html', {'items': items})
```

```python
# urls.py (in app)
from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
]
```

```html
<!-- templates/myapp/index.html -->
<!doctype html>
<html>
    <head><title>Items</title></head>
    <body>
        <h1>Items</h1>
        <ul>
            {% for item in items %}
                <li>{{ item.name }} — {{ item.description }}</li>
            {% empty %}
                <li>No items yet.</li>
            {% endfor %}
        </ul>
    </body>
</html>
```

## Features of Django

Django provides a rich set of built-in features that speed up development and help you build secure, maintainable web applications.

- Rapid development: sensible defaults and many high-level helpers let you build quickly.
- Batteries included: admin, ORM, templating, forms, authentication, sessions, and more.
- ORM (Object-Relational Mapper): define models in Python and interact with the database using a high-level API.
- Automatic admin interface: a generated admin UI for managing models (configurable and extensible).
- Security: built-in protection against common vulnerabilities (CSRF, XSS, SQL injection, clickjacking) and strong password handling.
- Scalability: support for caching, database sharding, and pluggable components.
- URL dispatching: clean, readable URL routing with named routes.
- Templating engine: safe and expressive template language with inheritance and filters.
- Forms and validation: helpers to generate forms, validate input, and re-render with errors.
- Internationalization (i18n) and localization (l10n): built-in tools for translating and formatting.
- Middleware: a simple way to plug code into request/response processing.
- Testing: integrated test framework (based on unittest) and test client for request simulation.

When to use Django:
- Building CRUD apps, content sites, dashboards, admin tools, or APIs (with Django REST Framework for more advanced APIs).

## What is MVT (Model–View–Template)?

MVT is the architectural pattern Django follows. It's very similar to MVC (Model–View–Controller) but adapted for web development and Django's design choices.

- Model: The data layer. Models are Python classes (subclassing `django.db.models.Model`) that describe database tables and provide a high-level API for querying and manipulating data.

- View: The business logic / controller in practice. In Django, a "view" is a Python callable (function or class-based view) that receives an `HttpRequest` and returns an `HttpResponse`. Views handle input, fetch or save data through models, and select templates to render.

- Template: The presentation layer. Templates are HTML (or other text formats) with placeholders and template tags that render dynamic data passed from views.

How data flows (simple):
1. URL dispatcher maps an incoming request to a view.
2. View uses Models to read/write data and prepares context data.
3. View renders a Template with context and returns an HttpResponse.

Mapping MVT → practical files:
- Model: `myapp/models.py`
- View: `myapp/views.py` (or `myapp/views/*.py` for larger apps; class-based views often live in `views.py`)
- Template: `templates/myapp/*.html`

Example (full flow recap):
- User visits `/` → URL pattern routes to `views.index`.
- `views.index` queries `Item.objects.all()` (Model) and calls `render(request, 'myapp/index.html', {'items': items})`.
- Template `myapp/index.html` loops over `items` and renders HTML for the browser.

Best practices and notes:
- Keep views thin: most logic should live in models, model managers, or services/helpers to keep views simple and testable.
- Use class-based views for repeated patterns (ListView, DetailView, CreateView, UpdateView) to reduce boilerplate.
- Keep templates focused on presentation — avoid heavy logic in templates.
- Use Django's forms and model forms to handle validation and rendering of input safely.

---
````