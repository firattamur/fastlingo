import os
from enum import Enum

import toml
from fastlingo.core.exceptions import FastLingoException
from fastlingo.core.logger import Logger


class ConfigKey(Enum):
    """Enum for the config keys."""

    TRANSLATION_SERVICE = "translation_service"
    API_KEYS = "api_keys"
    SOURCE_LANGUAGE = "source_language"
    TARGET_LANGUAGES = "target_languages"
    METADATA_FOLDER = "metadata_folder"
    FIELDS_TO_TRANSLATE = "fields_to_translate"
    CACHE = "cache"
    CACHE_FOLDER = "cache_folder"
    CACHE_ENABLED = "cache_enabled"


class Config:
    """Class for the config."""

    CONFIG_FILE_NAME = "fastlingo.toml"
    DEFAULT_CONFIG = {
        ConfigKey.TRANSLATION_SERVICE.value: "google",
        ConfigKey.API_KEYS.value: {"google": ""},
        ConfigKey.SOURCE_LANGUAGE.value: "ENGLISH",
        ConfigKey.TARGET_LANGUAGES.value: ["AUTO"],
        ConfigKey.METADATA_FOLDER.value: "./fastlane/metadata",
        ConfigKey.FIELDS_TO_TRANSLATE.value: ["name", "description"],
        ConfigKey.CACHE.value: {
            ConfigKey.CACHE_FOLDER.value: ".fastlingo-cache",
            ConfigKey.CACHE_ENABLED.value: True,
        },
    }

    def __init__(self, config_file_path: str) -> None:
        """Initialize the config.

        Args:
            config_file_path (str): The path to the config file.

        Returns:
            None
        """

        self._config_file_path = config_file_path
        self._config = None
        self._logger = Logger(name="Config").get_logger()

        self._load()

    def _load(self) -> None:
        """Load the config.

        Returns:
            None
        """

        if not os.path.exists(self._config_file_path):
            raise FastLingoException(
                f"Configuration file '{self._config_file_path}' not found."
            )

        with open(self._config_file_path) as file:
            self._config = toml.load(file)

    def get(self, key: ConfigKey, default: str = None) -> str:
        """Get a config value.

        Args:
            key     (ConfigKey): The config key.
            default (str)      : The default value.

        Returns:
            str: The config value.
        """

        if key.value in self._config:
            return self._config[key.value]

        return default

    def _print_config(self) -> None:
        """Print the config in detail.

        Returns:
            None
        """

        self._logger.info("Configuration:")
        for key, value in self._config.items():
            self._logger.info(f"{key}: {value}")

    @staticmethod
    def create_initial_config_file(config_file_path: str = CONFIG_FILE_NAME) -> None:
        """Create the initial config file.

        Args:
            config_file_path (str): The path to the config file.

        Returns:
            None
        """

        if os.path.exists(config_file_path):
            raise FastLingoException(
                f"Config file '{config_file_path}' already exists in {config_file_path}."
            )

        with open(config_file_path, "w") as file:
            toml.dump(Config.DEFAULT_CONFIG, file)
