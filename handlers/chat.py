from aiogram import Router, types
from aiogram.filters import Command
from local_gpt import get_gemini_response
from database import get_user_info
from aiogram.types import ReplyKeyboardRemove

router = Router()

# Словарь для хранения состояния чата для каждого пользователя
active_chats = {}

@router.message(Command("chat"))
async def start_chat(message: types.Message):
    user_id = message.from_user.id
    user_info = get_user_info(user_id)

    # Приветственное сообщение и установка флага активного чата
    personalized_greeting = f"Привет! Я здесь, чтобы поддержать тебя. О чем бы ты хотел поговорить?\n"
    active_chats[user_id] = True  # Помечаем пользователя как активного в чате

    # Убираем кнопки меню
    await message.answer(personalized_greeting, reply_markup=ReplyKeyboardRemove())

@router.message(Command("exit_chat"))
async def exit_chat(message: types.Message):
    user_id = message.from_user.id

    # Удаляем пользователя из активных чатов
    if user_id in active_chats:
        del active_chats[user_id]
        await message.answer("Спасибо за разговор. Если тебе снова понадобится поддержка, не стесняйся обращаться ко мне!")
        
        # Возвращаем меню после завершения чата
        from handlers.menu import main_menu_keyboard
        await message.answer("Вы можете снова использовать меню:", reply_markup=main_menu_keyboard)
    else:
        await message.answer("Ты ещё не начал(а) чат. Введи /chat, чтобы начать общение.")

@router.message()
async def chat_with_bloom(message: types.Message):
    user_id = message.from_user.id

    # Проверка, находится ли пользователь в активном чате
    if user_id not in active_chats:
        # Если пользователь не в активном чате, обработчик не срабатывает
        return

    # Генерация ответа от AI-ассистента
    user_message = message.text
    response, _ = get_gemini_response(user_message)

    # Ответ пользователю
    await message.answer(response)
