# casting

my_str1 = str(100)
print(type(my_str1), my_str1)
my_str2 = str(True)
print(type(my_str2), my_str2)
my_str3 = str(None)
print(type(my_str3), my_str3)

my_int1 = int("100")
print(type(my_int1), my_int1)
my_int2 = int(True)
print(type(my_int2), my_int2)
my_int3 = int(10.6)
print(type(my_int3), my_int3)

print(float(90))
print(float("90"))
print(float(False))

print("Object 10 is:", bool(10))
print("Object 0.0 is:", bool(0.0))
print("Object 'a' is:", bool('a'))
print("Object '' is:", bool(''))
print("Object None is:", bool(None))
