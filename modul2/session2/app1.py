text = input("Introduceti un sir: ")

text_length = len(text)
print("Lungimea sirului este: {}".format(text_length))

print(f"Lungimea sirului este: {text_length}")

print("Lungimea sirului este: " + str(text_length))

text_length = text.__len__()
print("Lungimea sirului este:", text_length)
