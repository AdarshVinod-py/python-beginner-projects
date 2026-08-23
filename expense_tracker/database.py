import sqlite3

def create_connection():
    connection = sqlite3.connect("expenses.db")
    cursor = connection.cursor()
    return connection, cursor

def create_tables(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS categories(
            id INTEGER PRIMARY KEY,
            category TEXT NOT NULL UNIQUE
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses(
            id INTEGER PRIMARY KEY,
            amount REAL NOT NULL,
            category_id INTEGER NOT NULL,
            date TEXT NOT NULL,
            description TEXT,
            FOREIGN KEY (category_id) REFERENCES categories(id)
            )
    """)

def insert_default_categories(cursor):
    cursor.execute("SELECT COUNT(*) FROM categories")
    result = cursor.fetchone()
    if result[0]== 0:
        categories_list = [ ("Food",),("Bills",),("Travel",),("Shopping",),("Health",),("Entertainment",),("Others",)]
        cursor.executemany("INSERT INTO categories (category) VALUES (?)",categories_list)

def setup_database():
    connection , cursor = create_connection()
    create_tables(cursor)
    insert_default_categories(cursor)
    connection.commit()
    connection.close()