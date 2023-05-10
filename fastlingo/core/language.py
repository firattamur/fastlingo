from typing import Dict

from fastlingo.translate_services import TranslateService


class Language:
    """Language class for language objects"""

    def __init__(
        self, name: str, folder: str, codes: Dict[TranslateService, str]
    ) -> None:
        """Initialize a language object.

        Args:
            name   (str): The name of the language.
            folder (str): The folder of the language. This is the folder name of the language in the Fastlane project.
            codes (dict): The codes of the language. The keys are the translation services and the values are the codes of the language for the translation service.

        Returns:
            None
        """

        self._name = name
        self._folder = folder
        self._codes = codes

    @property
    def name(self) -> str:
        """Get the name of the language.

        Returns:
            str: The name of the language.
        """

        return self._name

    @property
    def folder(self) -> str:
        """Get the folder of the language.

        Returns:
            str: The folder of the language.
        """

        return self._folder

    @property
    def codes(self) -> dict:
        """Get the codes of the language.

        Returns:
            dict: The codes of the language.
        """

        return self._codes

    def code(self, translate_service: TranslateService) -> str:
        """Get the code of the language for a translation service.

        Args:
            translate_service (TranslateService): The translation service.

        Returns:
            str: The code of the language for the translation service.
        """

        return self._codes[translate_service]

    def __str__(self) -> str:
        """Get the string representation of the language.

        Returns:
            str: The string representation of the language.
        """

        return (
            f"Language(name={self._name}, folder={self._folder}, codes={self._codes})"
        )
