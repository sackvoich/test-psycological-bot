from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

router = Router()

# Создание клавиатуры с выбором настроения
buttons = [
    [KeyboardButton(text="😊 Хорошее")],
    [KeyboardButton(text="😐 Нейтральное")],
    [KeyboardButton(text="😔 Плохое")]
]
mood_keyboard = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

@router.message(Command("mood"))
async def ask_mood(message: types.Message):
    await message.answer("Как ты себя чувствуешь сегодня?", reply_markup=mood_keyboard)

@router.message(F.text.in_({"😊 Хорошее", "😐 Нейтральное", "😔 Плохое"}))
async def receive_mood(message: types.Message):
    mood = message.text
    await message.answer(
        f"Спасибо, что поделился(лась) своим настроением: {mood}",
        reply_markup=ReplyKeyboardRemove()
    )
