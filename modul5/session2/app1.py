STOCK = {"tomato": {"price": 1, "stock": 500}}

MENU = """
Meniu:
1. Vizualizare stoc
2. Adaugare produs
3. Stergere produs
4. Iesire
"""


def visualise_stock():
    for product, info in STOCK.items():
        print(80 * "#")
        print("product:", product)
        print("stock:", info["stock"])
        print("price:", info["price"])
        print(80 * "#")


def add_product():
    name, price, stock = input("give product details:[name,price,stock]:").split(',')
    info = STOCK.get(name, {})
    info.update({"price": int(price)})
    info.update({"stock": info.get("stock", 0) + int(stock)})
    STOCK[name] = info


def delete_product():
    name = input("give product name to delete: ")
    del STOCK[name]


action_map = {1: visualise_stock, 2: add_product, 3: delete_product, 4: quit}


def print_menu_and_get_selection():
    print(MENU)
    return int(input("select an option:"))


while True:

    user_option = print_menu_and_get_selection()
    if user_option not in action_map:
        break
    action_map[user_option]()
