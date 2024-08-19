def power_of_number(numbers: list):
    powers = []
    second_numer = int(input("Provide power of number: "))
    for number in numbers:
        result = number ** second_numer
        powers.append(result)
    return powers


def calculate_sum(numbers: list):
    result = 0
    for number in numbers:
        result += number
    return result


def multiplication_of_number(numbers: list):
    powers = []
    second_numer = int(input("Provide multiplier: "))
    for number in numbers:
        result = number * second_numer
        powers.append(result)
    return powers


def calculate_numbers():
    good_numbers = list()
    user_input = input("Please enter numbers separated by commas: ")
    user_input_list = user_input.split(',')
    print(user_input_list)
    for number in user_input_list:  # type: str
        if not number.isnumeric():
            print(f"Number {number} is not a good number. ")
            continue
        else:
            int_number = int(number)
        if 0 <= int_number <= 100:
            good_numbers.append(int_number)
    while True:
        print("""
    1. Fiecare numar la puterea y
    2. Suma tuturor numerelor din lista
    3. Inmultirea fiecarui numar cu y
    4. Iesire
        """)
        option = input("Alegeti optiunea: ").strip()
        if option == "1":
            result = power_of_number(good_numbers)
        elif option == "2":
            result = calculate_sum(good_numbers)
        elif option == "3":
            result = multiplication_of_number(good_numbers)
        elif option == "4":
            quit()
        else:
            result = None
        print(result)


calculate_numbers()
