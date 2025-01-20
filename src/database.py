import os
import sqlite3
from typing import List, Tuple, Optional

# Создаём папку для базы данных, если она не существует
DB_FOLDER = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
if not os.path.exists(DB_FOLDER):  # Проверяем существование папки
    os.makedirs(DB_FOLDER)  # Создаём папку, если её нет

# Путь к базе данных
DB_PATH = os.path.join(DB_FOLDER, 'warehouses.db')

def init_db():
    """Инициализация базы данных: создание таблицы, если её нет."""
    conn = sqlite3.connect(DB_PATH)  # Подключаемся к базе данных
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS warehouses (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            address TEXT NOT NULL,
            work_time TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def save_warehouses_to_db(warehouses: List[dict]) -> None:
    """Сохраняем список складов в базу данных SQLite."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    for wh in warehouses:
        cursor.execute("""
            INSERT OR REPLACE INTO warehouses (id, name, address, work_time)
            VALUES (?, ?, ?, ?)
        """, (wh["ID"], wh["name"], wh["address"], wh["workTime"]))
    conn.commit()
    conn.close()

def get_warehouses_from_db(limit: int = 5) -> List[Tuple]:
    """Получить список складов из базы данных с ограничением по количеству."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(f"SELECT id, name, address, work_time FROM warehouses LIMIT {limit}")
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_warehouse_by_name(name: str) -> Optional[Tuple]:
    """Получить склад из базы данных по названию."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, name, address, work_time 
        FROM warehouses 
        WHERE LOWER(name) LIKE LOWER(?)
    """, (f"%{name}%",))
    result = cursor.fetchone()
    conn.close()
    return result
