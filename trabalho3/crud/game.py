from models import Game

from .base import CRUD


class CRUDGame(CRUD):

    def get_by_name(self, name:str) -> Game:
        return self._db_session.query(Game).filter(Game.name.like(f"%{name}%")).all()


crud_game = CRUDGame(Game)
