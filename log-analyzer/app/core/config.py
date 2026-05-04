from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()


class Config(BaseSettings):
    PROJECT_NAME:str = os.getenv("PROJECT_NAME", "fast-api-backend-template")
    VERSION:str = "v1"
    DATABASE_URL : str = os.getenv("DATABASE_URL")



config=Config()