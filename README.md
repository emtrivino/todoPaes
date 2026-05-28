# TodoPAES MVP (Python-first local development)

TodoPAES now ships with a **Python-only default workflow**: FastAPI API + built-in server-rendered UI (Jinja2), no Node.js/npm required.

## Quickstart (Windows CMD + PyCharm friendly)
```bat
cd backend
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -e .
python -m app.seed.seed_data --reset
python -m uvicorn app.main:app --reload --port 8000
```

Open:
- http://127.0.0.1:8000
- http://127.0.0.1:8000/docs

Demo user after seed:
- demo@todopaes.cl
- demo1234

## PyCharm setup
1. Open the **repository root** folder in PyCharm.
2. Set interpreter to `backend/.venv`.
3. Create a Run Configuration:
   - Module name: `uvicorn`
   - Parameters: `app.main:app --reload --port 8000`
   - Working directory: `backend`
4. Run seed in terminal:
   - `python -m app.seed.seed_data`
   - or safe reset: `python -m app.seed.seed_data --reset`
5. Start run config and browse:
   - `http://127.0.0.1:8000`
   - `http://127.0.0.1:8000/docs`

## Windows helper scripts (CMD)
- `scripts\setup_backend.bat`
- `scripts\run_backend.bat`
- `scripts\reset_db.bat`

## Backend notes
- Supported target versions: Python 3.10, 3.11, 3.12.
- Use `python` commands (not `py`).
- Main API endpoints remain available under `/api/v1/*`.

## Frontend status
- `frontend/` (Next.js) remains in the repository as optional/legacy.
- It is **not required** for default local development.

## Troubleshooting schema mismatch
If local SQLite schema is out-of-date, seed prints a clear message and stops.
Run:
```bat
python -m app.seed.seed_data --reset
```
This reset is explicit and avoids silent data loss.
