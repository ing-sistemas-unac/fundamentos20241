# Importar numpy
import numpy as np
sample_list = [1, 2, 3]
# Convertir la lista a un arreglo de numpy
np_sample_list = np.array(sample_list)
# Imprimir la lista
print(np_sample_list)

# Generar números en un rango dentro del arreglo
range_list = np.arange(0, 100)
print(range_list)
# Generar números en un arreglo dentro de un rango y el paso (salto)
range_list = np.arange(0, 100, 2)
print(range_list)

# Generar un arreglo con unos y ceros
zeros_list = np.zeros(20, int) # El 2 indica la cantidad de ceros
ones_list = np.ones(40, int) # El 4 indica la cantidad de unos
print(zeros_list)
print(ones_list)

# Hallar el máximo valor en una lista
print("Valor máximo en la lista =", range_list.max())
print("Posición o índice del valor máximo =", range_list.argmax())



