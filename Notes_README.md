

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


