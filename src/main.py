import asyncio
from aiogram import Bot, Dispatcher, F
from src.config import TELEGRAM_BOT_TOKEN
from src.database import init_db
from src.handlers import (
    start_command,
    update_warehouses,
    list_warehouses,
    get_warehouse_info
)

# Создаем объект бота
bot = Bot(TELEGRAM_BOT_TOKEN)
dp = Dispatcher()

# Регистрируем обработчики
dp.message.register(start_command, F.text == "/start")
dp.message.register(update_warehouses, F.text == "/update")
dp.message.register(list_warehouses, F.text == "/list")
dp.message.register(get_warehouse_info)

async def main():
    print("Бот запущен!")
    # Инициализация базы данных
    init_db()
    # Удаляем старые обновления
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
