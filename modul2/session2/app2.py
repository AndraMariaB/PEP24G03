print("/-\\ ".center(9))
print("// _ \\\\ ".center(9))
print("-------".center(9))
print("\\\\ _ // ".center(9))
print("\\-/ ".center(9))

print((4 * '-').center(9, " "))
print('/ \\'.center(9, " "))
print('/_______\\'.center(9, " "))

size = 20
for i in range(1, size, 2):
    print((i * '*').center(size + 2, " "))
