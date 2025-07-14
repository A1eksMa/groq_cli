import click
import json
from cli.config import config

@click.command()
def config_command():
    """Displays the current configuration settings."""
    config_dict = {key: value for key, value in config.__dict__.items() if not key.startswith('_')}
    click.echo(json.dumps(config_dict, indent=4))

# Rename the command to 'config' for the CLI
config_command.name = 'config'
