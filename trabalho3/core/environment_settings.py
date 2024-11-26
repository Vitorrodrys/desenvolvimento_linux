from pydantic_settings import BaseSettings


class ENVSettings(BaseSettings):
    DB_FILENAME: str


env_settings = ENVSettings()
