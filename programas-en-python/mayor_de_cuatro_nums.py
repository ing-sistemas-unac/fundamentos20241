# Pedimos los números al usuario
num1 = int(input("Ingrese el número 1\n"))
num2 = int(input("Ingrese el número 2\n"))
num3 = int(input("Ingrese el número 3\n"))
num4 = int(input("Ingrese el número 4\n"))

# Crear las variables para guardar el número mayor y el número menor
num_mayor = num1
num_menor = num2

# Creamos las condiciones para actualizar las variables 
if num2 > num_mayor:
    num_mayor = num2
if num3 > num_mayor:
    num_mayor = num3
if num4 > num_mayor:
    num_mayor = num4

if num1 < num_menor:
    num_menor = num1
if num3 < num_menor:
    num_menor = num3
if num4 < num_menor:
    num_menor = num4

print(f"El número mayor es {num_mayor}")