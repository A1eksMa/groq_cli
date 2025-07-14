
import click
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
import os

@click.command()
def run():
    """Запускает интерактивную сессию (REPL) для общения с моделью."""
    from cli.cli import main as cli_group
    
    # Создаем сессию с историей. История будет сохраняться в файле.
    history_file = os.path.expanduser('~/.chat_cli_history')
    session = PromptSession(history=FileHistory(history_file))
    
    click.echo("Интерактивная сессия запущена. Введите 'exit' или 'quit' для выхода.")
    
    # Получаем текущий контекст Click
    ctx = click.get_current_context()

    while True:
        try:
            # Показываем промпт и ждем ввода пользователя
            user_input = session.prompt('chat> ')
            
            if not user_input.strip():
                continue

            # Команды для выхода из REPL
            if user_input.lower() in ['exit', 'quit']:
                break

            # Разбиваем ввод на имя команды и аргументы
            parts = user_input.split()
            command_name = parts[0]
            args = parts[1:]

            # Ищем команду в нашей группе Click
            command = cli_group.get_command(ctx, command_name)

            if command:
                try:
                    # Вызываем команду программно с нужными аргументами
                    # Мы передаем управление Click, который сам разберет аргументы
                    ctx.invoke(command, *args)
                except click.exceptions.UsageError as e:
                    # Обрабатываем ошибки, если пользователь ввел неверные аргументы
                    click.echo(f"Ошибка: {e}", err=True)
                except Exception as e:
                    # Обработка других возможных ошибок выполнения команды
                    click.echo(f"Произошла ошибка при выполнении команды '{command_name}': {e}", err=True)
            else:
                click.echo(f"Команда '{command_name}' не найдена.", err=True)

        except (EOFError, KeyboardInterrupt):
            # Обработка Ctrl+D (EOFError) или Ctrl+C (KeyboardInterrupt) для выхода
            break
    
    click.echo("Выход из интерактивной сессии.")

