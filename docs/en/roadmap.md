### Development Roadmap: Chat-CLI

**Stage 1: Core Chat Functionality (MVP)**

The goal of this stage is to get a basic, interactive chat running with a single, hard-coded provider. This will form the foundation of the application.

1.  **Implement `new` command**:
    *   Implement the logic in `cli/commands/new.py` to create a new project directory.
    *   Add functionality to create a default `config.json` and an empty `chat.db` database file.
2.  **Implement `run` command**:
    *   Flesh out `cli/commands/run.py` to launch an interactive session.
    *   Integrate the `prompt-toolkit` library for a smooth command-line interface (it's already in `requirements.txt`).
3.  **Basic API Integration**:
    *   Implement the `BaseProvider` in `cli/api/base_provider.py`.
    *   Integrate the `DummyProvider` from `cli/api/dummy_provider.py` to simulate API responses.
4.  **Interactive Loop**:
    *   Create the main chat loop that takes user input, sends it to the provider, and prints the response.

**Stage 2: Conversation & History Management**

This stage introduces persistence, allowing users to save, load, and manage their conversations.

1.  **Database Models**:
    *   Define the SQLAlchemy models in `cli/database/models.py` for `Conversation`, `Message`, and `ConfigurationSettings`.
2.  **Database Integration**:
    *   Use the `Alembic` setup to manage database migrations.
    *   Integrate database sessions (`cli/database/session.py`) into the chat loop to save all messages.
3.  **Context Management**:
    *   Implement logic to automatically build the context (conversation history) to be sent with each new prompt.
    *   Add commands to allow the user to view, enable/disable, or delete previous messages from the context.
4.  **Save/Load Conversations**:
    *   Create commands like `chat save <name>` and `chat load <name>` to manage different conversation threads.

**Stage 3: Advanced Prompt Engineering**

This stage adds the specialized features for prompt engineering mentioned in the `README.md`.

1.  **Prompt Editing**:
    *   Implement a command that allows the user to open a previous prompt in their default text editor (`$EDITOR`), save the changes, and regenerate the conversation from that point.
2.  **Dialogue Visualization**:
    *   Create a `chat tree` command that displays the current conversation as a branching tree, which is especially useful for exploring different responses to the same prompt.
3.  **Context Enrichment**:
    *   Add a command (`chat add-context <file>`) to easily add the content of a file into the conversation history as context for the model.

**Stage 4: Multi-Provider Support & Configuration**

This stage focuses on building the pluggable API module and allowing the user to configure the application.

1.  **Real API Integration**:
    *   Create a concrete implementation for a first real provider (e.g., `GroqProvider`) that handles making API requests and getting responses.
2.  **API Key Management**:
    *   Implement a simple and secure way to load the API key from an environment variable.
3.  **Dynamic Provider Loading**:
    *   Refactor the API integration to dynamically load available provider modules from the `cli/api` directory.
4.  **Configuration System**:
    *   Create a configuration service (`cli/services/config.py`) that reads settings from a file (e.g., `~/.chat_cli/config.json`).
    *   Use `templates/default_config.json` to create a default configuration for new users.
    *   Allow users to select the default provider and model in the config file.
5.  **Model Selection Command**:
    *   Add a command (e.g., `chat model <provider>.<model>`) to let users switch the active language model for the current session.
6.  **Flexible NN Settings**:
    *   Allow users to specify model parameters (like `temperature`, `max_tokens`) both in the config file and as options in the `run` command.