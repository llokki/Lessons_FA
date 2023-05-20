from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, JSON, create_engine, event
from datetime import datetime

metadata = MetaData()

roles = Table(
    "roles",
    metadata, #для миграции
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("permission", JSON),
)

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String,nullable=False),
    Column("username", String, nullable=False),
    Column("password", String, nullable=False),
    Column("registered_at", TIMESTAMP, default=datetime.utcnow),#не utcnow(), чтобы каждый раз заново вызывалась функция
    Column("role_id", Integer, ForeignKey("roles.id")),
)
