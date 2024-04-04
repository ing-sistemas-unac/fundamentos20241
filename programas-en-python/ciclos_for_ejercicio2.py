"""
Cree un programa que cuente el número de vocales en una cadena ingresada por el usuario.
"""
# Pedir al usuario que ingrese un texto
print("Ingrese un texto para saber cuántas vocales tiene")
palabra = input().lower()

# Crear las variables para contar las vocales
cantidad_a = 0
cantidad_e = 0
cantidad_i = 0
cantidad_o = 0
cantidad_u = 0

# Definir el ciclo para recorrer las letras y evaluar si son vocales
for letra in palabra:
    if letra == "a":
        cantidad_a += 1
    elif letra == "e":
        cantidad_e += 1
    elif letra == "i":
        cantidad_i += 1
    elif letra == "o":
        cantidad_o += 1
    elif letra == "u":
        cantidad_u += 1
    else:
        pass # El pass es un skip o saltarse ese pedazo

# Imprimir los resultados
print(f"{palabra} tiene:")
print(f"{cantidad_a} vocales a")
print(f"{cantidad_e} vocales e")
print(f"{cantidad_i} vocales i")
print(f"{cantidad_o} vocales o")
print(f"{cantidad_u} vocales u")


    