"""
Crea un programa que lea 5 edades y las almacene en un arreglo. El programa debe mostrar el promedio de las edades.
"""
# Colorama para dar color al texto en la consola
from colorama import init, Fore
init() # Inicializar colorama
print(Fore.BLUE)
# Crear un arreglo/array/vector para almacenar las edades
edades = []
# Crear un ciclo para pedir las 5 edades
for i in range(0, 5): # Rango de 0 a 5 porque el 5 no lo toma
    edad = int(input("Ingresa una edad:\t")) # \t da un espacio de tabulación, es decir, 4 espacios en blanco
    edades.append(edad) # Guardar la edad en el arreglo de edades
# Imprimir el arreglo de edades
print(Fore.GREEN,"Edades =" , edades)
# Usar un ciclo for para sacar las edades del arreglo y poder hacer el cálculo del promedio
suma_edades = 0 # Variables para guardar la suma de todas las edades
for edad in edades:
    suma_edades += edad # Almacena la edad en la variable suma_edades
# Calcular el promedio
promedio_edades = suma_edades/len(edades) # len() calcula la cantidad de elemetos que tiene el arreglo
print(Fore.MAGENTA + f"Promedio edades = {promedio_edades}")