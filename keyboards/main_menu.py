from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Создаем кнопки для основных команд
buttons = [
    [KeyboardButton(text="/resources")],  # Кнопка для вызова команды /resources
    [KeyboardButton(text="/tips")],       # Кнопка для вызова команды /tips
    [KeyboardButton(text="/contact")],    # Кнопка для вызова команды /contact
    [KeyboardButton(text="/mood")],       # Кнопка для вызова команды /mood
    [KeyboardButton(text="/help")]        # Кнопка для вызова команды /help
]

main_menu_keyboard = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
