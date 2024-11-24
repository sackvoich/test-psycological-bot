import google.generativeai as genai
import re
from gemini_api import API_KEY
import logging

# Устанавливаем API ключ для взаимодействия с Google Generative AI
genai.configure(api_key=API_KEY)

# Настройки генерации для модели
generation_config = {
    "temperature": 0.8,           # Контроль креативности ответа
    "top_p": 0.9,                 # Ограничение на выбор токенов для большей вариативности
    "max_output_tokens": 500,     # Количество токенов для ответа
    "response_mime_type": "text/plain"
}

# Создание модели и настройка генерации
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash-8b",
    generation_config=generation_config
)

# Инициализация сессии чата
chat_session = model.start_chat(
    history=[]
)

# Начальный промпт для модели
initial_prompt = """Ты - дружелюбный и эмпатичный психолог. Твоя задача - поддерживать пользователя, задавать уточняющие вопросы и помогать ему найти конструктивные решения. 

1. Всегда отвечай на русском языке.
2. Используй ясные и поддерживающие ответы.
3. Старайся избегать токсичных советов.
4. Если не можешь помочь, честно об этом скажи.

Начинай диалог!"""

chat_session.send_message(initial_prompt)

def format_response(text):
    """Форматирование ответа для корректного отображения в Telegram"""
    # Убираем любое форматирование
    return text

# Функция для генерации ответа через Google Generative AI
def get_gemini_response(user_input):
    try:
        logging.info(f"User input: {user_input}") 
        
        # Добавление нового сообщения от пользователя в историю чата
        response = chat_session.send_message(user_input)

        # Получаем текст из сгенерированного ответа
        generated_text = response.text.strip()
        
        logging.info(f"API response: {generated_text}") # Логируем ответ API

        # Фильтрация неадекватных ответов
        if is_inappropriate_or_repetitive(generated_text):
            return get_generic_response(), None
        
        # Форматируем текст (в данном случае убираем форматирование)
        formatted_text = format_response(generated_text)

        return formatted_text, None

    except Exception as e:
        logging.error(f"Error in get_gemini_response: {e}") # Логируем ошибки
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
        "Понимаю, что это может быть непросто. Я здесь, чтобы поддержать тебя.",
        "Мне жаль слышать, что ты так себя чувствуешь. Давай обсудим, как я могу помочь.",
        "Каждый сталкивается с трудностями, и это нормально. Важно знать, что ты не один."
    ]
    return responses[0]
