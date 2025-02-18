import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class Settings(BaseSettings):
    # bot_token: str = os.getenv("BOT_TOKEN")
    database_url: str = os.getenv("DATABASE_URL")
    JWT_SECRET: str
    JWT_ALGORITHM: str
    REDIS_URL: str
    MAIL_SALT: str
    MAIL_USERNAME: str
    MAIL_PASSWORD: str
    MAIL_FROM: str
    MAIL_PORT: int
    MAIL_SERVER: str
    MAIL_FROM_NAME: str
    MAIL_STARTTLS: bool = True
    MAIL_SSL_TLS: bool = False
    USE_CREDENTIALS: bool = True
    VALIDATE_CERTS: bool = True
    DOMAIN: str
    OTP_SECRET: str
    OTP_LENGTH: int
    OTP_ALGORITHM: str
    OTP_VALIDITY: int
    ACCESS_TOKEN_EXPIRY: int
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


Config = Settings()

broker_url = Config.REDIS_URL
result_backend = Config.REDIS_URL
broker_connection_retry_on_startup = True
