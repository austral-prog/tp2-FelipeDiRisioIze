def change():
    expense = 23.75
    money = 100
    change = money - expense

    pesos = int(change)
    centavos = int((change * 100) - (pesos * 100))

    print("\nVuelto\n")
    print("Pesos:")
    print(pesos)
    print("Centavos")
    print(centavos)

