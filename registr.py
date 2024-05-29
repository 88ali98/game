import sqlite3

connect = sqlite3.connect("users.db")
cursor = connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS users (
               id INTEGER PRIMARY KEY,
               name VARCHAR(100) NOT NULL,
               email VARCHAR(100) NOT NULL,
               age INTEGER NOT NULL,
               phone VARCHAR(100) NOT NULL
);""")

class Users:
    def __init__(self):
        self.name = None
        self.email = None
        self.age = 0
        self.phone = None

    def registr(self, name, email, age, phone):
        self.name = name
        self.email = email
        self.age = age
        self.phone = phone

        
        cursor.execute("""
                INSERT INTO users (name, email, age, phone)
                VALUES (?, ?, ?, ?)
            """, (name, email, age, phone))
        connect.commit()
    

    def start(self):
            print("Регистрация началась")
            name = input("Введите имя: ")
            email = input("Введите почту: ")
            age = input("Введите возраст: ")
            phone = input("Введите номер: ")
            self.registr(name, email, age, phone)

user = Users()
user.start()

connect.close()
