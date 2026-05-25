from pydantic import BaseModel, EmailStr
class UserOut(BaseModel): id:int; email:EmailStr; full_name:str
class Config: from_attributes=True
