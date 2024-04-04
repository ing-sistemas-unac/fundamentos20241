palabra = "hola"
print("Intente adivinar la palabra. Tiene 4 letras")
while True:
    palabra_usuario = input()
    if palabra == palabra_usuario:
        print("FELICITACIONES, has adivinado la palabra")
        break
    else: 
        print("Sigue intentando")