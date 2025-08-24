# Ejercicio 1
first_name = "AdA"
last_name  = "LoVeLAce"
name = f"{first_name} {last_name}"

print(name.lower())
print(name.title())
print(name.upper())
print("\t" + name.lower())

# Ejercicio 2
X = "Bangladesh"
Y = "Barbados"

print(f"The result of {X} comes first in the dictionary than {Y} is {X<Y}.")
print(f"The result of {Y} comes first in the dictionary than {X} is {Y<X}.")

# Ejercicio 3
gasto = float(input("Ingresar gasto:\n"))
pagado = float(input("Dinero recibido\n"))
vuelto = pagado - gasto

pesos = int(vuelto)
centavos = int((vuelto * 100) - (pesos * 100))

print("\nVuelto\n")
print("Pesos:")
print(pesos)
print("Centavos")
print(centavos)

