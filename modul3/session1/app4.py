pass_pc = '7677'
for _ in range(3):
    if input("Introduceti parola: ") != pass_pc:
        print("Mai incearca.")
    else:
        print("Access allowed.")
        break
else:
    print("Access denied.")
