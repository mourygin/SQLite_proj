#coding=UTF-8
import sqlite3
from random import randint

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER)
''')
connection.commit()

cursor.execute('DELETE FROM Users')
connection.commit()

for i in range(1, 10):
    query = f'''
    INSERT INTO Users
    (username, email, age, balance)
    VALUES
    ('user_{i}', 'mail_{i}', {randint(18,70)}, 1000)'''
    cursor.execute(query)
connection.commit()

for i in range(1,10,2):
    query = f'UPDATE Users SET balance = 500 WHERE id = {i}'
    cursor.execute(query)
connection.commit()

for i in range(1,10,3):
    query = f'DELETE FROM Users WHERE id = {i}'
    cursor.execute(query)
connection.commit()

query = 'SELECT username, email, age, balance FROM Users WHERE age <> 60'
cursor.execute(query)
users = cursor.fetchall()
for user in users:
    print(user)
connection.close()