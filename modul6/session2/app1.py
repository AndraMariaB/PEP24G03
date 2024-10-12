from modul6.session2.part1 import Haine, Accesorii

MENIU_1 = '''
Welcome
1.Categoii
2.Produse
3.Iesire
'''
MENIU_2 = '''
1.Adaugare
2.Vizualizare
3.Iesire la meniul principal
'''
HEADER1 = f"{80 * '='}\n{' CATEGORII '.center(80, '=')}\n{80 * '='}"
HEADER2 = f"{' PRODUSE '.center(80, '=')}\n{80 * '='}"
CLASS_MAPPING = {
    'haine': Haine,
    'accesorii': Accesorii,
}


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
        while True:
            print(HEADER2)
            print(MENIU_2)
            option = int(input("Introduceti optiunea: "))
            if option == 3:
                return
            elif option == 1:
                self.add_product()
            elif option == 2:
                self.view_product()

    def add_product(self):
        while True:
            category_class = input("Introduceti numele categoriei: ")
            if category_class not in CLASS_MAPPING:
                continue
            nume_produs = input("Introduceti numele produsului: ")
            if not nume_produs.isalnum():
                continue
            pret_produs = input("Introduceti pretul produsului: ")
            if not pret_produs.isnumeric():
                continue
            stock_produs = input("Introduceti stocul produsului: ")
            if not stock_produs.isnumeric():
                continue
            self.stock.append(CLASS_MAPPING[category_class](nume_produs, int(pret_produs), int(stock_produs)))
            return

    def view_product(self):
        self.stock.sort(key=sort_categories)
        category_change = ""
        for product in self.stock:
            if category_change != product.__class__.__name__:
                print("print a category")  # HOMEWORK!!!
                category_change = product.__class__.__name__
            print(f"nume:{product.name}")
            print(f"price:{product.price}")
            print(f"stock:{product.stock}")
            print(f"{80 * '-'}")


def sort_categories(product: Products):
    return product.__class__.__name__


MAG = Magazin()
MAG.run()
