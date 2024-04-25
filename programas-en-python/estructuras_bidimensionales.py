notas_estudiantes = [[77, 68, 86, 73], [96, 87, 89, 81], [70, 90, 86, 81]]
# Cada fila pertenece a un estudiante
print(notas_estudiantes)
# Ciclo for para recorrer las filas del arreglo
for fila in notas_estudiantes: # fila es el nombre de la variable para el ciclo for
    # Ciclo for para recorrer las columnas de cada fila
    for item_col in fila: # item_col es el nombre de la variable para el ciclo for 
        # Este print lleva el end para que se muestren todos los elementos de la columna de forma horizontal
        print(f"|{item_col}", end="")
    # Este print hace el salto de línea al finalizar los elementos de cada fila
    print("|", end="")
    print()
for i in range(len(notas_estudiantes)): # fila es el nombre de la variable para el ciclo for
    # Ciclo for para recorrer las columnas de cada fila
    print(f"Nota1 = {notas_estudiantes[i][0]} Nota2 = {notas_estudiantes[i][1]}")

