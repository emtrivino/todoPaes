from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_current_user, get_db
from app.schemas.dashboard import DashboardOut
from app.services.dashboard_service import DashboardService

router = APIRouter()


@router.get("", response_model=DashboardOut)
def my_dashboard(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return DashboardService.build_summary(db, user.id)
