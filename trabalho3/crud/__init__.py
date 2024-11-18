from models import Game, GameDeveloper, Platform

from .crud_base import CRUD


crud_game = CRUD(Game)
crud_game_developer = CRUD(GameDeveloper)
crud_platform = CRUD(Platform)
