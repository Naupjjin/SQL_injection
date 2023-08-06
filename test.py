import sqlite3

username = input("請輸入用戶名稱: ")
password = input("請輸入密碼: ")


conn = sqlite3.connect('user_database.db')
cursor = conn.cursor()

query = f"SELECT id, username FROM users WHERE username = '{username}' AND password = '{password}'"
cursor.execute(query)

user = cursor.fetchone()

conn.close()


if user:
    print("登錄成功！")
    print("用戶 ID:", user[0])
    print("用戶名稱:", user[1])
else:
    print("登錄失敗。")
