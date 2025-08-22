# db.py
import sqlite3

def create_database():
    """Создание базы данных и таблицы пользователей"""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Создаём таблицу users, если она не существует
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            username TEXT DEFAULT '',
            first_name TEXT DEFAULT '',
            last_name TEXT DEFAULT ''
        );
    ''')

    conn.commit()
    conn.close()

def add_user(user_id, username=None, first_name=None, last_name=None):
    """Добавляет пользователя в базу данных, если его там ещё нет."""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Проверяем, существует ли уже такой пользователь
    cursor.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
    existing_user = cursor.fetchone()

    if not existing_user:
        # Если пользователя нет, добавляем его
        cursor.execute("""
            INSERT INTO users (user_id, username, first_name, last_name)
            VALUES (?,?,?,?)
        """, (user_id, username or '', first_name or '', last_name or ''))
        conn.commit()

    conn.close()

def get_all_users():
    """Возвращает список всех зарегистрированных пользователей"""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()

    users = [
        {
            'user_id': row[0],
            'username': row[1],
            'first_name': row[2],
            'last_name': row[3]
        }
        for row in rows
    ]

    conn.close()
    return users