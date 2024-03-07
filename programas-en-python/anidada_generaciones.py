print('Ingrese su año de nacimiento para saber a qué generación pertenece y su ciclo vital')
birth_year = int(input())
print('Ingrese su sexo para que la atención sea más personalizada')
sexo = input()

# Clasificar el sexo
if sexo.lower() == 'hombre':
    print('Hola bro')
    
    # Clasificar la generación
    if birth_year >= 1969 and birth_year <= 1980:
        print('Generación X')

    elif birth_year >= 1981 and birth_year <= 1993:
        print('Millenials')

    elif birth_year >= 1994 and birth_year <= 2010:
        print('Generación Z')
        # Clasificar su ciclo vital 
        edad = 2024 - birth_year
        if edad == 30:
            print('Usted es casi un adulto mayor')
        elif edad < 30 and edad > 20:
            print('Usted es un adulto joven')
        else:
            print('Usted es un joven')

    elif birth_year >= 2011:
        print('Alfa')
    else:
        print('Su edad no aplica para una generación')

elif sexo.lower() == 'mujer':
    print('Hola, que bueno que nos visites')
    # Clasificar la generación
    if birth_year >= 1969 and birth_year <= 1980:
        print('Tú perteneces a la Generación X')
    elif birth_year >= 1981 and birth_year <= 1993:
        print('Tú perteneces a la Millenials')
    elif birth_year >= 1994 and birth_year <= 2010:
        print('Tú perteneces a la Generación Z')
    elif birth_year >= 2011:
        print('Tú perteneces a la generación Alfa')
    else:
        print('Lo siento, tu edad no aplica para una generación')
else:
    print('El sexo no está dentro de las opciones disponibles')