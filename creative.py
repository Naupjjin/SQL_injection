import sqlite3
conn = sqlite3.connect('user_database.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        username TEXT,
        password TEXT
    )
''')

cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ('admin', 'dsfseqopokpafopddoapkfoakpodf'))


conn.commit()
conn.close()
