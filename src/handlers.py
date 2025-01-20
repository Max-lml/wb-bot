
from aiogram.types import Message
from src.database import get_warehouses_from_db, get_warehouse_by_name
from src.api import fetch_and_save_warehouses

async def start_command(message: Message):
    """Обработка команды /start."""
    text = (
        "Привет! Я бот, который может работать с базой складов Wildberries.\n"
        "Я уже загрузил данные о складах в базу для вас.\n\n"
        "Доступные команды:\n"
        "/update - обновить данные о складах из Wildberries\n"
        "/list - показать данные о 5 складах из базы\n"
        "Просто напишите название склада, чтобы найти его в базе."
    )
    update_status = fetch_and_save_warehouses()
    await message.answer(f"{text}\n\n{update_status}")

async def update_warehouses(message: Message):
    """Обновление базы данных из Wildberries API."""
    update_status = fetch_and_save_warehouses()
    await message.answer(update_status)

async def list_warehouses(message: Message):
    """Вывод первых 5 складов из базы данных."""
    warehouses = get_warehouses_from_db()
    if warehouses:
        text = "Список первых 5 складов из базы данных:\n\n"
        for wh in warehouses:
            text += (
                f"- ID: {wh[0]}\n"
                f"  Название: {wh[1]}\n"
                f"  Адрес: {wh[2]}\n"
                f"  Время работы: {wh[3]}\n\n"
            )
        await message.answer(text)
    else:
        await message.answer("База данных пуста. Сначала выполните команду /update.")

async def get_warehouse_info(message: Message):
    """Обработка текстового сообщения для поиска склада."""
    name = message.text.strip()
    warehouse = get_warehouse_by_name(name)
    if warehouse:
        id, name, address, work_time = warehouse
        text = (
            f"Склад найден:\n"
            f"- ID: {id}\n"
            f"- Название: {name}\n"
            f"- Адрес: {address}\n"
            f"- Время работы: {work_time}"
        )
    else:
        text = "Склад с таким названием не найден. Попробуйте другое название."
    await message.answer(text)
