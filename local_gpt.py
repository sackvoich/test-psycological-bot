import google.generativeai as genai
import re
from gemini_api import API_KEY

# Устанавливаем API ключ для взаимодействия с Google Generative AI
genai.configure(api_key=API_KEY)

# Настройки генерации для модели
generation_config = {
    "temperature": 0.8,           # Контроль креативности ответа
    "top_p": 0.9,                 # Ограничение на выбор токенов для большей вариативности
    "max_output_tokens": 400,     # Количество токенов для ответа
    "response_mime_type": "text/plain"
}

# Создание модели и настройка генерации
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config
)

# Инициализация сессии чата
chat_session = model.start_chat(
    history=[]
)

# Функция для генерации ответа через Google Generative AI
def get_gemini_response(user_input):
    try:
        # Добавление нового сообщения от пользователя в историю чата
        response = chat_session.send_message(user_input)

        # Получаем текст из сгенерированного ответа
        generated_text = response.text.strip()

        # Фильтрация неадекватных ответов
        if is_inappropriate_or_repetitive(generated_text):
            return get_generic_response(), None

        return generated_text, None

    except Exception as e:
        return f"Произошла ошибка при подключении к API: {str(e)}", None

# Функция для проверки на неадекватные или повторяющиеся ответы
def is_inappropriate_or_repetitive(text):
    # Проверяем наличие большого количества повторений одного и того же
    if len(set(text.split())) < 5:
        return True
    # Проверяем на содержание фраз, которые противоречат поддерживающей функции
    prohibited_phrases = [
        "бросить", "убить", "насилие", "перестань любить", "она не стоит тебя", "сделай её счастливой"
    ]
    for phrase in prohibited_phrases:
        if re.search(rf"\b{phrase}\b", text, re.IGNORECASE):
            return True
    return False

# Функция для возврата поддерживающего шаблонного ответа
def get_generic_response():
    responses = [
        "Понимаю, как тебе сейчас сложно. Я здесь, чтобы поддержать тебя, давай попробуем вместе найти лучшее решение.",
        "Мне жаль, что ты чувствуешь себя так. Помни, что ты не один, и я готов помочь тебе найти выход.",
        "Это действительно тяжёлая ситуация, но важно помнить, что всё может измениться. Давай обсудим, что ты можешь сделать, чтобы почувствовать себя лучше."
    ]
    return responses[0]
