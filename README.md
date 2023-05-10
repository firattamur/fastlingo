<div align="center">
  <img src=".github/assets/logo.png" height="128">

[![PyPI version](https://badge.fury.io/py/fastlingo.svg)](https://badge.fury.io/py/fastlingo)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)

</div>

FastLingo is a command-line tool designed to translate iOS app metadata using a variety of translation sources. It is built on top of [Fastlane](https://fastlane.tools) and [Deliver](https://docs.fastlane.tools/actions/deliver/). FastLingo is currently supports the following translation sources:

- [Google Cloud Translation API](https://cloud.google.com/translate)

Full documentation can be found [here](https://fastlingo.readthedocs.io/en/latest/).

### Features

- Multilingual app metadata translation.
- Configurable translation sources.
- Translation caching for enhanced performance and fewer API calls.
- Seamless integration with Fastlane metadata folder structure.

### Installation

To install FastLingo, execute the following command:

```bash
pip install fastlingo
```

### Configuration

Before using FastLingo, configure your preferred translation source by establishing API keys and endpoints. Generate a template configuration file by executing:

```bash
fastlingo init
```

This action creates a `FastLingo.toml` file in the current directory, which can then be edited to include your API keys and endpoints. For example, to configure the Google Cloud Translation API, add the following to your configuration file:

```toml
translation_service = "google"
source_language = "ENGLISH"
target_languages = [ "AUTO",]
metadata_folder = "your/metadata/folder"
fields_to_translate = [ "name", "description" ]

[api_keys]
google = "service/account/key.json"

[cache]
cache_folder = ".fastlingo-cache"
cache_enabled = true
```

### How to Use

To translate your app metadata, run:

```bash
fastlingo translate
```

This will translate all the metadata fields specified in your configuration file for each target language.

### Contributing

Pull requests are welcome. Additions to the translation source list are encouraged.

### License

FastLingo is available under the MIT license.
