from aiogram import Router, types, F
from aiogram.filters import Command
from local_gpt import get_gemini_response
from database import get_user_info
from aiogram.types import ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from .states import ChatState
from handlers.menu import main_menu_keyboard
import logging
from keyboards.menu_keyboards import chat_menu_keyboard # <--- Импортируйте новую клавиатуру

router = Router()

@router.message(Command("chat"))
async def start_chat(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    user_info = get_user_info(user_id)

    personalized_greeting = f"Привет! Я здесь, чтобы поддержать тебя. О чем бы ты хотел поговорить?\n"
    await message.answer(personalized_greeting, reply_markup=chat_menu_keyboard) # <--- Используем новую клавиатуру
    logging.info("Setting state to ChatState.CHAT")
    await state.set_state(ChatState.CHAT)
    
    current_state = await state.get_state()
    logging.info(f"Current state after setting: {current_state}")

@router.message(Command("exit_chat"))
async def exit_chat(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state == ChatState.CHAT.state:
        await state.clear()
        await message.answer("Спасибо за разговор...", reply_markup=main_menu_keyboard)
    else:
        await message.answer("Ты ещё не начал(а) чат...")

@router.message(ChatState.CHAT)
async def chat_with_bloom(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    print(f"chat_with_bloom called! Message: {message.text}")

    user_message = message.text
    response, _ = get_gemini_response(user_message) # Убедитесь, что эта функция возвращает корректный ответ
    print(response)
    try:
        await message.answer(response)
    except Exception as e:
        logging.error(f"Error sending message: {str(e)}") # Логируйте саму ошибку
        await message.answer(f"Произошла ошибка: {e}")
        
@router.message(ChatState.CHAT, F.text == "❌ Завершить чат")
async def exit_chat_button(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Чат завершен. Вы вернулись в главное меню.", reply_markup=main_menu_keyboard)