sexo = input("¿Eres hombre o mujer? ")
edad = int(input("¿Cuántos años do you have? "))
peso = float(input("¿Cuánto pesas.. jummm quien sabe que le pase al cohete con tu peso? (en kg)"))
estatura = float(input("¿Cuánto mides?Me gustan mas las bajitas ahi como dato (en metros) "))

imc = peso / (estatura ** 2)

if edad < 18 or (sexo == 'mujer' and edad > 60) or (sexo == 'hombre' and edad > 65) or imc > 25:
    print("Sorry, ERROR 404.. No apto para la exploración espacial")
else:
    if 18 <= edad <= 25:
        if imc < 18.5:
            print("Costo de la exploración espacial: 50.000 USD")
        else:
            print("Costo de la exploración espacial: 45.000 USD")
    elif 26 <= edad <= 35:
        if imc < 18.5:
            print("Costo de la exploración espacial: 47.000 USD")
        else:
            print("Costo de la exploración espacial: 40.000 USD")
    elif 36 <= edad <= 50:
        if imc < 18.5:
            print("Costo de la exploración espacial: 53.000 USD")
        else:
            print("Costo de la exploración espacial: 55.000 USD")
    else:
        if imc < 18.5:
            print("Costo de la exploración espacial: 67.000 USD")
        else:
            print("Costo de la exploración espacial: 60.000 USD")
