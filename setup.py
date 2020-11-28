import sqlite3

connection = sqlite3.connect("data.db")
cursor = connection.cursor()

with open("setup.sql", "r") as sql:
    cursor.executescript(sql.read())

with open("token.0", "w") as file:
    token = input("Enter your discord bot token: ")
    file.write(token)