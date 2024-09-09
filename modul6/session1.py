class Animal(object):
    __generic = True

    def __init__(self):
        print("in Animal")

class Dog(Animal):
    color = "brown"

    def __init__(self):
        super().__init__()
        print("in Dog")

    def print_generic(self):
        print(self._Animal__generic)

    def __str__(self):
        return f"{self.__class__.__name__}_{self.color}"



dog = Dog()
dog.print_generic()
print(dog)


