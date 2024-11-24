from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from database import save_user_info, save_mood_history, get_mood_history  # Импортируем функции для работы с историей настроений
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
    save_mood_history(user_id, mood)  # Сохраняем настроение в историю

    # Получаем историю настроений пользователя
    mood_history = get_mood_history(user_id)

    # Персонализируем приветствие в зависимости от последнего настроения
    if mood == "😊 Хорошее":
        greeting = f"Замечательно! Рад, что у тебя хорошее настроение. Если нужна будет помощь, я здесь."
    elif mood == "😐 Нейтральное":
        greeting = f"Понятно. Надеюсь, я смогу тебе чем-то помочь."
    else:
        greeting = f"Мне жаль, что ты чувствуешь себя плохо. Помни, что я здесь, чтобы поддержать тебя. Давай попробуем найти решение вместе."

        # Если плохое настроение, можно предложить ресурсы
        from handlers.resources import send_resources
        await send_resources(message)

    await message.answer(
        f"{greeting}\n\nСпасибо, что поделился(лась) своим настроением: {mood}",
        reply_markup=ReplyKeyboardRemove()
    )

    # Выводим историю настроений (опционально)
    if mood_history:
        history_str = "Твои последние настроения:\n"
        for m, t in mood_history:
            history_str += f"- {t.strftime('%Y-%m-%d %H:%M')}: {m}\n"
        await message.answer(history_str)

    # Возвращаем основное меню
    await message.answer("Выберите пункт меню:", reply_markup=main_menu_keyboard)