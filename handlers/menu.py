from aiogram import Router, types, F
from aiogram.filters import Command
import logging
from keyboards.menu_keyboards import main_menu_keyboard, back_to_menu_keyboard  # Импортируем клавиатуры
from aiogram.fsm.context import FSMContext # Импортируем FSMContext
from handlers.states import ChatState  # <--- Импортируйте ChatState


router = Router()
router.name = 'menu'

@router.message(Command("menu"))
async def show_menu(message: types.Message):
    logging.info("Menu command invoked")
    await message.answer("Выберите пункт меню:", reply_markup=main_menu_keyboard)

# Обработчик для каждой кнопки меню с функционалом
@router.message(lambda message: message.text in ["📚 Полезные ресурсы", "💡 Советы", "📞 Контакты", "😊 Настроение", "🆘 Помощь", "👨‍⚕️ Чат с психологом"])
async def handle_menu_buttons(message: types.Message, state: FSMContext):
    logging.info(f"Button pressed: {message.text}")
    current_state = await state.get_state()

    if current_state is None: # Если не в чате, показываем основное меню
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
        elif message.text == "👨‍⚕️ Чат с психологом" and current_state != ChatState.CHAT.state: # Если в чате, игнорируем кнопку
            from handlers.chat import start_chat  # Импортируем обработчик чата
            await start_chat(message, state)  # Запускаем чат
        
@router.message(F.text == "⏪ Назад в меню")
async def back_to_main_menu(message: types.Message, state: FSMContext):
    await state.clear() # очищаем состояние, если пользователь был в чате
    await show_menu(message)
