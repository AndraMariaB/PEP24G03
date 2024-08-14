# get number from user (n1)
# define function
# while loop until "q" (n2)
# n1 ** n2

n1 = int(input("Give first number: "))


def power_of_number(number1):
    while True:
        number2 = input("Give second number: ")
        if number2 == "q":
            return
        else:
            number2 = int(number2)
        print(number1 ** number2)


power_of_number(n1)
