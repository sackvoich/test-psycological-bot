from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keyboards.inline_menu import inline_menu


router = Router()

# Создание клавиатуры с выбором настроения
buttons = [
    [KeyboardButton(text="😊 Хорошее")],
    [KeyboardButton(text="😐 Нейтральное")],
    [KeyboardButton(text="😔 Плохое")]
]
mood_keyboard = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

# Обработчик команды /mood для запроса настроения
@router.message(Command(commands=['mood']))
async def ask_mood(message: types.Message):
    await message.answer("Как ты себя чувствуешь сегодня?", reply_markup=mood_keyboard)

# Обработчик для ответа пользователя о настроении
@router.message()
async def receive_mood(message: types.Message):
    # Проверяем, содержится ли текст в заранее определённых вариантах
    if message.text in ["😊 Хорошее", "😐 Нейтральное", "😔 Плохое"]:
        mood = message.text
        # Сохраните настроение в базе данных, если это нужно
        await message.answer(f"Спасибо, что поделился(лась) своим настроением: {mood}", reply_markup=types.ReplyKeyboardRemove())
