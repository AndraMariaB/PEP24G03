string1 = "Hello Python"
string2 = "Ana are mere"
string3 = "Pizza Party"

rejoin1 = "_".join(string1.split())
rejoin2 = "_".join(string2.split())
rejoin3 = "_".join(string3.split())

print(rejoin1)
print(rejoin2)
print(rejoin3)

string1 = string1 + "."
string2 = string2 + "."
string3 = string3 + "."

print(string1)
print(string2)
print(string3)

words1 = string1.split()
words2 = string2.split()
words3 = string3.split()

print(4 * (words1[0] + " ") + ' '. join(words1[1:]))
print(4 * (words2[0] + " ") + ' '. join(words2[1:]))
print(4 * (words3[0] + " ") + ' '. join(words3[1:]))

