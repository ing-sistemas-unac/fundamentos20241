# Array con datos homogéneos
vector1 = [1, 2, 3, 0, -2, 1, 100]
print("vector 1 =",vector1)
print("longitud del vector 1 =", len(vector1))
# Índices como expresiones con variables
a = 1
b = 2
print("vector1[a+b] =", vector1[a+b])
print("vector1[3] =", vector1[3])

# Array con datos heterogéneos: datos de diferentes tipos
vector2 = ["Pluto", 31, 12, 2023, 30.8]
print(f"Nombre = {vector2[0]}\nFecha de nacimiento = {vector2[1]}/{vector2[2]}/{vector2[3]}\nPeso = {vector2[-1]}")

# Array se inicializa vacío y luego se añaden elementos
vector3 = []
nombre = input("Ingrese su nombre\n")
vector3.append(nombre)
print(vector3)

