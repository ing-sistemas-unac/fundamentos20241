"""
Calcular la suma y producto de dos números que introduce el usuario

Pseudocódigo
Algoritmo suma_producto_numeros
	Definir num1, num2, suma, producto Como Real
	Escribir 'Ingrese el número 1'
	Leer num1
	Escribir 'Ingrese el número 2'
	Leer num2
	suma <- num1+num2
	producto <- num1*num2
	Escribir 'La suma de los números es ', suma, ' y el producto de los números es ', producto
FinAlgoritmo
"""
num1 = int(input("Ingrese el número 1\t")) # int() convierte lo que está adentro en un entero
num2 = int(input("Ingrese el número 2\t")) # si ingreso en la consola un decimal, el programa dará error
suma = num1+num2
producto = num1*num2
print(f"La suma de los números es {suma} y el producto de los números es {producto}") # usamos la f antes del string para indicar que daremos formato y así se podrán usar las llaves {} para llamar a las variables