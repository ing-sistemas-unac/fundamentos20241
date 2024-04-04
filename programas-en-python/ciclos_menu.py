while True:
    print("¡Bienvenido! Seleccione una opción: \n1. Saludar\n2. Despedirse\n0. Cerrar programa")
    opcion = int(input())
    if opcion == 1:
        print("Hola")
    elif opcion == 2:
        print("Adiós")
    elif opcion == 0:
        break
    else:
        print("Opción no válida")
    