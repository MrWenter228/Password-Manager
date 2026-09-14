import json
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError, VerificationError

PIN_FILE = "pincode.json"

ph = PasswordHasher(
    time_cost=3,
    memory_cost=65536,
    parallelism=4
)

def create_pincode():
    while True:
        pincode = input("Введіть новий PIN-код (4 цифри): ")
        if not pincode.isdigit():
            print("PIN-код повинен містити тільки цифри.")
            continue
        if len(pincode) != 4:
            print("PIN-код повинен містити 4 цифри.")
            continue
        hashed_pincode = ph.hash(pincode)
        with open(PIN_FILE, "w") as pin_file:
            json.dump(
                {"pincode": hashed_pincode},
                pin_file,
                indent=4
            )
        print("PIN-код успішно створено.")
        return True

def check_pincode():
    try:
        with open(PIN_FILE, "r") as pin_file:
            data = json.load(pin_file)

        correct_hash = data["pincode"]
    except FileNotFoundError:
        print("PIN-код ще не створений.")
        return False
    except (json.JSONDecodeError, KeyError):
        print("Файл PIN-коду пошкоджений.")
        return False
    i = 0
    while i < 3:
        pincode = input("Введіть PIN-код: ")

        try:
            ph.verify(correct_hash, pincode)

            print("PIN-код правильний. Доступ дозволено.")
            return True

        except (VerifyMismatchError, VerificationError):
            i += 1

            if i < 3:
                print(
                    f"Невірний PIN-код. "
                    f"Залишилось спроб: {3 - i}."
                )

    print("Доступ заборонено.")
    return False