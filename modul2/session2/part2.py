# advanced methods

my_str = """ multi word string 
this is the second line
"""
words = my_str.split()
print(words)
print(type(words))

print(words[::-1])  # reverses list just like string

rejoin = " # ".join(words)
print(rejoin)

rejoin_string = " ! ".join('''Hello World''')
print(rejoin_string)

# object id

var1 = 1
print(id(var1))

var2 = 3_000_000  # try with 30
print(id(var2))

var3 = 3_000_001  # try with 31
print(id(var3))

print("Some random code executed")

result = var1 + var2
print(id(result))

print("Numbers are equal: ", result == var3)

# keyword "in"

a = "text1ABC"
b = "AB"
print(b in a)

a = ['one', 'two']
b = 'one'
c = 'on'
print(b in a)
print(c in a)
