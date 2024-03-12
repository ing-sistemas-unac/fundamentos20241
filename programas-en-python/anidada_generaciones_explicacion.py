print('Ingrese su año de nacimiento para saber a qué generación pertenece y su ciclo vital')
nacimiento = int(input())
print('Ingrese su sexo para que la atención sea más personalizada')
sexo = input()

# Clasificar el sexo
if sexo.lower() == 'hombre':
    print("Usted es un hombre")

    # Clasificar la generación
    if nacimiento >= 1969 and nacimiento <= 1980:
        print('Generación X')

    elif nacimiento >= 1981 and nacimiento <= 1993:
        print('Millenials')
    
    elif nacimiento >= 1994 and nacimiento <= 2010:
        print('Generación Z')
    
    elif nacimiento >= 2011:
        print('Alfa')

    else:
        print('Su edad no aplica para una generación')

elif sexo.lower() == 'mujer':
    print("Usted es una mujer")

    # Clasificar la generación

    if nacimiento >= 1969 and nacimiento <= 1980:
        print('Generación X')

    elif nacimiento >= 1981 and nacimiento <= 1993:
        print('Millenials')
    
    elif nacimiento >= 1994 and nacimiento <= 2010:
        print('Generación Z')
    
    elif nacimiento >= 2011:
        print('Alfa')

    else:
        print('Su edad no aplica para una generación')

else:
    print("El sexo no es correcto. Por favor intente nuevamente")
