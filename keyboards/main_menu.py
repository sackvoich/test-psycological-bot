from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Создаем кнопки для основных команд
buttons = [
    [KeyboardButton(text="/resources")],
    [KeyboardButton(text="/tips")],
    [KeyboardButton(text="/contact")],
    [KeyboardButton(text="/mood")],
    [KeyboardButton(text="/help")]
]

main_menu_keyboard = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
