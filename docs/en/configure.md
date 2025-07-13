# Configuration

Chat CLI uses a multi-layered configuration system to provide maximum flexibility. Settings are loaded from multiple sources, with each subsequent level overriding the previous one. This allows you to set global defaults, project-specific settings, and temporary overrides.

The order of precedence is as follows:
1.  Global User Configuration
2.  Project-Specific Configuration
3.  Environment Variables

---

### Level 1: Global User Configuration

This file is for storing your personal default settings that you want to apply to all your projects.

*   **Path:** `~/.chat_cli/chat.cfg`
*   **Purpose:** To set global preferences like your default language, preferred model, or editor. The application looks for this file on startup.

**Example `~/.chat_cli/chat.cfg`:**
```json
{
  "user_name": "Alex",
  "default_language": "english",
  "default_model": "groq/llama3-70b",
  "editor": "vim"
}
```

---

### Level 2: Project-Specific Configuration

This level of configuration is loaded from a project-specific database file, typically named `<project_name>.db` (with `chat.db` as the default name). This database is created and managed by the `chat new` command.

*   **Path:** `<project_folder>/<project_name>.db` (default: `chat.db`)
*   **Purpose:** To store settings unique to a particular project, such as the programming language, specific model, or other project-specific data.
*   **Discovery:** When you run a command like `chat add` or `chat run`, the CLI automatically searches for the project database in the current directory and then moves up the directory tree until it finds one. This allows you to run commands from any subdirectory within your project.

**Example (Conceptual) of Project-Specific Configuration Data:**
(Note: This data is stored in a database, not directly in a human-readable file like JSON)
```
{
  "project_path": "/home/user/projects/my_python_project",
  "language": "english",
  "code_language": "python",
  "model": "anthropic/claude-3-opus"
}
```
In this example, the `model` setting would override the `default_model` from the global config.

---

### Level 3: Environment Variables

Environment variables are the highest-priority configuration source, ideal for sensitive data like API keys or for temporary overrides.

*   **Purpose:** To securely provide API keys without hardcoding them into files and to temporarily change a setting without editing any configuration files.
*   **Precedence:** Values set via environment variables will always override settings from any configuration file.

**Example:**
```bash
# Set API keys (best practice)
export GROQ_API_KEY="gsk_..."
export ANTHROPIC_API_KEY="sk-ant-..."

# Temporarily override the editor for the current session
export EDITOR="code"
```

This layered approach provides a powerful and flexible way to manage your settings across different contexts.
