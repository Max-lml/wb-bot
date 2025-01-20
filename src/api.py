import requests
from typing import Tuple
from src.config import WB_API_TOKEN, WB_API_URL
from src.database import save_warehouses_to_db

def fetch_and_save_warehouses() -> str:
    """Запрашиваем данные с Wildberries API и сохраняем их в базу."""
    headers = {"Authorization": f"Bearer {WB_API_TOKEN}"}
    try:
        response = requests.get(WB_API_URL, headers=headers)
        if response.status_code == 200:
            warehouses = response.json()
            save_warehouses_to_db(warehouses)
            return "Данные о складах успешно обновлены!"
        else:
            return f"Ошибка при запросе: {response.status_code} {response.text}"
    except Exception as e:
        return f"Произошла ошибка при запросе: {str(e)}"
