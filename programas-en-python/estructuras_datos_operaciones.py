# Definir un arreglo de frutas favoritas
frutas = ["manzana", "uva", "fresa", "banano", "mango"]
# Acceder a una posición
print("frutas[2] =", frutas[2])
# Acceder a una posición negativa
print("frutas[-3] =", frutas[-3])
# Añadir un elemento al final de la lista
frutas.append("kiwi")
frutas.append("tamarindo")
frutas.append("kiwi")
# Imprimir la lista 
print("frutas =", frutas)
# Crear una copia de la lista
copia_frutas = frutas.copy()
print("copia =", copia_frutas)
# Eliminar los elementos de la lista
copia_frutas.clear()
print("copia_frutas =", copia_frutas)
# Contar cuántas veces aparece el "kiwi"
print("cantidad de kiwis =", frutas.count("kiwi"))
# Usar extend para unir dos listas
copia_frutas.append("guama")
copia_frutas.extend(frutas) # Añadimos los elementos de la lista frutas a la lista copia_frutas
print("copia_frutas =", copia_frutas)
# Consultar el índice de un elemento
print("índice del tamarindo en copia_frutas =", copia_frutas.index("tamarindo"))
# Añadir un elemento en una posición en específico
copia_frutas.insert(4, "toronja") # "toronja" en la posición 4
print("copia_frutas =", copia_frutas)
# Eliminar un elemento de una posición en específico
copia_frutas.pop(9) # Se fue 1 kiwi
print("copia_frutas =", copia_frutas)
# Eliminar un elemento conociendo su valor
copia_frutas.remove("toronja")
print("copia_frutas =", copia_frutas)
# Invertir el orden de copia_frutas
copia_frutas.reverse()
print("copia_frutas invertido =", copia_frutas)
# Ordenar la lista
copia_frutas.sort()
print("copia_frutas ordenado A-Z =", copia_frutas)
copia_frutas.sort(reverse=True)
print("copia_frutas ordenado Z-A =", copia_frutas)
# Recorrer el arreglo con un ciclo for
# Ciclo for con rango 
for indice in range(0, len(frutas)):
    if indice == len(frutas)-1:
        print(frutas[indice], end=".")
    else: 
        print(frutas[indice], end=", ")
# Ciclo for iterando en la lista 
for fruta in frutas:
    print(fruta, end=" ")

        




