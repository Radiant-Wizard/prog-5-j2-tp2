from psycopg2 import connect
from app.core.config import Settings


def getConnection():
    return connect(
        host=Settings.DB_HOST,
        port=Settings.DB_PORT,
        user=Settings.DB_USERNAME,
        password=Settings.DB_PASSWORD,
        database=Settings.DB_USERNAME,
    )
