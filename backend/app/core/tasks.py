# файл соеденяется с бд и создает дополнительную конфигурациюкоторую мы задали
from typing import Callable
from fastapi import FastAPI

from app.db.tasks import connect_to_db, close_db_connection


# эти фукциии могу происходить в фотоновом режиме асинхронноб, не дожидаясь процессов из другой части кода
def create_start_app_handler(app: FastAPI) -> Callable:
    # создаем подфункию который возвращает обьект в карантине
    async def start_app() -> None:
        # ждем пока произо  дет контакт с базой данных
        await connect_to_db(app)
    # как только конект произошел вернуть запуск программы
    return start_app

# создаем останавливующий приложение обрабочик
# Callable - вызываемый функция проверяет если обьект можно выpвать(он класс или функция) и возвращет True
def create_stop_app_handler(app: FastAPI) -> Callable:
    async def stop_app() -> None:
        await close_db_connection(app)

    return stop_app
