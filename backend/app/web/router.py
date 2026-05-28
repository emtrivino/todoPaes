from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.core.security import hash_password, verify_password
from app.models.attempt import Attempt
from app.models.question import Question
from app.models.subject import Subject
from app.models.user import User
from app.services.dashboard_service import DashboardService

web_router = APIRouter(include_in_schema=False)
templates = Jinja2Templates(directory="app/templates")


def _current_user(request: Request, db: Session) -> User | None:
    email = request.cookies.get("todopaes_user")
    if not email:
        return None
    return db.query(User).filter_by(email=email).first()


@web_router.get("/", response_class=HTMLResponse)
def home(request: Request, db: Session = Depends(get_db)):
    return templates.TemplateResponse(
        request,
        "home.html",
        {"user": _current_user(request, db), "subjects": db.query(Subject).all()},
    )


@web_router.get("/login", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse(request, "login.html", {"error": None})


@web_router.post("/login", response_class=HTMLResponse)
def login_submit(request: Request, email: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    user = db.query(User).filter_by(email=email).first()
    if not user or not verify_password(password, user.hashed_password):
        return templates.TemplateResponse(request, "login.html", {"error": "Credenciales inválidas"}, status_code=401)
    response = RedirectResponse(url="/dashboard", status_code=303)
    response.set_cookie("todopaes_user", user.email, httponly=True, samesite="lax")
    return response


@web_router.get("/register", response_class=HTMLResponse)
def register_page(request: Request):
    return templates.TemplateResponse(request, "register.html", {"error": None})


@web_router.post("/register")
def register_submit(full_name: str = Form(...), email: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    if db.query(User).filter_by(email=email).first():
        return RedirectResponse(url="/register?error=1", status_code=303)
    db.add(User(full_name=full_name, email=email, hashed_password=hash_password(password)))
    db.commit()
    response = RedirectResponse(url="/dashboard", status_code=303)
    response.set_cookie("todopaes_user", email, httponly=True, samesite="lax")
    return response


@web_router.get("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request, db: Session = Depends(get_db)):
    user = _current_user(request, db)
    if not user:
        return RedirectResponse(url="/login", status_code=303)
    summary = DashboardService.build_summary(db, user.id)
    return templates.TemplateResponse(request, "dashboard.html", {"user": user, "summary": summary})


@web_router.get("/subjects", response_class=HTMLResponse)
def subjects(request: Request, db: Session = Depends(get_db)):
    return templates.TemplateResponse(request, "subjects.html", {"subjects": db.query(Subject).all()})


@web_router.get("/practice", response_class=HTMLResponse)
def practice(request: Request, db: Session = Depends(get_db)):
    return templates.TemplateResponse(request, "practice.html", {"questions": db.query(Question).filter_by(is_active=True).limit(20).all()})


@web_router.post("/practice/{question_id}")
def practice_answer(question_id: int, selected_option: str = Form(...), request: Request = None, db: Session = Depends(get_db)):
    user = _current_user(request, db)
    if not user:
        return RedirectResponse(url="/login", status_code=303)
    question = db.query(Question).filter_by(id=question_id, is_active=True).first()
    if not question:
        return RedirectResponse(url="/practice", status_code=303)
    is_correct = selected_option == question.correct_option
    db.add(Attempt(user_id=user.id, question_id=question_id, selected_option=selected_option, is_correct=is_correct))
    db.commit()
    return RedirectResponse(url=f"/results?correct={int(is_correct)}&question_id={question_id}", status_code=303)


@web_router.get("/results", response_class=HTMLResponse)
def results(request: Request, question_id: int, correct: int = 0, db: Session = Depends(get_db)):
    q = db.query(Question).filter_by(id=question_id).first()
    return templates.TemplateResponse(request, "results.html", {"question": q, "correct": bool(correct)})
