from pydantic import BaseModel


class SubjectOut(BaseModel):
    id: int
    code: str
    name: str

    class Config:
        from_attributes = True
