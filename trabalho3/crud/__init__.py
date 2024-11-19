from models import Game, GameDeveloper, Platform, game_gamedev_link

from .crud_base import CRUD


crud_game = CRUD(Game)
crud_game_developer = CRUD(GameDeveloper)
crud_platform = CRUD(Platform)
crud_gamedev_link = CRUD(game_gamedev_link)