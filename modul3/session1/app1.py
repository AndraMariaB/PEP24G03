cnp = input('Introdu te rog CNP: ')
first_number = int(cnp[0])
if first_number >= 1 and first_number <= 2:
    century = 1900
elif first_number >= 5 and first_number <= 6:
    century = 2000
else:
    century = 1800
print(century)
year = int(cnp[1:3])
print(year + century)
age = 2024 - (year + century)
if age > 18:
    print("Aveti peste 18 ani")
else:
    print("NU Aveti peste 18 ani")
