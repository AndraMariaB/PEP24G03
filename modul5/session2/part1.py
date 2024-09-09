class Shop:
    stock = {'test': 123}
    color = "red"

    # pass
    def add_product(self):
        # print(id(self) # id of self is the same with id of "s"
        name, price, stock = input("give product details:[name,price,stock]:").split(',')
        info = self.stock.get(name, {})
        info.update({"price": int(price)})
        info.update({"stock": info.get("stock", 0) + int(stock)})
        self.stock[name] = info
        self.color = "blue"
        return "done"

# Shop.stock
s = Shop()
# s.stock
print(type(s))
print(id(s))
print(Shop.color)
print(s.color)
# print(Shop.add_product(Shop))
print(s.add_product())
# print(s.stock)
# print(id(s.stock), "memory location of instance variable stock")
# print(Shop.stock)
# print(id(Shop.stock), "memory location of Class variable stock")

# var1 = "Text"
# print(id(var1))
# var1 = "Text".lower()
# print(id(var1))
#
# var2 = []
# print(id(var2))
# var2.append(1)
# print(id(var2))

