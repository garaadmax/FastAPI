import os
from dotenv import load_dotenv ,dotenv_values
from pydantic_settings import BaseSettings, SettingsConfigDict
load_dotenv()

class Settings(BaseSettings):
    #bot_token: str = os.getenv("BOT_TOKEN")
    database_url: str = os.getenv("DATABASE_URL")
    model_config = SettingsConfigDict(env_file=".env",extra="ignore")

Config = Settings()