from models import GameDeveloper, Platform, game_gamedev_link

from .base import CRUD
from .game import crud_game

crud_game_developer = CRUD(GameDeveloper)
crud_platform = CRUD(Platform)
crud_gamedev_link = CRUD(game_gamedev_link)


__all__ = [
    "crud_game"
]