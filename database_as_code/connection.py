import os

from sqlalchemy import Engine, create_engine
from sqlalchemy.engine.url import URL


def connection() -> Engine:
    """
    Create the connection with the database using the ENV VARS:
        DRIVERNAME
        DB_USERNAME
        DB_PASSWORD
        DB_HOST
        DB_PORT
        DATABASE
    One possible TODO here is to give the chance to pass like an
    argument and
    """
    drivername = os.getenv("DRIVERNAME")
    username = os.getenv("DB_USERNAME")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    port = int(os.getenv("DB_PORT"))
    database = os.getenv("DATABASE")

    db_url = URL.create(
        drivername=drivername,
        username=username,
        password=password,
        host=host,
        port=port,
        database=database,
    )
    engine = create_engine(db_url)
    return engine
