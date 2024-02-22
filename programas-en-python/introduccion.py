# Esto es un comentario de una sola línea
"""
Esto
es 
un 
comentario
de 
varias 
líneas
.....
"""

# saludo es el identificador de la variable
# "Hello world! :)" es el texto o dato que se guarda
saludo = "Hello" # texto o string o str 

# nombre es una variable que pide que el usuario introduzca el dato que va a almacenar
nombre = input("Ingresa tu nombre \n")

# emoji es una variable de tipo string o str
emoji = ";) 🙌🙌"

print(saludo, nombre, emoji) # la coma me sirve para unir textos o variables 
print(saludo + " " + nombre + emoji) # el signo + me sirve para unir textos o variables. A esta unión se le llama concatenar 
print(saludo * 3 + "\n" + emoji * 4) # En los string puedo usar el * para repetir el texto las veces que desee
print(saludo[-5]) # con [0] o [0:2] o [-1] puedo acceder a las posiciones de una cadena de texto

