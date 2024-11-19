from typing import Generic, Optional, Type, TypeVar

from db import create_db_session
from models import Base

ModelType = TypeVar("ModelType", bound=Base)

class CRUD(Generic[ModelType]):

    def __init__(self, model: Type[ModelType]):
        self.__model = model

    def create(self, data: ModelType) -> ModelType:
        with create_db_session() as session:
            session.add(data)
            session.commit()
            session.refresh(data)
            return data

    def remove(self, data_id: int) -> Optional[ModelType]:
        with create_db_session() as session:
            data = session.get(self.__model, data_id)
            if not data:
                return None
            session.delete(data)
            session.commit()
            return data

    def get(self, data_id: int) -> Optional[ModelType]:
        with create_db_session() as session:
            return session.get(self.__model, data_id)

    def update(self, data: ModelType) -> ModelType:
        with create_db_session() as session:
            updated_data = session.merge(data)
            session.commit()
            session.refresh(updated_data)
            return updated_data

    def update_fields(self, data_id: int, new_data: dict) -> Optional[ModelType]:
        """
        Update an object into database with base at new_data dict keys and values.
        Example:
            new_data = {
                name: "New Name",
                description: "New Description"
            }
        only the fields name and description will be updated into object with data_id.
        """
        with create_db_session() as session:
            existing_data = session.get(self.__model, data_id)
            if not existing_data:
                return None
            for key, value in new_data.items():
                setattr(existing_data, key, value)
            session.commit()
            session.refresh(existing_data)
            return existing_data
