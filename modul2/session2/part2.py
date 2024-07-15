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