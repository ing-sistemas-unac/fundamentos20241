"""
Crea un programa que lea 5 números para la lista1 y 5 números para la lista2. Luego, el programa debe crear una lista3 que almacene el producto de cada elemento de la lista 1 y la lista 2.
"""
# Leer los números de la lista 1
lista1 = []
for i in range(1,6):
    num = int(input(f"Ingrese el número {i}\t"))
    lista1.append(num)
# Leer los números de la lista 2
lista2 = []
for i in range(1,6):
    num = int(input(f"Ingrese el número {i}\t"))
    lista2.append(num)
# Calcular el producto de los números y guardarlo en la lista 3
lista3 = []
for i in range(0, 5):
    lista3.append(lista1[i]*lista2[i])
print(lista3)