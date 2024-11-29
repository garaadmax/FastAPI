# from pydantic import BaseSettings
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    # app_name: str
    # debug: bool = False

    # model_config = SettingsConfigDict(
    #     env=".env",
    #     extra="ignore"
    # )
    model_config = {
        "env": ".env",
        "extra": "ignore"
    }
config = Settings()