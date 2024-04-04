"""
Cree un programa que imprima todos los números pares en un rango que el usuario determine.
"""

print("Ingrese el número inicial")
num_init = int(input())
print("Ingrese el número final")
num_fin = int(input())

for num in range(num_init, num_fin):
    if num % 2 == 0:
        print(num)
    else:
        pass