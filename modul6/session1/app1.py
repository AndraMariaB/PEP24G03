import random


class Not18(Exception):
    pass


class Tombola:
    prize = {
        0: ["Un suc", "o punga de chipsuri", "o caserola de prajituri"],
        100: ["Un prajitor de paine", "O consola de Gaming", "o Tastatura mecanica"],
        500: ["Un robot de bucatarie", "o masina", "orice produs de la valorile de castig mai mic"]

    }

    def __init__(self):
        self.user = {}
        self.current_user = ""

    def get_cnp_from_user(self):
        cnp = input("CNP: ")
        self.user[cnp] = 0
        self.current_user = cnp

    def check_user_age(self):
        first_number = int(self.current_user[0])
        if first_number >= 1 and first_number <= 2:
            century = 1900
        elif first_number >= 5 and first_number <= 6:
            century = 2000
        else:
            century = 1800
        year = int(self.current_user[1:3])
        age = 2024 - (year + century)
        if age < 18:
            raise Not18('User is not 18')

    def get_value_of_receipt(self):
        self.user[self.current_user] = float(input("Introduceti valoarea bonului: "))

    def get_winner(self):
        winner_cnp = random.choice(list(self.user.keys()))
        value = self.user[winner_cnp]
        if value < 100:
            winn = random.choice(self.prize[0])
        elif 100 >= value <= 500:
            winn = random.choice(self.prize[100])
        elif value > 500:
            winn = random.choice(self.prize[500] + self.prize[100] + self.prize[0])
        else:
            raise RuntimeError("Valuarea de pe bon nu este corecta")

        print(f"Felicitari {winner_cnp}!!!")
        print(f"Ai castigat: {winn}")

    def start(self):
        while True:
            self.get_cnp_from_user()
            self.check_user_age()
            self.get_value_of_receipt()
            more_users = input("Add new user? [no]")
            if more_users == "no":
                break
        self.get_winner()


tombola1 = Tombola()
tombola1.start()
