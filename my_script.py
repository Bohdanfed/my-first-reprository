def greet_user():
    name = input("Введіть ваше ім'я: ")
    age = input("Введіть ваш вік: ")
    print(f"Привіт, {name}! Вам {age} років.")

if __name__ == "__main__":
    greet_user()