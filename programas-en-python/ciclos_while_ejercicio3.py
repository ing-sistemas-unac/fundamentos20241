"""
Cree un programa que seleccione un número aleatorio y pida al usuario que ingrese un número hasta que  adivine el número elegido por el programa.
"""
# Importar la librería random para generar números aleatorios
import random 
# Crear un número aleatorio entero con randint 
numero_aleatorio = random.randint(0, 100)
# Crear el ciclo para pedir números al usuario
while True:
    # Pedir el número al usuario
    numero_usuario = int(input("Ingrese un número entre 0 y 100 -> "))
    # Comparar los dos números
    if numero_usuario >= 0 and numero_usuario <= 100:
        if numero_usuario == numero_aleatorio:
            print("Felicitaciones :) has adivinado")
            break
        elif numero_usuario > numero_aleatorio: 
            print("Sigue intentando. PISTA: El número es menor que el que acabas de ingresar... ")
        elif numero_usuario < numero_aleatorio:
            print("Sigue intentando. PISTA: El número es mayor que el que acabas de ingresar...")
        else:
            print()
    else:
        print("Debe ingresar un número entre 0 y 100")
