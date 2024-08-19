def suma(lista: list):
    return sum(lista)


def medie(lista: list):
    return suma(lista) / len(lista)


def putere(lista: list):
    result = 1
    for i in lista:
        result **= i
    return result


meniu = {
    "1": medie,
    "2": suma,
    "3": putere,
}


def math_operation():
    numbers = list()
    while True:
        try:
            number = float(input("Introduceti numere, x pentru incheiere: "))
        except ValueError as e:
            print(e.args)
            if (e.args[0]) == "could not convert string to float: 'x'":
                print("all numbers received")
                break
            else:
                raise e
        else:
            numbers.append(number)

    print("""
    Meniu:
    1. Media numerelor
    2. Suma numerelor
    3. Puterea numerelor din lista de numere
    4. Iesire
    """)
    option = input("Introduceti optiunea dvs: ").strip()

    try:
        f = meniu[option]
    except KeyError as e:
        if e.args[0] == "4":
            raise SystemExit
        else:
            raise e
    else:
        result = f(numbers)
        return result


print(math_operation())
