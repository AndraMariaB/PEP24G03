"""
function to return warranty status of product presuming 3 yars warranty
"""
import datetime

products = {
    "product1": datetime.datetime(2020, 3, 10),
    "product2": datetime.datetime(2021, 2, 20),
    "product3": datetime.datetime(2022, 5, 30),

}

def get_warranty(name: str) -> bool:
    pass