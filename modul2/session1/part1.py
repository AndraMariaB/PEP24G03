# String data type
# definition
string_with_quotes1 = 'Hello\' World'
print(string_with_quotes1)
string_with_quotes2 = "Hello\" World"
print(string_with_quotes2)
string_with_quote3 = """Hello " '
 World"""
print(string_with_quote3)

# string methods

count = string_with_quotes1.count("l")
print(count)
centered = string_with_quotes1.center(30, "#")
print(centered)
added = string_with_quotes1 + string_with_quotes2
print(added)


# Integer data type
# definition
number1 = 100000
number2 = 100_000
print(number2)

# int methods

result1 = number1.bit_length()
print(result1)

result2 = (number1 + number2) * 2
print(result2)

result3 = number1.__add__(number2)
print(result3)

# Float data type
# definition

float1 = 10.23
float2 = 10.30

# float type
print(type(float1))
print(type(float2))

# float methods
result = float1 > float2
print(result)
print(type(result))

# Bool data type
# definition
true = True
false = False

result_bool1 = not true
print(result_bool1)

result_bool2 = true and false
print(result_bool2)

result_bool2 = true or false
print(result_bool2)

# Input function
user_input = input("Give name: ")  # interacts with stdin
print("User provided input:", user_input)
