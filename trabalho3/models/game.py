from enum import StrEnum
from typing import Optional

from sqlalchemy import Column, ForeignKey
from sqlalchemy import Float, Integer, String, Table
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column, relationship


from .base import Base


class GameGenre(StrEnum):
    ACTION = "Action"
    ADVENTURE = "Adventure"
    RPG = "Role-Playing Game"
    FPS = "First-Person Shooter"
    STRATEGY = "Strategy"
    SIMULATION = "Simulation"
    PUZZLE = "Puzzle"
    SPORTS = "Sports"
    HORROR = "Horror"
    PLATFORMER = "Platformer"

class Platform(Base):
    __tablename__ = 'platforms'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)

game_gamedev_link = Table(
    'game_gamedev_link',
    Base.metadata,
    Column('game_id', Integer, ForeignKey('games.id')),
    Column('game_developer_id', Integer, ForeignKey('game_developers.id')),
)

class GameDeveloper(Base):

    __tablename__ = 'game_developers'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    games: Mapped[list["Game"]] = relationship("Game", back_populates="game_developer")

class Game(Base):
    __tablename__ = 'games'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    game_developer_id: Mapped[int] = mapped_column(ForeignKey("game_developers.id"))
    game_developer: Mapped["GameDeveloper"] = relationship("GameDeveloper", back_populates="games")
    genre: Mapped[GameGenre] = mapped_column(String(50))
    description: Mapped[Optional[str]] = mapped_column(String(500))
    price: Mapped[float] = mapped_column(Float())
