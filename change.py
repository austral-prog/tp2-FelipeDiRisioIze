def change():
    expense = 23.75
    money = 100
    change = money - expense

    pesos = int(change)
    centavos = int((change * 100) - (pesos * 100))

    print("Ingresar gasto:")
    print(expense)
    print("Dinero recibido")
    print(money)
    print("\nVuelto\n")
    print("Pesos:")
    print(pesos)
    print("Centavos:")
    print(centavos)

