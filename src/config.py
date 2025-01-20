import os
from dotenv import load_dotenv

# Загружаем переменные окружения из .env файла
load_dotenv()

# Токены и настройки
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
WB_API_TOKEN = os.getenv("WB_API_TOKEN")
WB_API_URL = "https://supplies-api.wildberries.ru/api/v1/warehouses"
DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'warehouses.db')
