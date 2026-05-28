@echo off
cd /d %~dp0\..\backend
call .venv\Scripts\activate
python -m app.seed.seed_data --reset
