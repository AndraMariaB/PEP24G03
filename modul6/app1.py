class Tombola:

    def __init__(self):
        self.user = []
        print("creating new game")


    def get_cnp_from_user(self):
        cnp = input("CNP: ")
        self.user.append(cnp)


tombola1 = Tombola()
tombola1.get_cnp_from_user()
print(tombola1.user)

# tombola1.new_thing = 10
# print(tombola1.new_thing)
# print(Tombola.new_thing)
# result = tombola.get_cnp_from_user()

# tombola2 = Tombola()