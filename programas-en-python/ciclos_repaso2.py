opcion = -1
while opcion != 0:
    print("Bienvenido. Seleccione una opción: 1. Decir hola 2. Dar bendición 0. Salir")
    opcion = int(input())
    if opcion == 1:
        print("Hola")
    elif opcion == 2: 
        print("Dios lo bendiga")
    elif opcion == 0:
        pass
    else:
        print("Opción inválida, intente nuevamente")