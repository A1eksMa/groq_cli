# структура проекта

Эта структура нацелена на модульность, расширяемость и простоту поддержки.

## Структура проекта

```
/groq_cli/
├── alembic/                      # Папка для миграций базы данных Alembic
│   ├── versions/                 # Файлы миграций
│   └── env.py                    # Файл конфигурации Alembic
├── docs/                         # Документация
│   ├── help.md
│   ├── help.ru.md
│   └── structure.md              # Этот файл
├── cli/                          # Основной пакет с исходным кодом приложения
│   ├── __init__.py
│   ├── api/                      # Модули для взаимодействия с API разных поставщиков
│   │   ├── __init__.py
│   │   ├── base_provider.py      # Базовый (абстрактный) класс для всех провайдеров
│   │   ├── dummy_provider.py     # Провайдер-заглушка для тестирования
│   │   └── groq_provider.py      # Пример реализации для Groq API
│   ├── commands/                 # Модули с реализацией команд Click
│   │   ├── __init__.py
│   │   ├── add.py
│   │   ├── edit.py
│   │   ├── log.py
│   │   ├── new.py
│   │   └── switch.py
│   ├── database/                 # Все, что связано с базой данных
│   │   ├── __init__.py
│   │   ├── crud.py               # Функции для операций с БД (Create, Read, Update, Delete)
│   │   ├── models.py             # Модели табл��ц SQLAlchemy
│   │   └── session.py            # Настройка сессии и движка SQLAlchemy
│   ├── services/                 # Бизнес-логика, не привязанная к командам
│   │   ├── __init__.py
│   │   ├── chat_manager.py       # Логика управления диалогом (создание, ветвление)
│   │   ├── config_manager.py     # Управление конфигурацией (чтение, запись)
│   │   └── translation.py        # Сервис перевода (включая заглушку)
│   ├── cli.py                    # Главный файл Click, который собирает все команды
│   └── utils.py                  # Вспомогательные утилиты (например, работа с редактором)
├── templates/                    # Шаблоны конфигураций
│   └── default_config.json       # Шаблон конфига по умолчанию для новых проектов
├── tests/                        # Папка с тестами
│   ├── commands/
│   └── services/
├── .gitignore
├── alembic.ini                   # Конфигурация Alembic
├── config.json                   # Глобальный файл конфигурации приложения
├── LICENSE
├── pyproject.toml                # Определение проекта, зависимостей и entry points
├── README.md
└── requirements.txt              # Список зависимостей
```

## Пояснения по ключевым каталогам и файлам

1.  **`pyproject.toml`**: Это современный стандарт для управления проектом. Здесь вы определите зависимости (`click`, `sqlalchemy`, `alembic` и др.), а также, что самое важное, **точку входа** для вашего CLI. Это позволит установить пакет и вызывать его по имени (например, `chat`).
    ```toml
    [project.scripts]
    chat = "cli.cli:main"
    ```

2.  **`cli/cli.py`**: Центральный файл для Click. Он импортирует команды из папки `cli/commands` и регистрирует их. Это делает код чище, чем если бы вся логика была в одном файле.
    ```python
    # cli/cli.py
    import click
    from .commands.new import new_command
    from .commands.add import add_command
    # ... и так далее

    @click.group()
    def main():
        """An advanced toolkit for prompt engineering..."""
        pass

    main.add_command(new_command, name="new")
    main.add_command(add_command, name="add")
    # ...
    ```

3.  **`cli/commands/`**: Каждая команда (`new`, `add` и т.д.) вынесена в свой файл. Это упрощает навигацию и поддержку. Каждый файл содержит одну функцию, декорированную `@click.command()`.

4.  **`cli/database/`**:
    *   `models.py`: Здесь вы определите класс `Message` (или как вы его назовете) с помощью SQLAlchemy ORM, описывая колонк�� `id`, `role`, `original`, `english`, `parent_id` и т.д.
    *   `crud.py`: Содержит функции типа `get_message(db_session, message_id)`, `create_message(...)`. Это отделяет логику работы с БД от бизнес-логики в командах.

5.  **`cli/api/`**:
    *   `base_provider.py`: Определяет абстрактный класс с единым методом, например `get_response(prompt: str, config: dict) -> str`. Все остальные провайдеры должны его наследовать. Это гарантирует единый интерфейс.
    *   `dummy_provider.py`: Ваша **функция-заглушка**.
        ```python
        # cli/api/dummy_provider.py
        from .base_provider import BaseProvider

        class DummyProvider(BaseProvider):
            def get_response(self, prompt: str, config: dict) -> str:
                return f"Echo: {prompt}"
        ```

6.  **`cli/services/`**:
    *   `config_manager.py`: Будет отвечать за чтение `config.json`, поиск нужной модели и её н��строек, а также за копирование шаблона из `templates/` при выполнении команды `new`.
    *   `translation.py`: Здесь будет логика перевода, включая **функцию-заглушку**, которая просто возвращает исходный текст.
    *   `chat_manager.py`: Может содержать сложную логику команды `add`: получить сообщение, сохранить в БД, вызвать сервис перевода, вызвать нужный API-провайдер, сохранить ответ. Это разгрузит файл `commands/add.py`.

7.  **`alembic/` и `alembic.ini`**: Стандартная структура, генерируемая командой `alembic init`. Вы будете создавать новые миграции (`alembic revision --autogenerate`) каждый раз при изменении моделей в `database/models.py`.
