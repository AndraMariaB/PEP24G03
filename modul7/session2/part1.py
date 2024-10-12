# # lambda function
#
# my_function1 = lambda first_number, second_number: first_number + second_number
#
#
# def my_function2(first_number, second_number):
#     return first_number + second_number
#
#
# print("result f1", my_function1(2, 3))
#
# print("result f1", my_function2(2, 3))
#
# def calculate(func, *args, **kwargs):
#     return func(*args, **kwargs)
#
# print(calculate(my_function1, 2, 3))
# print(calculate(sum, (2, 3)))
# print(calculate(lambda first_number, second_number: first_number + second_number, 2, 3))
#
# # map function
#
# result = map(lambda obj: bool(obj), [0, 1, None, "", " ", 1.2, set()])
# print(type(result))
# print(result)
# print(list(result))
#
# # filter function
#
# result = filter(lambda obj: bool(obj), [0, 1, None, "", " ", 1.2, set()])
# print(type(result))
# print(result)
# print(list(result))
#
# # generator change
# my_var = [0, 1, None, "", " ", 1.2, set()]
# result = map(lambda obj: bool(obj), my_var)
# print(type(result))
# print(result)
# my_var.append("test")
# print(list(result))
#
# # my_var = [0, 1, None, "", " ", 1.2, set()]
# # result = map(lambda obj: obj, my_var)
# # for obj in result: # result is not final until it is iterated
# #     print(obj)
# #     my_var.insert(0, "example")

# datetime

import datetime

date1 = datetime.datetime(2020, 10, 15, 22, 30, 15)
date2 = datetime.datetime(2020, 10, 14, 20, 30, 15)
result = date1 - date2
print(type(result))
print(result)
print(datetime.datetime.now())

results = {}

while True:
    option = input('press key:')
    now = datetime.datetime.now()
    if option == "q":
        print(results)
        quit()
    results.update({option: now})


