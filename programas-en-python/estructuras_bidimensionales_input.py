notas_estudiantes = [[], [], []] # Creamos la matriz bidimensional
for i in range(0, 3): # Ciclo for para iterar en las filas
    print(f"Estudiante {i+1}") # Imprimir el número del estudiante
    for j in range(0, 3): # Ciclo for para iterar en los datos de las filas
        print(f"Ingrese la nota {j+1}") # Pedir la nota de cada estudiante
        nota = int(input())
        notas_estudiantes[i].append(nota) # Guardar la nota en la fila correspondiente
print(notas_estudiantes)
