import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    def __init__(self):
        self.DB_HOST: str = os.getenv("DB_HOST", "localhost")
        self.DB_PORT: str = os.getenv("DB_PORT", "5432")
        self.DB_USERNAME: str = os.getenv("DB_USERNAME", os.getenv("USER"))
        self.DB_PASSWORD: str = os.getenv("DB_PASSWORD", "password")
        self.DB_NAME: str = os.getenv("DB_NAME", "postgres")


settings = Settings()
