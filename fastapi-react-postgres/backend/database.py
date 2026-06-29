import os
from sqlalchemy import create_engine

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg://postgres:pg_password@db:5432/fastapi_db",
)

engine = create_engine(DATABASE_URL)