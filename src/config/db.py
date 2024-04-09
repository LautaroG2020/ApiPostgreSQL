import psycopg2
from src.services.dotenv_service import DotenvService

POSTGRESQL_DATABASE_USERNAME = DotenvService.get_env_variable("POSTGRESQL_DATABASE_USERNAME")
POSTGRESQL_DATABASE = DotenvService.get_env_variable("POSTGRESQL_DATABASE")
POSTGRESQL_DATABASE_PASSWORD = DotenvService.get_env_variable("POSTGRESQL_DATABASE_PASSWORD")
POSTGRESQL_DATABASE_SERVER = DotenvService.get_env_variable("POSTGRESQL_DATABASE_SERVER")


class Database:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname= POSTGRESQL_DATABASE,
            user= POSTGRESQL_DATABASE_USERNAME,
            password= POSTGRESQL_DATABASE_PASSWORD,
            host= POSTGRESQL_DATABASE_SERVER
        )
        self.cursor = self.conn.cursor()
