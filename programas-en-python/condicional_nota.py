"""
Algoritmo aprobar_materia
    Pedir nota
    Leer nota
    Condición para ver si aprobó o no
FinAlgoritmo
"""

print("Ingrese su nota")
nota = float(input())
if nota >= 3 and nota <= 5:
    print("Felicitaciones, aprobó")
elif nota >= 0 and nota < 3:
    print("Lo siento, usted perdió la materia por la razón que sea")
else: 
    print("Usted no ingresó una nota válida")