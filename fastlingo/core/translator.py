from fastlingo.core.config import Config, ConfigKey
from fastlingo.core.field import Field
from fastlingo.core.fileio import FileIO
from fastlingo.core.language import Language
from fastlingo.core.language_utils import LanguageUtils
from fastlingo.core.logger import Logger
from fastlingo.core.translations_cache import TranslationsCache
from fastlingo.translate_services import TranslateFactory


class Translator:
    """Translator class for translation operations"""

    def __init__(self, config: Config) -> None:
        """Initialize the translator.

        Args:
            config (Config): The config.

        Returns:
            None
        """

        self._config = config
        self._translate_service = config.get(ConfigKey.TRANSLATION_SERVICE)

        self.logger = Logger(name="Translator").get_logger()

        self._translator = TranslateFactory().create(
            self._translate_service,
            config.get(ConfigKey.API_KEYS).get(self._translate_service),
        )
        self._cache = TranslationsCache(
            config.get(ConfigKey.CACHE)["cache_folder"],
        )

    def start(self) -> None:
        """Start the translator.

        Returns:
            None
        """

        languages_to_translate = LanguageUtils.get_languages_to_translate(
            self._config.get(ConfigKey.TARGET_LANGUAGES),
            self._config.get(ConfigKey.METADATA_FOLDER),
        )
        source_language = LanguageUtils.get_language_by_name(
            self._config.get(ConfigKey.SOURCE_LANGUAGE)
        )
        fields_to_translate = Field.get_fields_to_translate(
            self._config.get(ConfigKey.FIELDS_TO_TRANSLATE)
        )

        metadata_folder = self._config.get(ConfigKey.METADATA_FOLDER)

        for target_language in languages_to_translate:
            for field in fields_to_translate:
                source_field_path = FileIO.get_field_file_path(
                    metadata_folder, source_language.folder, field.value
                )

                target_field_path = FileIO.get_field_file_path(
                    metadata_folder, target_language.folder, field.value
                )

                content = FileIO.read(source_field_path)

                translation = self._get_translation(
                    content, source_language, target_language
                )

                FileIO.write(target_field_path, translation)

            self.logger.info(
                f"Translated {source_language.name} to {target_language.name}"
            )

    def _get_translation(
        self, content: str, source_language: Language, target_language: Language
    ) -> str:
        """Get the translation.

        Args:
            content         (str): The content to translate.
            source_language (Language): The source language.
            target_language (Language): The target language.

        Returns:
            str: The translation.
        """

        if self._config.get(ConfigKey.CACHE)["cache_enabled"]:
            translation = self._cache.get(
                source_language.code(self._translate_service),
                target_language.code(self._translate_service),
                content,
            )

            if translation is None:
                translation = self._translate(
                    content,
                    source_language.code(self._translate_service),
                    target_language.code(self._translate_service),
                )
                self._cache.set(
                    source_language.code(self._translate_service),
                    target_language.code(self._translate_service),
                    content,
                    translation,
                )
        else:
            translation = self._translate(
                content,
                source_language.code(self._translate_service),
                target_language.code(self._translate_service),
            )

        return translation

    def _translate(
        self, content: str, source_language: str, target_language: str
    ) -> str:
        """Translate a content.

        Args:
            content         (str): The content to translate.
            source_language (str): The source language.
            target_language (str): The target language.

        Returns:
            str: The translation.
        """

        if source_language == target_language:
            return content

        return self._translator.translate(content, source_language, target_language)
