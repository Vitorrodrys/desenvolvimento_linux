from models import Game, GameDeveloper, Platform

from .base import CRUD

crud_game_developer = CRUD(GameDeveloper)
crud_game = CRUD(Game)
crud_platform = CRUD(Platform)


__all__ = ["crud_game"]
