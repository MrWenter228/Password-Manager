import json
import os

FILE_NAME = "passwords.json"
def load_passwords():
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)
            if not isinstance(data, list):
                return []
            return data
    except json.JSONDecodeError:
        print("Файл passwords.json пошкоджений або порожній.")
        return []
    
def save_passwords(passwords):
    with open(FILE_NAME, "w") as file:
        json.dump(passwords, file, indent=4)