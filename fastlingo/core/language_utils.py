import os

from fastlingo.core.exceptions import FastLingoException
from fastlingo.core.language import Language


class LanguageUtils:
    @staticmethod
    def get_supported_languages() -> list:
        """Get the supported languages.

        Returns:
            list: The supported languages.
        """

        return [
            Language(name="Arabic", folder="ar-SA", codes={"google": "ar"}),
            Language(name="Catalan", folder="ca", codes={"google": "ca"}),
            Language(
                name="Chinese (Simplified)", folder="zh-Hans", codes={"google": "zh-CN"}
            ),
            Language(
                name="Chinese (Traditional)",
                folder="zh-Hant",
                codes={"google": "zh-TW"},
            ),
            Language(name="Croatian", folder="hr", codes={"google": "hr"}),
            Language(name="Czech", folder="cs", codes={"google": "cs"}),
            Language(name="Danish", folder="da", codes={"google": "da"}),
            Language(name="Dutch", folder="nl-NL", codes={"google": "nl"}),
            Language(
                name="English (Australia)", folder="en-AU", codes={"google": "en"}
            ),
            Language(name="English (Canada)", folder="en-CA", codes={"google": "en"}),
            Language(
                name="English (United Kingdom)", folder="en-GB", codes={"google": "en"}
            ),
            Language(name="English", folder="en-US", codes={"google": "en"}),
            Language(name="Finnish", folder="fi", codes={"google": "fi"}),
            Language(name="French (Canada)", folder="fr-CA", codes={"google": "fr"}),
            Language(name="French (France)", folder="fr-FR", codes={"google": "fr"}),
            Language(name="German", folder="de-DE", codes={"google": "de"}),
            Language(name="Greek", folder="el", codes={"google": "el"}),
            Language(name="Hebrew", folder="he", codes={"google": "iw"}),
            Language(name="Hindi", folder="hi", codes={"google": "hi"}),
            Language(name="Hungarian", folder="hu", codes={"google": "hu"}),
            Language(name="Indonesian", folder="id", codes={"google": "id"}),
            Language(name="Italian", folder="it", codes={"google": "it"}),
            Language(name="Japanese", folder="ja", codes={"google": "ja"}),
            Language(name="Korean", folder="ko", codes={"google": "ko"}),
            Language(name="Malay", folder="ms", codes={"google": "ms"}),
            Language(name="Norwegian", folder="no", codes={"google": "no"}),
            Language(name="Polish", folder="pl", codes={"google": "pl"}),
            Language(
                name="Portuguese (Brazil)", folder="pt-BR", codes={"google": "pt"}
            ),
            Language(
                name="Portuguese (Portugal)", folder="pt-PT", codes={"google": "pt"}
            ),
            Language(name="Romanian", folder="ro", codes={"google": "ro"}),
            Language(name="Russian", folder="ru", codes={"google": "ru"}),
            Language(name="Slovak", folder="sk", codes={"google": "sk"}),
            Language(name="Spanish (Mexico)", folder="es-MX", codes={"google": "es"}),
            Language(name="Spanish (Spain)", folder="es-ES", codes={"google": "es"}),
            Language(name="Swedish", folder="sv", codes={"google": "sv"}),
            Language(name="Thai", folder="th", codes={"google": "th"}),
            Language(name="Turkish", folder="tr", codes={"google": "tr"}),
            Language(name="Ukrainian", folder="uk", codes={"google": "uk"}),
            Language(name="Vietnamese", folder="vi", codes={"google": "vi"}),
        ]

    @staticmethod
    def get_language_by_name(name: str) -> Language:
        """Get the language by the name.

        Args:
            name (str): The name.

        Returns:
            Language: The language.
        """
        for language in LanguageUtils.get_supported_languages():
            if language.name.lower() == name.lower():
                return language

        raise FastLingoException(f"Language with name '{name}' not found.")

    @staticmethod
    def get_language_by_fastlane_folder(folder: str) -> Language:
        """Get the language by the fastlane folder.

        Args:
            folder (str): The fastlane folder.

        Returns:
            Language: The language.
        """
        for language in LanguageUtils.get_supported_languages():
            if language.folder == folder:
                return language

        raise FastLingoException(f"Language with folder '{folder}' not found.")

    @staticmethod
    def get_languages_to_translate(
        config_languages: list, metadata_folder: str
    ) -> list:
        """Get the languages to translate.

        Args:
            config_languages (list): The languages from the config file.
            metadata_folder   (str): The path to the metadata folder.

        Returns:
            list: The languages to translate.
        """
        if not config_languages or config_languages[0] == "AUTO":
            return LanguageUtils.auto_detect_languages_in_metadata_folder(
                metadata_folder
            )

        languages = [
            lang
            for lang in LanguageUtils.get_supported_languages()
            if lang.folder in config_languages
        ]
        return languages

    @staticmethod
    def auto_detect_languages_in_metadata_folder(metadata_folder: str) -> list:
        """Auto detect the languages in the metadata folder.

        Returns:
            list: The languages in the metadata folder.
        """

        if not os.path.exists(metadata_folder):
            raise FastLingoException(f"Metadata folder '{metadata_folder}' not found.")

        languages = []

        for folder in os.listdir(metadata_folder):
            if not os.path.isdir(os.path.join(metadata_folder, folder)):
                continue

            try:
                language = LanguageUtils.get_language_by_fastlane_folder(folder)
                languages.append(language)
            except Exception:
                continue

        return languages
