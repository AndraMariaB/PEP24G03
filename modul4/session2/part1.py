# Exceptions

divider = [3]
# if divider:
#     number = 100/divider
# else:
#     print("Infinite")

try:
    number = 100 / divider
    # raise RuntimeError("Custom Error")
    # raise SystemExit
    # raise BaseException
    # print("No Errors")
except ZeroDivisionError:
    print("Infinite")
except TypeError:
    print("Wrong divider type")
except Exception:
    print("Something happened")
else:
    print("This is only executed is no errors encountered")