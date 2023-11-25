import os
from pydantic import validator, ValidationError
from pydantic_settings import BaseSettings
from functools import lru_cache

# Assume que o ".env" está na raiz do projeto
dotenv_path = os.path.dirname(__file__) + "/../../.env"
print(dotenv_path)


# Classe de configurações. Regras de inicialização e configuração são documentadas pelo pydantic.
# https://pydantic-docs.helpmanual.io/usage/settings/


class Settings(BaseSettings):
    DB_URL: str
    DB_ECHO: bool = False
    DB_POOL_SIZE: int = 20

    SECRET_KEY: str
   
    @validator("DB_URL")
    def change_database_prefix(cls, url: str):  # pylint: disable=no-self-argument
        # Transforma um prefixo de "postgres://" em "postgresql://". O objetivo disso é providenciar suporte à
        # extensão do Postgres do Heroku, a qual define o URL do banco de dados com o prefixo "postgres://", o
        # qual causa erros no carregamento do driver de DB utilizado pelo SQLAlchemy.

        if url.startswith("postgres://"):
            return url.replace("postgres://", "postgresql://", 1)
        return url
    
    class Config:
        env_file = dotenv_path
        env_file_encoding = "utf-8"
    

class SettingsException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


@lru_cache  # ver também: https://fastapi.tiangolo.com/advanced/settings/#settings-in-a-dependency
def get_settings():
    try:
        return Settings()
    except ValidationError as ve:
        details = [f'{error["loc"]}: {error["msg"]}' for error in ve.errors()]
        msg = f"Falha ao carregar variáveis de ambiente: {details}"
        raise SettingsException(msg) from ve


   