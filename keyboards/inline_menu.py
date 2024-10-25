from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Создаем инлайн-кнопки для команд
inline_buttons = [
    [InlineKeyboardButton(text="Ресурсы", callback_data="resources")],
    [InlineKeyboardButton(text="Советы", callback_data="tips")],
    [InlineKeyboardButton(text="Связаться с психологом", callback_data="contact")],
    [InlineKeyboardButton(text="Как вы себя чувствуете?", callback_data="mood")],
    [InlineKeyboardButton(text="Помощь", callback_data="help")]
]

inline_menu = InlineKeyboardMarkup(inline_keyboard=inline_buttons)
