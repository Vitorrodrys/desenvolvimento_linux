from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core import env_settings

def create_db_session():
    engine = create_engine(f"sqlite:///{env_settings.DB_FILENAME}")
    return sessionmaker(bind=engine), engine
