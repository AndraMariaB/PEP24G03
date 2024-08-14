# Crate function for a shop selecter based on price

shop1 = {'apple': 100, "banana": 120, "orange": 95, "plums": 200}
shop2 = {'apple': 103, "banana": 122, "orange": 93, "pumpkins": 150}
shop3 = {'apple': 110, "banana": 110, "orange": 100}

shopping_cart = {'apple': 3, "banana": 4, "orange": 5}
shop_names = {"LIDL": shop1, "KAUF": shop2, "Auch": shop3}


def best_buy(items_to_by, shops) -> tuple[str, str]:
    return shop_name, cost


print(best_buy(shopping_cart, shop_names))
