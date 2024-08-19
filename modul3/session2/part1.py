# functions

def function1(arg1, kwarg1="Default Text"):
    if arg1:
        print(arg1)
    else:
        print(kwarg1)
    my_new_var = 10  # cannot be accessed outside of function code block

print(function1)
function1("Example Text")
function1("")
function1("", kwarg1="New Value1")
function1("", "New Value2")
function1(arg1="", kwarg1="New Value3")

# print(args1)
# print(my_new_var)