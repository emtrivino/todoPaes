# TodoPAES MVP

Monorepo MVP para preparar la PAES con enfoque diario tipo app.

## Requisitos
- Python 3.11+
- Node.js 20+
- Git
- PyCharm

## Backend
```bash
cd backend
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate
pip install -e .
cp ../.env.example .env
python -m app.seed.seed_data
uvicorn app.main:app --reload --port 8000
```

## Frontend
```bash
cd frontend
npm install
npm run dev
```

Abrir:
- Backend docs: http://localhost:8000/docs
- Frontend: http://localhost:3000

Demo:
- demo@todopaes.cl
- demo1234

## PyCharm
1. Abre la carpeta raíz `todopaes` en PyCharm.
2. Configura el intérprete backend con `backend/.venv`.
3. Crea Run Configuration:
   - Module name: `uvicorn`
   - Parameters: `app.main:app --reload --port 8000`
   - Working directory: `backend`
4. En terminal de frontend ejecuta `npm run dev`.

## GitHub push
```bash
git init
git add .
git commit -m "Initial TodoPAES MVP"
```

Opción A (GitHub CLI):
```bash
gh repo create todopaes --private --source=. --remote=origin --push
```

Opción B (manual):
```bash
git remote add origin https://github.com/YOUR_USER/todopaes.git
git branch -M main
git push -u origin main
```

## Roadmap sugerido
- Importador de datos oficiales de admisión
- Suscripciones con MercadoPago (TODO)
- Más asignaturas PAES
- Motor adaptativo
- CMS admin
- SEO/Blog
- Wrapper móvil
