print('Ingrese el año para saber si es bisiesto o no')
year = int(input())
if year % 4 == 0: 
    if year % 100 == 0:
        if year % 400 == 0:
            print("El año es un año bisiesto (tiene 366 días)")
        else:
            print("El año no es un año bisiesto (tiene 365 días)")
    else: 
        print("El año es un año bisiesto (tiene 366 días)")
else:
    print("El año no es un año bisiesto (tiene 365 días)")


"""
Si el año es divisible por 4, vaya al paso 2. De lo contrario, vaya al paso 5.
Si el año es divisible por 100, vaya al paso 3. De lo contrario, vaya al paso 4.
Si el año es divisible por 400, vaya al paso 4. De lo contrario, vaya al paso 5.
El año es un año bisiesto (tiene 366 días).
El año no es un año bisiesto (tiene 365 días).
"""