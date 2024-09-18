class EnumeratorCuvant():
    def __init__(self, cuvant: str):
        self.cuvant = cuvant
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.cuvant:
            letter = self.cuvant[0]
            self.cuvant = self.cuvant[1:]
            index = self.i
            self.i = self.i + 1
            return (index, letter)
        else:
            raise StopIteration


for i, litera in EnumeratorCuvant("alfabet"):
    print(f"{i}: {litera}")
