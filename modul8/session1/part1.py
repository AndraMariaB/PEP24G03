import time

my_list = [1, 2, 3, 4]
# my_list = 'abcd'

for nr in my_list:  # my_list is iterable
    print(nr)

# steps for for loop
list_iterator = my_list.__iter__()
print(type(list_iterator))
print(list_iterator.__next__())
print(list_iterator.__next__())
print(list_iterator.__next__())
print(list_iterator.__next__())
# print(list_iterator.__next__())  # list_iterator is empty (consumed)

print(id(list_iterator))
print(id(list_iterator.__iter__()))


class MyCars:
    cars = {1: "Logan"}

    def __iter__(self):
        return MyCarsIterator(self.cars)

    def add_car(self, index: int, name: str):
        self.cars.update({index: name})


class MyCarsIterator:

    def __init__(self, cars: dict):
        self.cars = cars

    def __iter__(self):
        return self

    def __next__(self):
        for index in self.cars:
            name = self.cars.pop(index)
            time.sleep(1)
            return f'{index}:{name}'
        raise StopIteration


o = MyCars()
o.add_car(2, "BMW")

for element in o:
    print(element)
