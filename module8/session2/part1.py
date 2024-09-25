file = open("my_file", "w")
file.write("Hello World\n")
file.flush()
file.close()

with open("my_file", "a") as file:
    file.write("add extra string")
