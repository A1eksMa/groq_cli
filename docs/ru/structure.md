# Project Structure

This structure is aimed at modularity, extensibility, and ease of maintenance.

## Project Layout

```
/groq_cli/
├── alembic/                      # Folder for Alembic database migrations
│   ├── versions/                 # Migration files
│   └── env.py                    # Alembic configuration file
├── docs/                         # Documentation
│   ├── help.md
│   ├── help.ru.md
│   └── structure.md              # This file
├── cli/                          # Main package with the application's source code
│   ├── __init__.py
│   ├── api/                      # Modules for interacting with APIs of different providers
│   │   ├── __init__.py
│   │   ├── base_provider.py      # Base (abstract) class for all providers
│   │   ├── dummy_provider.py     # Dummy provider for testing
│   │   └── groq_provider.py      # Example implementation for the Groq API
│   ├── commands/                 # Modules with the implementation of Click commands
│   │   ├── __init__.py
│   │   ├── add.py
│   │   ├── edit.py
│   │   ├── log.py
│   │   ├── new.py
│   │   └── switch.py
│   ├── database/                 # Everything related to the database
│   │   ├── __init__.py
│   │   ├── crud.py               # Functions for DB operations (Create, Read, Update, Delete)
│   │   ├── models.py             # SQLAlchemy table models
│   │   └── session.py            # SQLAlchemy session and engine setup
│   ├── services/                 # Business logic not tied to commands
│   │   ├── __init__.py
│   │   ├── chat_manager.py       # Dialogue management logic (creation, branching)
│   │   ├── config_manager.py     # Configuration management (reading, writing)
│   │   └── translation.py        # Translation service (including a stub)
│   ├── cli.py                    # The main Click file that gathers all commands
│   └── utils.py                  # Helper utilities (e.g., working with an editor)
├── templates/                    # Configuration templates
│   └── default_config.json       # Default config template for new projects
├── tests/                        # Folder with tests
│   ├── commands/
│   └── services/
├── .gitignore
├── alembic.ini                   # Alembic configuration
├── config.json                   # Global application configuration file
├── LICENSE
├── pyproject.toml                # Project definition, dependencies, and entry points
├── README.md
└── requirements.txt              # List of dependencies
```

## Explanation of Key Directories and Files

1.  **`pyproject.toml`**: This is the modern standard for project management. Here you define dependencies (`click`, `sqlalchemy`, `alembic`, etc.), and most importantly, the **entry point** for your CLI. This allows the package to be installed and called by name (e.g., `chat`).
    ```toml
    [project.scripts]
    chat = "cli.cli:main"
    ```

2.  **`cli/cli.py`**: The central file for Click. It imports commands from the `cli/commands` folder and registers them. This makes the code cleaner than if all the logic were in a single file.
    ```python
    # cli/cli.py
    import click
    from .commands.new import new_command
    from .commands.add import add_command
    # ... and so on

    @click.group()
    def main():
        """An advanced toolkit for prompt engineering..."""
        pass

    main.add_command(new_command, name="new")
    main.add_command(add_command, name="add")
    # ...
    ```

3.  **`cli/commands/`**: Each command (`new`, `add`, etc.) is in its own file. This simplifies navigation and maintenance. Each file contains a single function decorated with `@click.command()`.

4.  **`cli/database/`**:
    *   `models.py`: Here you will define the `Message` class (or whatever you name it) using the SQLAlchemy ORM, describing the columns `id`, `role`, `original`, `english`, `parent_id`, etc.
    *   `crud.py`: Contains functions like `get_message(db_session, message_id)`, `create_message(...)`. This separates the DB logic from the business logic in the commands.

5.  **`cli/api/`**:
    *   `base_provider.py`: Defines an abstract class with a single method, for example, `get_response(prompt: str, config: dict) -> str`. All other providers must inherit from it. This ensures a uniform interface.
    *   `dummy_provider.py`: Your **stub function**.
        ```python
        # cli/api/dummy_provider.py
        from .base_provider import BaseProvider

        class DummyProvider(BaseProvider):
            def get_response(self, prompt: str, config: dict) -> str:
                return f"Echo: {prompt}"
        ```

6.  **`cli/services/`**:
    *   `config_manager.py`: Will be responsible for reading `config.json`, finding the required model and its settings, and copying the template from `templates/` when the `new` command is executed.
    *   `translation.py`: This will contain the translation logic, including a **stub function** that simply returns the original text.
    *   `chat_manager.py`: May contain the complex logic of the `add` command: get a message, save it to the DB, call the translation service, call the appropriate API provider, save the response. This will offload the `commands/add.py` file.

7.  **`alembic/` and `alembic.ini`**: A standard structure generated by the `alembic init` command. You will create new migrations (`alembic revision --autogenerate`) every time you change the models in `database/models.py`.
