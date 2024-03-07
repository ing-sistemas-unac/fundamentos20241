"""a = "Hola" # Definir una variable
b = 3
print("Ingresa tu nombre para decirte hola") # Print se usa para imprimir
nombre = input() # Input se usa para recibir un texto por teclado
print(f"{a * b} {nombre}")"""

# print("Ingrese el valor en pesos colombianos") # El print es como Escribir en PSeInt
pesos_colombianos = int(input("Ingrese el valor en pesos colombianos y debe ser un entero\t")) # El input es como Leer en PSeInt
dolar_estadounidense = pesos_colombianos/4000
euro = pesos_colombianos/4260
print(f"{dolar_estadounidense} dólares")
print(str(euro) + " euros")