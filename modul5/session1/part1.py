# from import_test import VAR2
import random

# random.randint(1, 49)
numbers = [_ for _ in range(1, 50)]
number = random.choice(numbers)
numbers.remove(number)
number = random.choice(numbers)
numbers.remove(number)
number = random.choice(numbers)
numbers.remove(number)

VAR1 = f"test_import {__name__}"
# NEW_VAR2 = VAR2 + "new text"

if __name__ == "__main__":
    print(VAR1)
    import math
    print(math.acosh(3))
