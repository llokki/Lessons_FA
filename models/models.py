from sqlalchemy import MetaData, Table, Column, Integer, Boolean, String, TIMESTAMP, ForeignKey, JSON, create_engine, event
from datetime import datetime

metadata = MetaData()

role = Table(
    "role",
    metadata, #для миграции
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("permission", JSON),
)

user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String,nullable=False),
    Column("username", String, nullable=False),
    Column("hashed_password", String, nullable=False),
    Column("registered_at", TIMESTAMP, default=datetime.utcnow),#не utcnow(), чтобы каждый раз заново вызывалась функция
    Column("role_id", Integer, ForeignKey(role.c.id)),
    Column("is_active", Boolean, default=False, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),
    Column("is_verified", Boolean, default=True, nullable=False)
)
