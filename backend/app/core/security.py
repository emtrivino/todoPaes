from datetime import datetime,timedelta
from jose import jwt
from passlib.context import CryptContext
from app.core.config import settings
pwd=CryptContext(schemes=["bcrypt"],deprecated="auto")
def hash_password(p:str)->str:return pwd.hash(p)
def verify_password(p,h):return pwd.verify(p,h)
def create_access_token(sub:str):
    return jwt.encode({"sub":sub,"exp":datetime.utcnow()+timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)},settings.SECRET_KEY,algorithm="HS256")
