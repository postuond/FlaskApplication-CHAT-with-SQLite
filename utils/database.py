from .db_connection import DatabaseConnection
import sqlite3

chat_file = 'history.db'

"""
    SQLite has 5 ways how to store data:

    1 - text, which is used for strings [text primary key is means no duplicates is allowed]
    2 - null, which means empty or void or no data here
    3 - integer, which means a whole number
    4 - real, which means float number
    5 - blob, which is binary data field, where you can store images or documents [ .pdf ] etc...

"""


def create_chat_table():
    with DatabaseConnection('history.db') as connection:
        cursor = connection.cursor()

        cursor.execute('CREATE TABLE IF NOT EXISTS history(chat text)')

def add_chat(chat):
    with DatabaseConnection('history.db') as connection:
        cursor = connection.cursor()
        cursor.execute('INSERT INTO history VALUES(?)', (chat,))
