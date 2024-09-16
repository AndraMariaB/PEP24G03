MENIU_1 = '''
Welcome
1.Categoii
2.Produse
3.Iesire
'''
HEADER1 = f"{80 * '='}\n{" CATEGORII ".center(80, '=')}\n{80 * '='}"


class Products:
    name: str = None
    price: int = None
    stock: int = None

    def __init__(self, name: str, price: int, stock: int):
        self.name = name
        self.price = price
        self.stock = stock

    def return_category(self):
        return f"{self.__class__.__name__}"


class Haine(Products):
    pass


class Accesorii(Products):
    pass


class Magazin():

    def __init__(self):
        self.stock = []
        self.stock.append(Haine(name="bluza", price=50, stock=500))

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
        categories = set()
        for product in self.stock:
            categories.add(product.return_category())
        for cat in categories:
            print("--- ", cat)

    def products(self):
        pass


MAG = Magazin()
MAG.run()
