while True:
    print("1.Cappucino...4lei")
    print("2.Espresso...3.5lei")
    option = int(input("Ce optiune alegeti? [1,2]: "))
    coin = int(input("Introduceti o bancnota [5,10]: "))
    pret = 0
    if coin != 5 and coin != 10:
        print("Bancnota Invalida")
        continue
    if option == 1:
        pret = 4
    elif option == 2:
        pret = 3.5
    print("Veti primi restul de {} leu".format(coin - pret))
    print("Produsul se livreaza ...")
