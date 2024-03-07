print("Ingrese un número para saber si positivo o negativo y si es par o impar")
numero = int(input())
# Evaluar si el número es positivo, negativo o cero
if numero > 0:
    print("El número es mayor que cero")
    # Evaluar si el número es par
    if numero % 2 == 0:
        print("El número es par")
    else:
        print("El número es impar")
elif numero < 0: 
    print("El número es menor que cero")
    # Evaluar si el número es par
    if numero % 2 == 0:
        print("El número es par")
    else:
        print("El número es impar")
else: 
    print("El número es cero")