# Database

## Database Selection

By default, the application uses **SQLite** as its database. This is a simple and lightweight database that is stored as a single file. It is well-suited for single-user operation, making it an ideal choice for this application.

In the future, there are plans to add support for more robust databases, such as **PostgreSQL** or others.

## ORM

To interact with the database, the application uses the **SQLAlchemy** Object-Relational Mapper (ORM). This allows for a high-level, object-oriented approach to database operations and makes it easier to support different database systems in the future.

## Database Content

The database stores two main types of information:
1.  The current application configuration.
2.  The user's chat history, including prompts and the corresponding responses from the language model.

### Table Structure

The main table for storing chat history is named `chat`. It has the following structure:

| Column     | Type      | Description                                           |
|------------|-----------|-------------------------------------------------------|
| `id`       | Integer   | The unique identifier for the message.                |
| `role`     | String    | The role of the message author (e.g., `user`, `model`). |
| `original` | String    | The message text in its original language.            |
| `english`  | String    | The English translation of the message text.          |
| `parent_id`| Integer   | The `id` of the preceding message in the conversation.|
| `config`   | JSON      | The model configuration options for this message.     |

The `parent` and `children` relationships are managed via SQLAlchemy's relationship feature, linking messages in a conversational tree.

## Migrations

The application is under active development, and the database structure may change. To manage these changes, we use **Alembic** for database migrations.

## Configuration

By default, the database file is named `chat.db` and is located in the current working directory. You can change the name and location of this file in the application's configuration file.
