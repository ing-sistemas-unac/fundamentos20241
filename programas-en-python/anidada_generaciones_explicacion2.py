print('Ingrese su año de nacimiento para saber a qué generación pertenece y su ciclo vital')
nacimiento = int(input())
print('Ingrese su sexo para que la atención sea más personalizada')
sexo = input()

# Clasificar la generación
if nacimiento >= 1969 and nacimiento <= 1980:
    if sexo.lower() == 'hombre':
        print("Usted es un hombre")
    elif sexo.lower() == 'mujer':
        print("Usted es una mujer")
    else: 
        print("El sexo no es correcto. Por favor intente nuevamente")
    print('Generación X')

elif nacimiento >= 1981 and nacimiento <= 1993:
    print('Millenials')
    if sexo.lower() == 'hombre':
        print("Usted es un hombre")
    elif sexo.lower() == 'mujer':
        print("Usted es una mujer")
    else: 
        print("El sexo no es correcto. Por favor intente nuevamente")
    # Clasificar su ciclo vital 
    edad = 2024 - nacimiento
    if edad == 30:
        print('Usted es casi un adulto mayor')
    elif edad < 30 and edad > 20:
        print('Usted es un adulto joven')
    else:
        print('Usted es un joven')

elif nacimiento >= 1994 and nacimiento <= 2010:
    print('Generación Z')

elif nacimiento >= 2011:
    print('Alfa')

else:
    print('Su edad no aplica para una generación')