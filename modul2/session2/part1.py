# string methods part2

result = len('My Text')
print(result)
print("My Text".__len__())

print('My Text {}'.format("example"))
print('My Text {} {}'.format("example", 'one'))
print('My Text {1} {0}'.format("example", 'one'))
print('My Text {text1} {text2}'.format(text1="example", text2='one'))

# len(100)
# (100).__len__()

# Slice of string
my_text = "Hello World"
          #012345678910

# index of char in string
print(my_text[0])

# range of indexes
print(my_text[0:3])

# step for slice
print(my_text[0:9:2])


