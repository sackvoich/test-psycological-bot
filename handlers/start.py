from aiogram import Router, types
from aiogram.filters import Command
from keyboards.main_menu import main_menu_keyboard

router = Router()

@router.message(Command(commands=['start']))
async def send_welcome(message: types.Message):
    await message.answer(
        "Привет! Я MindMate, чат-бот для поддержки твоего психического здоровья.\n\n"
        "Вот что я умею делать. Выбери команду ниже или напиши /help, чтобы узнать больше.",
        reply_markup=main_menu_keyboard
    )
