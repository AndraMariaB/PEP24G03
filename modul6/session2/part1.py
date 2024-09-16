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


cats = []
tricouri = Haine('tricou', 100, 100)
cats.append(tricouri)
cercei = Accesorii('cercei', 20, 10)
cats.append(cercei)

for cat in cats:
    print(cat.return_category())
