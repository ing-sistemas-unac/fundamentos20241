"""
Algoritmo pedir_edad_nombre
    Leer nombre
    Leer edad
    Imprimir 'Hola', nombre, edad
FinAlgoritmo
"""

print('Ingrese su nombre')
nombre = input()
print('Ingrese su edad')
edad = int(input())
"""print('Hola', nombre, 'de', edad, 'años')
print('Hola ' + nombre + ' de ' + str(edad) + ' años')
print(f'Hola {nombre} de {edad} años')"""
if edad > 18:
    print('Usted es mayor de edad')
elif edad == 18: 
    print('Usted tiene 18 años')
else:
    print('Usted es menor de edad')

