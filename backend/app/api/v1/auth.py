from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.schemas.auth import RegisterIn,LoginIn,TokenOut
from app.models.user import User
from app.core.security import hash_password,verify_password,create_access_token
router=APIRouter()
@router.post('/register',response_model=TokenOut)
def register(payload:RegisterIn,db:Session=Depends(get_db)):
 if db.query(User).filter_by(email=payload.email).first(): raise HTTPException(400,'Email ya registrado')
 u=User(email=payload.email,full_name=payload.full_name,hashed_password=hash_password(payload.password));db.add(u);db.commit()
 return TokenOut(access_token=create_access_token(payload.email))
@router.post('/login',response_model=TokenOut)
def login(payload:LoginIn,db:Session=Depends(get_db)):
 u=db.query(User).filter_by(email=payload.email).first()
 if not u or not verify_password(payload.password,u.hashed_password): raise HTTPException(401,'Credenciales inválidas')
 return TokenOut(access_token=create_access_token(u.email))
