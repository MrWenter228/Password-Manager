import random

def create_random_password():
    length = int(input("Введіть довжину пароля: "))
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-+"
    if length <= 10:
        print("Довжина пароля повинна бути більше 10 символів.")
        return
    if length >= 24:
        print("Довжина пароля не повинна перевищувати 24 символів.")
        return
    password = ''.join(random.choice(characters) for _ in range(length))
    print(f"Ваш новий випадковий пароль: {password}")