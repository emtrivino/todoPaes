from sqlalchemy import Column,Integer,String,DateTime
from sqlalchemy.sql import func
from app.core.database import Base
class User(Base):__tablename__="users";id=Column(Integer,primary_key=True);email=Column(String,unique=True,index=True);full_name=Column(String);hashed_password=Column(String);target_career=Column(String,nullable=True);target_university=Column(String,nullable=True);created_at=Column(DateTime,server_default=func.now());updated_at=Column(DateTime,server_default=func.now(),onupdate=func.now())
