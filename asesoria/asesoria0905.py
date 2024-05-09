arreglo = [9, 3, 5, -1, 8]

for elemento in arreglo:
    print(elemento, end=" ")
print()

for i in range(0, 5):
    print(arreglo[i], end= " ")

arreglo2d = [[1, 2, 3, 6, 3, -1], [3, 4, 8, 9, 1, 21], [2, 3, 6, 3, -1, 7], [2, 3, 6, 3, 5, 8]]

for fila in arreglo2d:
    for col in fila:
        print(col, end=" ")
    print()
print()

for f in range(len(arreglo2d)):
    for c in range(len(arreglo2d[f])):
        print(arreglo2d[f][c], end=" ")
    print()

for f in range(len(arreglo2d)):
    print(arreglo2d[f][3], end=" ")