import os
from sqlalchemy import create_engine

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://pg_user:pg_password@db:5432/fastapi_db",
)

engine = create_engine(DATABASE_URL)