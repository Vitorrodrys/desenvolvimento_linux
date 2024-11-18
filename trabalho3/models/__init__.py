from db import create_db_session

from .base import Base
from .game import Game, GameDeveloper, Platform


_, engine = create_db_session()

Base.metadata.create_all(engine)