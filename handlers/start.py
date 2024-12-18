from aiogram import Router, types
from aiogram.filters import Command
from handlers.menu import main_menu_keyboard  # Обновите импорт
from database import create_table, save_user_info, create_mood_history_table

router = Router()

# Создание таблицы при старте
create_table()
create_mood_history_table()

@router.message(Command("start"))
async def send_welcome(message: types.Message):
    # Сохранение информации о пользователе
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    save_user_info(user_id=user_id, name=user_name)
    
    await message.answer(
        f"Привет, {user_name}! Я MindMate, чат-бот для поддержки твоего психического здоровья.\n\n"
        "Вот что я умею делать. Выбери команду ниже или напиши /help, чтобы узнать больше.",
        reply_markup=main_menu_keyboard
    )