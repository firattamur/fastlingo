from abc import ABC, abstractmethod


class Translate(ABC):
    """Abstract class for translation services."""

    def __init__(self, api_key: str) -> None:
        """Initialize the translation service.

        Args:
            api_key (str): The API key.

        Returns:
            None
        """
        self._api_key = api_key

    @abstractmethod
    def translate(self, text: str, source_language: str, target_language: str) -> str:
        """Translate a text.

        Args:
            text            (str): The text to translate.
            source_language (str): The source language.
            target_language (str): The target language.

        Returns:
            str: The translated text.
        """
        pass

    @abstractmethod
    def supported_languages(self) -> list:
        """Get the supported languages.

        Returns:
            list: The supported languages.
        """
        pass
