print("Plan para el domingo")
print("Ingrese la previsión del clima para el domingo: lluvia o sol")
clima = input()
print("Ingrese si hay dinero para salir: si o no")
dinero = input()
print("Ingrese si hay tarea: si o no")
tarea = input()
print("Ingrese si hay amigos para el parche: si o no")
amigos = input()
# Si hay lluvia no hay que salir
if clima == 'sol':
    # Si hay dinero se puede salir
    if dinero == 'si':
        # Si no hay tarea se puede salir
        if tarea == 'no': 
            # Si hay amigos para el parche se puede salir
            if amigos == 'si':
                print("Todo está a favor para salir")
            else: 
                print("Se sale solo y ya") 
        else:
            print("Se puede salir, se trasnocha y ya")
    else:
        print("Se puede salir, toca conseguir la plata")
else: 
    print("No vamos a salir, estará lloviendo")