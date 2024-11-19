from typing import Type

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Session

from core import env_settings

_engine = create_engine(f"sqlite:///{env_settings.DB_FILENAME}", future=True)
_SessionLocal = sessionmaker(bind=_engine, autocommit=False, autoflush=False, class_=Session)

def create_db_session() -> Session:
    """
    Create a new session to interact with the database.
    """
    return _SessionLocal()

def create_all(base_class: Type[DeclarativeBase]):
    """
    Create all tables in the database.
    """
    base_class.metadata.create_all(bind=_engine)
