import sqlite3

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
