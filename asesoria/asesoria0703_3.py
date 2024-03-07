"""
Algoritmo identificar_triangulos
    Leer lado1
    Leer lado2
    Leer lado3
    Crear condición para saber si es equilátero
    Crear condición para saber si es equilátero
    Crear condición para saber si es escaleno
    Imprimir cuál condición cumple
FinAlgoritmo
"""

print('Ingrese el lado 1')
lado1 = int(input())
print('Ingrese el lado 2')
lado2 = int(input())
print('Ingrese el lado 3')
lado3 = int(input())
# Equilátero
if lado1 == lado2 == lado3:
    print('El triángulo es equilátero')
elif lado1 == lado2 != lado3 or lado1 == lado3 != lado2 or lado2 == lado3 != lado1:
    print('El triángulo es isósceles')
else:
    print('El triángulo es escaleno')