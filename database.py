import sqlite3
from datetime import datetime

# Подключение к базе данных
def create_connection():
    conn = sqlite3.connect("psychologist_bot.db")
    return conn

# Создание таблицы пользователей
def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            name TEXT,
            mood TEXT,
            important_notes TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Сохранение или обновление данных пользователя
def save_user_info(user_id, name=None, mood=None, notes=None):
    conn = create_connection()
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
    user = cursor.fetchone()

    if user is None:
        # Создание новой записи пользователя
        cursor.execute('INSERT INTO users (user_id, name, mood, important_notes) VALUES (?, ?, ?, ?)', 
                       (user_id, name, mood, notes))
    else:
        # Обновление существующего пользователя
        cursor.execute('''
            UPDATE users 
            SET name = COALESCE(?, name), 
                mood = COALESCE(?, mood), 
                important_notes = COALESCE(?, important_notes)
            WHERE user_id = ?
        ''', (name, mood, notes, user_id))

    conn.commit()
    conn.close()

# Получение данных пользователя
def get_user_info(user_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
    user = cursor.fetchone()
    conn.close()
    return user

# Добавление таблицы для хранения истории сообщений
def create_history_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS message_history (
            user_id INTEGER,
            message TEXT,
            mood TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()
    
# Сохранение сообщений и настроений
def save_message_history(user_id, message, mood):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO message_history (user_id, message, mood) 
        VALUES (?, ?, ?)
    ''', (user_id, message, mood))
    conn.commit()
    conn.close()

# Сохранение истории настроения
def save_mood_history(user_id, mood):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO mood_history (user_id, mood, timestamp) 
        VALUES (?, ?, ?)
    ''', (user_id, mood, datetime.now()))
    conn.commit()
    conn.close()

# Получение истории настроения пользователя
def get_mood_history(user_id, limit=7):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT mood, timestamp 
        FROM mood_history 
        WHERE user_id = ? 
        ORDER BY timestamp DESC 
        LIMIT ?
    ''', (user_id, limit))
    history = cursor.fetchall()
    conn.close()
    return history

# Добавление таблицы для истории настроений
def create_mood_history_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS mood_history (
            user_id INTEGER,
            mood TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()