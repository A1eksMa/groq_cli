import click

# This will be the main entry point for the CLI.
# We will add commands to this group from the `commands` directory.

@click.group()
def main():
    """
    An advanced toolkit for prompt engineering and code interaction with
    large language models.
    """
    pass

if __name__ == "__main__":
    main()
