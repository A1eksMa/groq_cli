# Chat CLI Help

This is a command-line interface to interact with large language models.

## Usage

```bash
chat <command> [arguments]
```

### `run`

Starts an interactive session (REPL) to communicate with the model.

**Usage:**

```bash
chat run
```

**Description:**

This command launches a REPL (Read-Eval-Print Loop) environment, allowing you to execute other `chat` commands without having to type `chat` each time. It's a convenient way to manage a conversation continuously.

*   **Interactive Prompt**: You will see a `chat>` prompt where you can type commands.
*   **Command Execution**: Any command available in the CLI (like `add`, `log`, `switch`, `edit`) can be run directly. For example, just type `add` and press Enter.
*   **History**: The session keeps a history of your commands, which you can navigate with the up and down arrow keys. The history is saved to `~/.chat_cli_history`.
*   **Exiting**: To exit the interactive session, type `exit` or `quit`, or press `Ctrl+D`.

**Options:**

*   `--path <project_path>` (optional): Sets the project's working directory. Defaults to the current directory.
*   `--dry-run` (optional): The interactive session will be executed in-memory.

### `config`

Displays the current configuration settings.

**Usage:**

```bash
chat config
```

## Commands

### `new`

Creates a new chat session.

**Usage:**

```bash
chat new <project_name>
```

**Description:**

This command creates the specified `<project_name>.db` (or `chat.db` if not specified) for a new chat session.

**Arguments:**

*   `<project_name>` (optional): The name for the new project.

### `add`

Adds a user prompt to the chat, gets a response from the model, and stores the conversation in the database.

**Usage:**

```bash
chat add
```

**Description:**

This command initiates a sequence of events to continue the conversation:

1.  **User Input**: The user is prompted to enter their message.
2.  **Save Prompt**: The message is saved as a new entry in `chat.db` with a unique `id`, the `original` text, and the `parent_id`.
3.  **Translate Prompt**: The message is translated into English, and the `english` field is updated.
4.  **Get Original Response**: The full conversation history (in the original language) is sent to the model.
5.  **Save Original Response**: The model's response is saved as a new record, linked to the user's prompt via the `parent_id` field.
6.  **Get English Response**: The English conversation history is sent to the model, and the English response is saved in the `english` field of the new record.
7.  **Update State**: The response record becomes the new "current" message.

**Error Handling:**

*   The application will exit with an error (e.g., "Database write error") if it fails to write to the database.
*   The application will exit if it fails to receive a response from the model during translation or response generation.

**Database Visualization:**

```
   User's Prompt Record             Model's Response Record
   ┌──────────────────────────┐       ┌───────────────────────────┐
   │ id: 10                   │       │ id: 11                    │
   │ original: "Как дела?"    │       │ original: "У меня все..." │
   │ english: "How are you?"  │       │ english: "I'm doing..."   │
   │ parent_id: 9             │       │ parent_id: 10             │
   └──────────────────────────┘       └───────────────────────────┘
```

**Database Columns:**

*   `id`: Unique identifier.
*   `role`: System, user or model.
*   `original`: The text in its original language.
*   `english`: The English translation of the text.
*   `parent_id`: The `id` of the preceding record.
*   `config`: options of model configuration.

### `switch`

Changes the current message (HEAD) to a different message in the chat history.

**Usage:**

```bash
chat switch <id>
```

**Description:**

This command allows you to change the current context of the conversation to any message in the history by specifying its ID. Subsequent commands, like `chat add`, will consider the new message as their parent, effectively allowing you to branch the conversation from an earlier point.

**Arguments:**

*   `<id>` (required): The ID of the message to set as the new current message (HEAD).

### `log`

Displays the nodes of the chat tree.

**Usage:** `log [<number>] [--show-text <mode>] [--lang <language>]`

**Arguments:**
*   `<number>`: (Optional) If specified, it shows a number of nodes from the current branch of the dialog that does not exceed the specified number. By default, it shows the entire dialog tree.

**Options:**
*   `--graph`: (Optional) Displays the chat tree as a graph.
*   `--show-text <mode>`: (Optional) Determines if and how message text is displayed. If this option is omitted, no text is shown.
    *   `all`: Show message text for each node.
    *   `leaves`: Show message text only for the last nodes in a branch.
*   `--lang <language>`: (Optional) Sets the language for displaying messages. This option is only effective when `--show-text` is used. Defaults to `both` if omitted.
    *   `origin`: Show messages only in the native language.
    *   `english`: Show messages only in English.
    *   `both`: Show message text in both languages for each node (default).

### `edit`

Edits the text of a specified message, with automatic translation to maintain consistency between the original and English versions.

**Usage:**

```bash
chat edit [<id>] [--original] [--english]
```

**Description:**

This command opens the text of a message in a terminal editor. If no `id` is provided, it targets the current message (HEAD).

To maintain consistency, the command automatically synchronizes the `original` and `english` text fields. Editing one field triggers an automatic translation to update the other.

*   **Editing original text (default)**: The edited text is saved, and then automatically translated to update the `english` field.
*   **Editing English text (`--english`)**: The edited text is saved, and then automatically translated back to the original language to update the `original` field.

**Example Workflow for `chat edit 10 --english`:**

1.  The `english` text from the message with `id` 10 is retrieved.
2.  The text is opened in a terminal editor for you to modify.
3.  The edited text is sent to a translation service to be translated into the original language.
4.  The edited text is saved in the `english` field.
5.  The translated text is saved in the `original` field.

**Arguments:**

*   `<id>` (optional): The ID of the message to edit. If omitted, the current message is used.

**Options:**

*   `--original`: Explicitly specifies that the `original` text field should be edited. This is the default behavior.
*   `--english`: Specifies that the `english` text field should be edited.

**Error Handling:**

*   The application will exit with a "Database access error" if it fails to write to the database.
*   The application will exit with a "Service not responding" error if it fails to get a response from the translation service.
