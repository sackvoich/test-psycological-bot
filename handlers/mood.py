from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from database import save_user_info
from handlers.menu import main_menu_keyboard  # Импортируем основное меню

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
    user_id = message.from_user.id
    # Сохраняем настроение пользователя
    save_user_info(user_id=user_id, mood=mood)
    
    user_id = message.from_user.id
    # Сохраняем настроение пользователя
    save_user_info(user_id=user_id, mood=mood)
    
    await message.answer(
        f"Спасибо, что поделился(лась) своим настроением: {mood}",
        reply_markup=ReplyKeyboardRemove()
    )
    
    # Возвращаем основное меню
    await message.answer("Выберите пункт меню:", reply_markup=main_menu_keyboard)
