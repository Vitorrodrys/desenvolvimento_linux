from typing import Generic, Optional, Type, TypeVar

from db import create_db_session
from models import Base

ModelType = TypeVar("ModelType", bound=Base)

class CRUD(Generic[ModelType]):

    def __init__(self, model: Type[ModelType]):
        self.__model = model
        self._db_session = create_db_session()

    def __del__(self):
        self._db_session.close()

    def create(self, data: ModelType) -> ModelType:
        self._db_session.add(data)
        self._db_session.commit()
        self._db_session.refresh(data)
        return data

    def remove(self, data_id: int) -> Optional[ModelType]:
        data = self._db_session.get(self.__model, data_id)
        if not data:
            return None
        self._db_session.delete(data)
        self._db_session.commit()
        return data

    def get(self, data_id: int) -> Optional[ModelType]:
        return self._db_session.get(self.__model, data_id)

    def update(self, data: ModelType) -> ModelType:
        updated_data = self._db_session.merge(data)
        self._db_session.commit()
        self._db_session.refresh(updated_data)
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
        existing_data = self._db_session.get(self.__model, data_id)
        if not existing_data:
            return None
        for key, value in new_data.items():
            setattr(existing_data, key, value)
        self._db_session.commit()
        self._db_session.refresh(existing_data)
        return existing_data
