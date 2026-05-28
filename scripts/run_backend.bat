@echo off
cd /d %~dp0\..\backend
call .venv\Scripts\activate
python -m uvicorn app.main:app --reload --port 8000
