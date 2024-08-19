# # dictionary
#
# my_dict1 = {}  # empty dict
# my_dict2 = {"key1": 1, True: 2, 3: "3"}  # , [2]: 4, [2]: 5} # lists cannot be keys
# # dict methods
# my_dict1.update({1: 1})
# print(my_dict1)
# my_dict1.update({1: 2, 2: 2})
# print(my_dict1)
#
# print(my_dict2.keys())
# for key in my_dict2.keys():
#     print(f"key is: {key}")
# for value in my_dict2.values():
#     print(f"value is: {value}")
# for item in my_dict2.items():
#     print(f"item is: {item}")
# for key, value in my_dict2.items():
#     print(f"key is: {key}, value is: {value}")
#
# # mutable
# print(my_dict2.get(True))
# print(my_dict2)
# print(id(my_dict2))
# print(my_dict2.pop(True))
# print(my_dict2)
# print(id(my_dict2))
#
# # a, b, c = (1, 2, 3)
# # print(a)
# # print(b)
# # print(c)
#
# # recusivitate


result = 7
def factorial1(n):
    result = 1
    for number in range(1, n + 1):
        result *= number
    return result


result2 = factorial1(3)
print(result2)
print(result)

# test = 5
def factorial2(n):
    if n == 1:
        return 1
    # global test
    # test = n
    return n * factorial2(n-1)

print(factorial2(1000))

