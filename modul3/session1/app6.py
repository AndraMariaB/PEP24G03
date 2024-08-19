word = input("give word: ")
first_letter = word[0]
nr = 0
for letter in word:
    if first_letter == letter:
        nr = nr + 1
print(first_letter, "apare de ", nr, "ori")
