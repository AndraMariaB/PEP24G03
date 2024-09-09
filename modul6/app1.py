class Not18(Exception):
    pass


class Tombola:

    def __init__(self):
        self.user = []
        print("creating new game")

    def get_cnp_from_user(self):
        cnp = input("CNP: ")
        self.user.append(cnp)

    def check_user_age(self):
        for cnp in self.user:
            first_number = int(cnp[0])
            if first_number >= 1 and first_number <= 2:
                century = 1900
            elif first_number >= 5 and first_number <= 6:
                century = 2000
            else:
                century = 1800
            year = int(cnp[1:3])
            age = 2024 - (year + century)
            if age < 18:
                raise Not18('User is not 18')


tombola1 = Tombola()
tombola1.get_cnp_from_user()
print(tombola1.user)
tombola1.check_user_age()
print(tombola1.user)
# tombola1.new_thing = 10
# print(tombola1.new_thing)
# print(Tombola.new_thing)
# result = tombola.get_cnp_from_user()

# tombola2 = Tombola()
