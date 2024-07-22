# if / else condition
a = "Hello World"
# a = ""
# a = 1
# a = 0

if a:
    print(a)
else:
    print("Empty string provided")

print("This will always execute")

# check is number is between 10 and 20 or 30 and 40
number = int(input("give number: "))
if number > 10 and number < 20:
    print("Number is in range (10-20)")
elif number > 30 and number < 40:
    print("Number is in range (30-40)")
else:
    print("Number is not in expected range")
