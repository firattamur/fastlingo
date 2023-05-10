import os

from fastlingo.core.exceptions import FastLingoException
from google.cloud import translate_v2 as translate

from .translate import Translate


class TranslateGoogle(Translate):
    """Class for Google Translate."""

    def __init__(self, api_key: str) -> None:
        """Initialize the translation service.

        Args:
            api_key (str): The API key.

        Returns:
            None
        """

        super().__init__(api_key)
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = api_key

        self._client = translate.Client()

    def translate(self, text: str, source_language: str, target_language: str) -> str:
        """Translate a text.

        Args:
            text            (str): The text to translate.
            source_language (str): The source language.
            target_language (str): The target language.

        Returns:
            str: The translated text.
        """

        try:
            response = self._client.translate(
                values=[text],
                target_language=target_language,
                format_="text",
                source_language=source_language,
            )

            translated_text = response[0]["translatedText"]

            return translated_text

        except Exception as e:
            raise FastLingoException(f"Google Translate error: {e}")

    def supported_languages(self) -> list:
        """Get the supported languages.

        Returns:
            list: The supported languages.
        """

        return self._client.get_languages()
