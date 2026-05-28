@echo off
cd /d %~dp0\..\backend
python -m venv .venv
call .venv\Scripts\activate
python -m pip install --upgrade pip
pip install -e .
