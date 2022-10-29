from pydantic import BaseSettings

class Settings(BaseSettings):
    url_database: str = "postgresql://postgres:postgres@localhost:5432/postgres"
