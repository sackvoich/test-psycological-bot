from aiogram import Router, types
from aiogram.filters import Command
import logging

router = Router()
router.name = 'menu'

# Восстанавливаем оригинальную клавиатуру меню с эмодзи
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

@router.message(Command("menu"))
async def show_menu(message: types.Message):
    logging.info("Menu command invoked")
    await message.answer("Выберите пункт меню:", reply_markup=main_menu_keyboard)

# Обработчик для каждой кнопки меню с функционалом
@router.message(lambda message: message.text in ["📚 Полезные ресурсы", "💡 Советы", "📞 Контакты", "😊 Настроение", "🆘 Помощь", "👨‍⚕️ Чат с психологом"])
async def handle_menu_buttons(message: types.Message):
    # Проверяем, что пользователь не находится в чате
    from handlers.chat import active_chats
    if message.from_user.id in active_chats:
        logging.info(f"User in chat tried to access menu: {message.text}")
        return

    logging.info(f"Button pressed: {message.text}")

    if message.text == "📚 Полезные ресурсы":
        from handlers.resources import send_resources  # Импортируем обработчик ресурсов
        await send_resources(message)  # Вызываем функцию для отправки ресурсов
    elif message.text == "💡 Советы":
        from handlers.tips import send_tips  # Импортируем обработчик советов
        await send_tips(message)  # Вызываем функцию для отправки советов
    elif message.text == "📞 Контакты":
        from handlers.contact import send_contact  # Импортируем обработчик контактов
        await send_contact(message)  # Вызываем функцию для отправки контактов
    elif message.text == "😊 Настроение":
        from handlers.mood import ask_mood  # Импортируем обработчик настроения
        await ask_mood(message)  # Вызываем функцию для запроса настроения
    elif message.text == "🆘 Помощь":
        from handlers.help import send_help  # Импортируем обработчик помощи
        await send_help(message)  # Вызываем функцию для отправки помощи
    elif message.text == "👨‍⚕️ Чат с психологом":
        from handlers.chat import start_chat  # Импортируем обработчик чата
        await start_chat(message)  # Запускаем чат
