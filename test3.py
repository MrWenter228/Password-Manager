import json
import os
import random
i = 0
while i < 3:
    try:
        pincode = int(input("Введіть пін-код: "))
    except ValueError:
        print("Введіть число.")
        continue
    if pincode == 1234:
        print("Пін-код вірний. Доступ дозволено.")
        break
    i = i + 1
    if i < 3:
        print("Невірний пін-код. У вас залишилось", 3 - i, "спроб.")
if pincode != 1234 and i == 3:
    print("Невірний пін-код. Доступ заборонено.")
    exit()
if os.path.exists("passwords.json"):
    with open("passwords.json", "r") as file:
        password_history = json.load(file)
else:
    password_history = []
def add_password():
    website = input("Введіть назву сайту: ")
    username = input("Введіть ім'я користувача: ")
    password = input("Введіть пароль: ")
    password_entry = {
        "website": website,
        "username": username,
        "password": password
    }
    password_history.append(password_entry)
    with open("passwords.json", "w") as file:
        json.dump(password_history, file)
    print("Пароль додано успішно!")
def show_passwords():
    if not password_history:
        print("Список паролів порожній.")
    else:
        for entry in password_history:
            print(f"Назва сайту: {entry['website']}\nІм'я користувача: {entry['username']} \nПароль: {entry['password']}")
def search_password():
    search_website = input("Введіть назву сайту для пошуку: ")
    found = False
    for entry in password_history:
        if entry["website"].lower() == search_website.lower():
            print(f"Знайдено пароль для сайту {search_website}:")
            print(f"Ім'я користувача: {entry['username']}\nПароль: {entry['password']}")
            found = True
            break
    if not found:
        print(f"Пароль для сайту {search_website} не знайдено.")
def delete_password():
    delete_website = input("Введіть назву сайту для видалення пароля: ")
    for entry in password_history:
        if entry["website"].lower() == delete_website.lower():
            password_history.remove(entry)
            with open("passwords.json", "w") as file:
                json.dump(password_history, file)
            print(f"Пароль для сайту {delete_website} видалено.")
            return
    print(f"Пароль для сайту {delete_website} не знайдено.")
def create_random_password():
    length = int(input("Введіть довжину пароля: "))
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-+"
    if length < 10:
        print("Довжина пароля повинна бути більше 10 символів.")
        return
    if length > 24:
        print("Довжина пароля не повинна перевищувати 24 символів.")
        return
    password = ''.join(random.choice(characters) for _ in range(length))
    print(f"Ваш новий випадковий пароль: {password}")
def change_password():
    website = input("Введіть назву сайту для зміни пароля: ")
    for entry in password_history:
        if entry["website"].lower() == website.lower():
            new_password = input("Введіть новий пароль: ")
            entry["password"] = new_password
            with open("passwords.json", "w") as file:
                json.dump(password_history, file)
            print(f"Пароль для сайту {website} змінено.")
            return
    print(f"Пароль для сайту {website} не знайдено.")
def menu():
    while True:
        try:
            password_menu = int(input("1 - Додати пароль\n2 - Показати всі паролі\n3 - Знайти пароль\n4 - Видалити пароль\n5 - створити випадковий пароль\n6 - Змінити пароль\n7 - Вийти\n"))
        except ValueError:
            print("Введіть число від 1 до 7.")
            continue
        if password_menu == 1:
            add_password()
        elif password_menu == 2:
            show_passwords()
        elif password_menu == 3:
            search_password()
        elif password_menu == 4:
            delete_password()
        elif password_menu == 5:
            create_random_password()
        elif password_menu == 6:
            change_password()
        elif password_menu == 7:
            print("Вихід з програми.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")
menu()