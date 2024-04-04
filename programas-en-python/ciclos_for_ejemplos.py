from colorama import init, Fore

# Inicializa colorama
init()

print(Fore.RED + "Números del 1 al 10")
for numero in range(0, 11, 1):
    print(numero, end=" ")

print(Fore.BLUE + "\n\nNúmeros del 1 al 10")
for numero in range(0, 11):
    print(numero, end=" ")

print(Fore.MAGENTA + "\n\nNúmeros del 10 al 0")
for numero in range(10, -1, -1):
    print(numero, end=" ")