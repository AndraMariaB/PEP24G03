def password_checker(password: str):
    if len(password) < 7:
        print("Parola trebuie sa aiba lungimea mai mare de 7 caractere.")
        return False
    if not (password.count('@') + password.count('!') + password.count('%')):
        print("Parola trebuie sa contina una din urmatoarele caractere: %, !, @.")
        return False
    for letter in password:
        if letter.isdigit():
            break
    else:
        print("Parola trebuie sa contina o cifra.")
        return False
    return True


while not password_checker(input("Introduceti o parola:")):
    pass
print("Parola este in regula.")

# print(password_checker("Bianca123@"))
# print(password_checker("Bianca123"))
# print(password_checker("Bianca@"))
# print(password_checker("B123@"))
