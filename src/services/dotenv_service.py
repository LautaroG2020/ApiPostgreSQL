from dotenv import load_dotenv, find_dotenv
import os

class DotenvService:
    initialized = False

    @staticmethod
    def _set_dotenv_path():
        dotenv_path = find_dotenv(".env.local")
        app_env = os.environ.get("ENVIRONMENT", "local")
        if app_env == "production":
            dotenv_path = find_dotenv(".env.production")

        load_dotenv(dotenv_path)
        DotenvService.initialized = True

    @staticmethod
    def get_env_variable(key: str):
        if not DotenvService.initialized:
            DotenvService._set_dotenv_path()
        return os.environ.get(key)