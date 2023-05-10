import click
from fastlingo.core import Translator
from fastlingo.core.config import Config
from fastlingo.core.exceptions import FastLingoException


@click.group()
def cli():
    """FastLingo is a CLI tool to translate metadata files for mobile apps."""
    pass


@click.command()
@click.option(
    "--config",
    default="FastLingo.toml",
    help="Path to the FastLingo.toml configuration file.",
)
def init(config: str) -> None:
    """Create an initial FastLingo.toml configuration file.

    Args:
        config (str): The path to the config file.

    Returns:
        None
    """

    try:
        Config.create_initial_config_file(config)
        click.secho(f"Configuration file '{config}' created.", fg="green")

    except FastLingoException as e:
        click.secho(e, fg="red")


@click.command()
@click.option(
    "--config",
    default="FastLingo.toml",
    help="Path to the FastLingo configuration file.",
)
def translate(config):
    """Start the translation process using the FastLingo.toml.

    Args:
        config (str): The path to the config file.

    Returns:
        None
    """

    try:
        config_instance = Config(config_file_path=config)

        translator = Translator(config_instance)
        translator.start()

        click.secho("Translation process completed.", fg="green")

    except FastLingoException as e:
        click.secho(e, fg="red")


cli.add_command(init)
cli.add_command(translate)

if __name__ == "__main__":
    """Main entry point for the CLI."""
    cli()
