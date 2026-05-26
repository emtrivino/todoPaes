from pydantic import BaseModel
class UserOut(BaseModel): id:int; email:str; full_name:str
class Config: from_attributes=True
