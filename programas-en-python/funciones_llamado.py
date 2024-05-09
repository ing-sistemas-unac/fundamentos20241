def saludar(nombre): # def nombre_funcion():
    # contenido de la función
    saludo = "¡Hola! "
    return saludo + nombre

nombre = input("Ingrese un nombre: ")
for i in range(5):
    print(saludar(nombre)) # llamar a la función


