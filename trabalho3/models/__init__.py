from db import create_all

from .base import Base
from .game import Game, GameDeveloper, GameGenre, Platform


create_all(Base)
