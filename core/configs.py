from typing import List
from pydantic import BaseSettings

from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os

load_dotenv()


class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = os.getenv("DB_URL")
    DBBaseModel = declarative_base()
    
    JWT_SECRET: str = os.getenv("JWT_SECRET")
    """
    import secrets
    
    token: str = secrets.token_urlsafe(32)
    """
    
    ALGORITHM: str = 'HS256'
    # 1 Semana de token em minutos
    ACESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7
    
    class Config:
        case_sensitive = True
        
settings: Settings = Settings()