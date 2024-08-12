#1.
##parola = input('introduceti parola: ')
##print('Parola introdusa este: ' , parola == 'Passme1n' )

#2.

nume1 = input("Introduceti un nume: ")
nume2 = input("Introduceti al doilea nume: ")
print("Lungimea primului nume este de",nume1.__len__() ,"caractere")
print(nume1==nume2)
print(nume1.__len__()>nume2.__len__())
print("Initiala primului nume este: ",nume1[0])
print("Primul nume inversat: ",nume1[::-1])

#3.

nr1 = input("Introduceti un numar: ")
print(nume1 * int(nr1))

#4.
sir1 = input("introduceti un sir: ")
print('\n'.join(sir1))


#5.
cuvant = input("Scrieti un cuvant: ")
print("Palindrom: ",cuvant==cuvant[::-1])

#6.
cuvant2 = input("introduceti un cuvant: ")
print(cuvant2[0]==cuvant2[0].upper())