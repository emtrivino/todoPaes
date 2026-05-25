from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    APP_NAME:str="TodoPAES";ENV:str="local";DATABASE_URL:str="sqlite:///./todopaes.db";SECRET_KEY:str="change-me";ACCESS_TOKEN_EXPIRE_MINUTES:int=1440;FRONTEND_URL:str="http://localhost:3000";OPENAI_API_KEY:str="";AI_PROVIDER:str="openai";AI_MOCK_MODE:bool=True
    class Config: env_file=".env"
settings=Settings()
