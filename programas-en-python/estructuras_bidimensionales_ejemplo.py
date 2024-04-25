# [Moto o carro, marca, modelo, cilindraje, color, ¿es nuevo?]
concesionario = [["Moto", "Yamaha", 2018, 150, "azul", True], ["Moto", "Honda", 2019, 200, "rojo", False], ["Moto", "Suzuki", 2020, 125, "negro", True], ["Carro", "BMW", 2024, 400, "blanco", True], ["Carro", "Lamborgini", 2025, 750, "negro", True], ["Carro", "Chevrolet", 2010, 200, "azul", False]]

# Imprimir lista completa sin formato
print("Concesionario =",concesionario,"\n")
titulos = ["Tipo", "Marca", "Modelo", "Cilindraje", "Color", "¿Es nuevo"]
for titulo in titulos: # Imprimir cada título con el formato de espacios
    espacio = " " # Espacio en blanco para repetirlo en la siguiente línea
    restante = espacio * (10-len(str(titulo))) # Cálculo de los espacios necesarios para formatear la columna
    print(f"| {titulo}{restante}", end=" ")
print("|", end="") # Barra al final de la fila
print() # Salto de línea al terminar la fila
    
print("-"*79) # Línea que divide los títulos de los datos

# Usar el ciclo for anidado para mostrar la matriz
for fila in concesionario: # for para recorrer las filas
    for dato in fila: # for para recorrer las columnas o datos de la fila actual
        espacio = " "
        restante = espacio * (10-len(str(dato)))
        print(f"| {dato}{restante}", end=" ") # Imprimir cada dato de forma horizontal
    print("|", end="")
    print() # print vacío para hacer el salto de línea

print()
# Mostrar los datos de la tabla usando solo un ciclo for
for i in range(len(concesionario)):
    print(f"Tipo = {concesionario[i][0]},  Marca = {concesionario[i][1]}, Modelo = {concesionario[i][2]}, Cilindraje = {concesionario[i][3]}, Color = {concesionario[i][4]}, ¿Es nuevo? = {concesionario[i][5]}")

print()
# Mostrar los datos de la tabla usando dos ciclos for con enumerate
for i, fila in enumerate(concesionario): # Ciclo externo para iterar en las filas
    for j, dato in enumerate(fila): # Ciclo interno para iterar en los datos de cada fila
        print(f"[{i}][{j}] = {dato}", end=" ")
    print()

