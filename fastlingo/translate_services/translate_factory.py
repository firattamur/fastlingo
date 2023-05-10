from .translate_google import TranslateGoogle
from .translate_service import TranslateService


class TranslateFactory:
    """Class for the translation factory."""

    def __init__(self) -> None:
        """Initialize the translation factory.

        Returns:
            None
        """

        self._translate_services = {
            TranslateService.GOOGLE.value: TranslateGoogle,
        }

    def create(self, translate_service: TranslateService, api_key: str):
        """Create a translation service.

        Args:
            translate_service (TranslateService): The translation service.
            api_key                 (str): The API key.

        Returns:
            Translate: The translation service.
        """

        return self._translate_services[translate_service](api_key)
