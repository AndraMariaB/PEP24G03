"""
function to return warranty status of product presuming 3 yars warranty
"""
import datetime

products = {
    "product1": datetime.datetime(2020, 3, 10),
    "product2": datetime.datetime(2021, 2, 20),
    "product3": datetime.datetime(2022, 5, 30),

}


def get_warranty_expired(name: str) -> bool:
    product_expiration_date = products.get(name, None)
    if not product_expiration_date:
        return True
    # product_expiration_date._year = product_expiration_date.year + 3
    warranty = datetime.datetime(
        year=product_expiration_date.year + 3,
        month=product_expiration_date.month,
        day=product_expiration_date.day,
    )
    if datetime.datetime.now() < warranty:
        return False
    return True


if __name__ == '__main__':
    print(get_warranty_expired('product3'))
