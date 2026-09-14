from storage import load_passwords
from password_manager import PasswordManager
from generator_passwords import create_random_password
from pincode_check import check_pincode, create_pincode
import os
import json

def menu(manager):
    while True:
        print("\n===== PASSWORD MANAGER =====")
        print("1 - Додати пароль")
        print("2 - Показати всі паролі")
        print("3 - Знайти пароль")
        print("4 - Видалити пароль")
        print("5 - Створити випадковий пароль")
        print("6 - Змінити пароль")
        print("7 - Вийти")
        try:
            choice = int(input("Виберіть дію: "))
        except ValueError:
            print("Введіть число від 1 до 7.")
            continue
        if choice == 1:
            manager.add_password()
        elif choice == 2:
            manager.show_passwords()
        elif choice == 3:
            manager.search_password()
        elif choice == 4:
            manager.delete_password()
        elif choice == 5:
            create_random_password()
        elif choice == 6:
            manager.change_password()
        elif choice == 7:
            print("Вихід з програми.")
            break
        else:
            print("Невірний вибір.")

def main():
    if not os.path.exists("pincode.json"):
        create_pincode()
    if not check_pincode():
        return
    passwords = load_passwords()
    manager = PasswordManager(passwords)
    menu(manager)

if __name__ == "__main__":
    main()