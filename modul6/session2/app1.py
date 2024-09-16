MENIU_1 = '''
Welcome
1.Categoii
2.Produse
3.Iesire
'''
HEADER1 = f"{80 * '='}\n{" CATEGORII ".center(80, '=')}\n{80 * '='}"


class Magazin():

    def run(self):
        while True:
            print(MENIU_1)

            option = int(input("Alegeti optiunea: "))
            if option == 3:
                quit()
            # Execute other options
            elif option == 1:
                self.category()
            elif option == 2:
                self.products()

    def category(self):
        print(HEADER1)

    def products(self):
        pass


MAG = Magazin()
MAG.run()
