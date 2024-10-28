from aiogram import Router, types, F
from aiogram.filters import Command
from local_gpt import get_gemini_response
from database import get_user_info

router = Router()

# Словарь для хранения контекста общения каждого пользователя
active_chats = {}

@router.message(Command("chat"))
async def start_chat(message: types.Message):
    user_id = message.from_user.id
    user_info = get_user_info(user_id)

    # Приветственное сообщение
    personalized_greeting = f"Привет! Я здесь, чтобы поддержать тебя. О чем бы ты хотел поговорить?\n"
    
    # Инициализация истории чата для пользователя
    active_chats[user_id] = None

    await message.answer(personalized_greeting)

@router.message(Command("exit_chat"))
async def exit_chat(message: types.Message):
    user_id = message.from_user.id

    # Удаляем пользователя из активных чатов
    if user_id in active_chats:
        del active_chats[user_id]
        await message.answer("Спасибо за разговор. Если тебе снова понадобится поддержка, не стесняйся обращаться ко мне!")
    else:
        await message.answer("Ты ещё не начал(а) чат. Введи /chat, чтобы начать общение.")

@router.message()
async def chat_with_bloom(message: types.Message):
    user_id = message.from_user.id

    # Проверка, находится ли пользователь в режиме чата
    if user_id not in active_chats:
        # Если пользователь не начал чат через команду /chat, игнорируем сообщение
        return

    # Генерация ответа от BLOOM через API
    user_message = message.text
    response, _ = get_gemini_response(user_message)

    # Ответ пользователю
    await message.answer(response)
