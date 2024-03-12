print("Ingrese la escala en la que desea trabajar: 1. Kelvin 2. Celsius 3. Farenheith")
escala = int(input())
print("Ingrese la temperatura que desea convertir. Puede ingresar decimales")
temperatura = float(input())
if escala == 1:
    farenheith = (temperatura - 273.15) *(9/5) + 32
    celsius = temperatura - 273.15
    print(f"{temperatura} Kelvin a Farenheith es {farenheith} y a Celsius es {celsius}")
elif escala == 2:
    print()
elif escala == 3:
    print()
else:
    print("No ingresó una temperatura válida")