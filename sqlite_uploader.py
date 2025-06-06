import sqlite3

def upload_to_sqlite(mongo_data, sqlite_path='user_history.db'):
    conn = sqlite3.connect(sqlite_path)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL,
            date TEXT NOT NULL
        )
    ''')

    for record in mongo_data:
        cursor.execute('INSERT INTO user_history (email, date) VALUES (?, ?)', (record['email'], record['date']))

    conn.commit()
    conn.close()
    print("Data uploaded to SQLite.")
