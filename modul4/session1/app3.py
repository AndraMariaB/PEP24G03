def get_passwords():
    user_passwords = {}
    for number in range(1, 4):
        user = input(f"Introduceti utilizatorul PC-ului {number}:")
        password = input(f"Introduceti parola PC-ului {number}:")
        user_passwords.update({user: password})
    for key, value in user_passwords.items():
        print(f"{key}-->{value}")

get_passwords()