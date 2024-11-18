from typing import Generic, TypeVar, Type

from db import create_db_session
from models import Base


ModelType = TypeVar("ModelType", bound=Base)



class CRUD(Generic[ModelType]):

    def __init__(self, model: Type[ModelType]):
        session, _ = create_db_session()
        self.__session = session
        self.__model = model

    def create(self, data: ModelType) -> ModelType:
        with self.__session() as session:
            session.add(data)
            session.commit()
            session.refresh(data)
            return data

    def remove(self, data_id: int) -> ModelType:
        with self.__session() as session:
            data = session.query(self.__model).get(data_id)
            session.delete(data)
            session.commit()
            return data

    def get(self, data_id: int) -> ModelType:
        with self.__session() as session:
            return session.query(self.__model).get(data_id)

    def update(self, data: ModelType) -> ModelType:
        with self.__session() as session:
            session.commit()
            session.refresh(data)
            return data
