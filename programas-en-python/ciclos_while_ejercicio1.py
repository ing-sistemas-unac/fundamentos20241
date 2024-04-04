"""
Cree un programa que imprima un contador regresivo desde 5 hasta 1.
"""
# Crear la variable para iterar en el ciclo
contador = 5
# Crear el ciclo usando la estructura while
while contador >= 1:
    if contador == 1:
        print(contador, end=".")
    else:
        print(contador, end=", ")
    contador = contador - 1
else:
    print("\nSe imprimieron los números de 5 hasta 1. Adiós")
