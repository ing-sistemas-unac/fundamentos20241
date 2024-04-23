# Creación de una tupla. Se crea con paréntesis y puede almacenar datos heterogéneos
nums_primos = (2, 3, 5, 7, 11, 13, 17, 19)
# Identificar el tipo de dato de ejemplo_tupla
print(type(nums_primos))
# Imprimir la tupla
print(nums_primos)
# Acceder a un elemento de una tupla
print("Elemento en la posición 0 =", nums_primos[0])
# Extraer los elementos de la tupla en variables
num1, num2, num3, num4, num5, num6, num7, num8 = nums_primos
print("Variable num1 =", num1) # num1 = nums_primos[0]
print("Variable num2 =", num2) # num2 = nums_primos[1]
print("Variable num8 =", num8) # num8 = nums_primos[7]
# Acceder a un rango de elementos de un arreglo
print("[2:6]", nums_primos[2:6])
print("[:2]", nums_primos[:2])
print("[2:]", nums_primos[2:])