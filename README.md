# StagePass 🎟️

StagePass is a modern backend platform for **event management and ticketing**.  
It is currently under active development and aims to deliver a clean, modular, and future‑proof architecture.

## ✨ Features

- User, event, and ticket management
- Modular monolith architecture
- Isolated testing with SQLite and Postgres
- CI/CD with GitHub Actions
- Docker & Kubernetes ready

## 🛠️ Tech Stack

- **Python 3.12**
- **FastAPI** (API framework)
- **SQLAlchemy 2.0** (ORM)
- **Alembic** (migrations)
- **Postgres** (main database)
- **SQLite in-memory** (tests)
- **Pytest + Coverage** (testing)
- **Passlib / Argon2** (password security)
- **GitHub Actions** (CI/CD)

## 🚧 Development Status

This project is still in progress.  
The goal is to build a backend system that is **clear, maintainable, and onboarding‑friendly**.

## 🚀 Run Locally

```bash
pip install -r requirements.txt
uvicorn api.main:app --reload
```
