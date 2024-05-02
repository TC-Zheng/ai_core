from dotenv import load_dotenv
import os


class AppConfig:
    def __init__(self) -> None:
        load_dotenv(override=True)
        self._load_env_vars()

    def _load_env_vars(self) -> None:
        self.DATABASE_URL = os.getenv("DATABASE_URL")
        self.LLM_STORAGE_PATH = os.getenv("LLM_STORAGE_PATH")


# Make a singleton instance of the Config class
appConfig = AppConfig()


def get_app_config() -> AppConfig:
    return appConfig
