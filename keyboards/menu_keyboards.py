from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Основная клавиатура меню
main_menu_keyboard = types.ReplyKeyboardMarkup(
    keyboard=[
        [types.KeyboardButton(text="📚 Полезные ресурсы")],
        [types.KeyboardButton(text="💡 Советы")],
        [types.KeyboardButton(text="📞 Контакты")],
        [types.KeyboardButton(text="😊 Настроение")],
        [types.KeyboardButton(text="🆘 Помощь")],
        [types.KeyboardButton(text="👨‍⚕️ Чат с психологом")]
    ],
    resize_keyboard=True
)

# Клавиатура с кнопкой "Назад в меню"
back_to_menu_keyboard = types.ReplyKeyboardMarkup(
    keyboard=[
        [types.KeyboardButton(text="⏪ Назад в меню")],
    ],
    resize_keyboard=True
)

chat_menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="❌ Завершить чат")],
        [KeyboardButton(text="⏪ Назад в меню")] # Сохраняем кнопку "Назад в меню"
    ],
    resize_keyboard=True
)