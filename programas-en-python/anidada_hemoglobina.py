print("Vamos a indicarle si tiene anemia o no")
print("Ingrese su sexo")
sexo = input()
print("Ingrese su edad")
edad = int(input()) # edad en años 
print("Ingrese su hemoglobina")
hemoglobina = int(input())

# Clasificar por sexo 
if sexo.lower() == 'hombre' or sexo.lower() == 'mujer':
    # Clasificar por edad de 0.5 a 5 años
    if edad >= 0.5 and edad < 5:
        # Clasificar por hemoglobina para la edad de 0.5 a 5 años
        if hemoglobina >= 110:
            print("Sin anemia :)")
        elif hemoglobina >= 100 and hemoglobina <= 109:
            print("Tiene anemia leve")
        elif hemoglobina >= 70 and hemoglobina <= 99:
            print("Tiene anemia moderada")
        elif hemoglobina < 70 and hemoglobina >= 1:
            print("Tiene anemia grave :(")
        else: 
            print("Su hemoglobina no es válida")
    # Clasificar por edad de 5 a 11 años
    elif edad >= 5 and edad <= 11:
        # Clasificar por hemoglobina para la edad de 5 a 11 años
        if hemoglobina >= 115:
            print("Sin anemia :)")
        elif hemoglobina >= 110 and hemoglobina <= 114:
            print("Tiene anemia leve")
        elif hemoglobina >= 80 and hemoglobina <= 109:
            print("Tiene anemia moderada")
        elif hemoglobina < 80 and hemoglobina >= 1:
            print("Tiene anemia grave :(")
        else: 
            print("Su hemoglobina no es válida")
    # Clasificar por edad de 12 a 14 años
    elif edad >= 12 and edad <= 14:
        # Clasificar por hemoglobina para la edad de 12 a 14 años
        if hemoglobina >= 120:
            print("Sin anemia :)")
        elif hemoglobina >= 110 and hemoglobina <= 119:
            print("Tiene anemia leve")
        elif hemoglobina >= 80 and hemoglobina <= 109:
            print("Tiene anemia moderada")
        elif hemoglobina < 80 and hemoglobina >= 1:
            print("Tiene anemia grave :(")
        else: 
            print("Su hemoglobina no es válida")
    # Clasificar por edad mayor a 15 años
    elif edad >= 15:
        # Clasificar por sexo mujer
        if sexo.lower() == 'mujer':
            # Clasificar hemoglobina para mujer mayor de 15 años
            if hemoglobina >= 120:
                print("Sin anemia :)")
            elif hemoglobina >= 110 and hemoglobina <= 119:
                print("Tiene anemia leve")
            elif hemoglobina >= 80 and hemoglobina <= 109:
                print("Tiene anemia moderada")
            elif hemoglobina < 80 and hemoglobina >= 1:
                print("Tiene anemia grave :(")
            else: 
                print("Su hemoglobina no es válida")
        # Clasificar por sexo hombre
        elif sexo.lower() == 'hombre':
            # Clasificar hemoglobina para hombre mayor de 15 años
            if hemoglobina >= 130:
                print("Sin anemia :)")
            elif hemoglobina >= 110 and hemoglobina <= 129:
                print("Tiene anemia leve")
            elif hemoglobina >= 80 and hemoglobina <= 109:
                print("Tiene anemia moderada")
            elif hemoglobina < 80 and hemoglobina >= 1:
                print("Tiene anemia grave :(")
            else: 
                print("Su hemoglobina no es válida")      
        else: 
            print("El sexo no es válido") 
    else:
        print("La edad no es válida")
else:
    print("El sexo no es válido")