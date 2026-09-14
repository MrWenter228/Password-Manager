from storage import save_passwords

class PasswordManager:
    def __init__(self, passwords):
        self.passwords = passwords
    def add_password(self):
        website = input("Введіть назву сайту: ")
        username = input("Введіть ім'я користувача: ")
        password = input("Введіть пароль: ")

        if not website or not username or not password:
            print("Усі поля повинні бути заповнені.")
            return
        password_entry = {
            "website": website,
            "username": username,
            "password": password
        }
        self.passwords.append(password_entry)
        save_passwords(self.passwords)
        print("Пароль додано успішно!")
    def show_passwords(self):
        if not self.passwords:
            print("Список паролів порожній.")
            return
        for entry in self.passwords:
            print(
                f"\nНазва сайту: {entry['website']}"
                f"\nІм'я користувача: {entry['username']}"
                f"\nПароль: {entry['password']}"
            )
    def search_password(self):
        website = input("Введіть назву сайту для пошуку: ")
        found = False
        for entry in self.passwords:
            if website.lower() in entry["website"].lower():
                print(
                    f"\nСайт: {entry['website']}"
                    f"\nІм'я користувача: {entry['username']}"
                    f"\nПароль: {entry['password']}"
                )
                found = True
        if not found:
            print(f"Пароль для {website} не знайдено.")
    def delete_password(self):
        website = input("Введіть назву сайту для видалення: ")

        for entry in self.passwords:
            if entry["website"].lower() == website.lower():
                confirm = input(
                    f"Видалити пароль для {entry['website']}? (y/n): "
                )
                if confirm.lower() != "y":
                    print("Видалення скасовано.")
                    return
                self.passwords.remove(entry)
                save_passwords(self.passwords)

                print("Пароль видалено.")
                return
        print(f"Пароль для {website} не знайдено.")
    def change_password(self):
        website = input("Введіть назву сайту: ")
        for entry in self.passwords:
            if entry["website"].lower() == website.lower():
                new_password = input("Введіть новий пароль: ")
                if not new_password:
                    print("Пароль не може бути порожнім.")
                    return
                entry["password"] = new_password
                save_passwords(self.passwords)
                print("Пароль успішно змінено.")
                return
        print(f"Пароль для {website} не знайдено.")