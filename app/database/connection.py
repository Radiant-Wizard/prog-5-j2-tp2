import psycopg2
from app.core.config import settings


def getConnection():
    return psycopg2.connect(
        host=settings.DB_HOST,
        port=settings.DB_PORT,
        user=settings.DB_USERNAME,
        password=settings.DB_PASSWORD,
        database=settings.DB_NAME,
    )
