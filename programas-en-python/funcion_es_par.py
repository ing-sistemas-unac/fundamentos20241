"""
Escribe una función llamada es_par que tome un número como argumento y devuelva True si es par, o False si es impar.
"""
def es_par(numero):
    if numero % 2 == 0:
        return True
    else: 
        return False

print("Ingrese un número para saber si es par o impar")    
numero = int(input())
print(f"¿Es {numero} un número par? =  {es_par(numero)}")