import sqlite3


def connect():
    conn = sqlite3.connect('data_store.db')
    cursor = conn.cursor()
    return cursor,conn
