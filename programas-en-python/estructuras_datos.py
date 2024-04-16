# Array de frutas
frutas = ["banano", "manzana", "pera", "melón", "mango"]
print("frutas =", frutas)
# Crea una copia de la lista original
copia_frutas = frutas.copy()
# Añade un nuevo elemento a la lista
copia_frutas.append("fresa")
# Imprime la lista 
print("copia =", copia_frutas)
# Elimina todos los elementos de la lista
# copia_frutas.clear()
# Imprime la lista 
print("copia =", copia_frutas)
print("frutas =", frutas)
# Añadir una manzana
copia_frutas.append("manzana")
# Contar cuántas manzanas hay en la copia
print("# de manzanas = ", copia_frutas.count("manzana"))
# Añadir las frutas de la copia al array original
frutas.extend(copia_frutas)
print("frutas =", frutas)
# Contar cuántas manzanas hay en el arreglo original
print("# de manzanas = ", frutas.count("manzana"))
# Ordena los elementos de la lista en orden alfabético A-Z
copia_frutas.sort()
print("frutas ordenadas =", copia_frutas)
# Ordena los elementos de la lista en orden alfabético invertido Z-A
copia_frutas.sort(reverse=True)
print("frutas ordenadas =", copia_frutas)

# Array de notas
notas = [5, 1.5, 3, 2, 1, 1, 4, 3, 2, 1]
print("notas =", notas)
# Eliminar la segunda nota para dejar todo como enteros
notas.pop(1)
print("notas =", notas)
# Eliminar el primer elemento que sea 1
notas.remove(1)
print("notas =", notas)
# Invierte el orden de una lista 
notas.reverse()
print("notas =", notas)
# Ordena los elementos de la lista en orden ascendente
notas.sort()
print("notas =", notas)


# Array de nombres de estudiantes
estudiantes = ["Fulano", "Nicol", "Juan José", "Daniel", "Oscar"]
print("estudiantes =", estudiantes)
# Averiguar la posición de un elemento, en este caso de Juan José
print("Índice del estudiante Juan José", estudiantes.index("Juan José"))
# Añadir un estudiante a la posición 0
estudiantes.insert(0, "Jerónimo")
print("estudiantes =", estudiantes)
# Averiguar la posición de un elemento, en este caso de Juan José
print("Índice del estudiante Juan José", estudiantes.index("Juan José"))
# Añadir un estudiante a la posición 3
estudiantes.insert(3, "Juan José")
print("estudiantes =", estudiantes)
# Averiguar la posición de un elemento, en este caso de Juan José
# Si hay dos "Juan Jose" devuelve la posición del primero que encuentra
print("Índice del estudiante Juan José", estudiantes.index("Juan José"))
