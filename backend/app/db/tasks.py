# файл соеденяется с бд и создает дополнительную конфигурациюкоторую мы задали
from fastapi import FastAPI
from databases import Database
from app.core.config import DATABASE_URL
import logging

# создаем переменную для записи в логов
logger = logging.getLogger(__name__)

# None  тип возвращаемых данных, в даннос лучае функция ничего не возвращает она подключается
# подлючается по юрл определенном в core/config.py

async def connect_to_db(app: FastAPI) -> None:
    """ Функция подключения к бд"""
    # задаем максимальный и минимальное количество конектов
    database = Database(DATABASE_URL, min_size=2, max_size=10)

    try:
        #  попробуй: подключится кбазе данных, жди пока не подключится
        await database.connect()
        app.state._db = database
    except Exception as e:
        # не получилось выдай меседж попробуй снова
        # регистрирует сообщения предупреждения
        logger.warn("--- DB CONNECTION ERROR ---")
        logger.warn(e)
        logger.warn("--- DB CONNECTION ERROR ---")

async def close_db_connection(app: FastAPI) -> None:
    try:
        await app.state._db.discinnect()
    except Exception as e:      
        logger.warn("--- DB DISCONNECT ERROR ---")
        logger.warn(e)
        logger.warn("--- DB DISCONNECT ERROR ---")
