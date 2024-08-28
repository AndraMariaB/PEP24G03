import random

name = input("Introduceti numele: ")

for i in range(3):
    print("Introduceti optiunea [p (piatra), f(foarfeca), h(hartie) q pentru a iesi]:")
    user_option = input(f"-> {name}:").strip()
    server_option = random.choice(["p", "f", "h"])
    print(f"-> server: {server_option}")
    if user_option == "p":
        if server_option == "p":
            pass
        elif server_option == "f":
            print(name + "ai castigat.")
        elif server_option == "h":
            print(name + "ai pierdut.")
    elif user_option == "f":
        if server_option == "p":
            print(name + "ai pierdut.")
        elif server_option == "f":
            pass
        elif server_option == "h":
            print(name + "ai castigat.")
    elif user_option == "h":
        if server_option == "p":
            print(name + "ai castigat.")
        elif server_option == "f":
            print(name + "ai pierdut.")
        elif server_option == "h":
            pass