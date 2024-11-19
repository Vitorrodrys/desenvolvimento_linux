from db import create_all

from .base import Base
from .game import Game, GameDeveloper, Platform, game_gamedev_link


create_all(Base)
