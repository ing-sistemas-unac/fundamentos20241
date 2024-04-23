from colorama import init, Fore
init()
print(Fore.BLUE)
vector1 = [4, 3, 1, 0, 5]
print("vector1[0] =", vector1[0])
# Actualizar el valor de la posición 0. Se guardará 1
vector1[0] = 1
print(vector1)
# Actualizar el valor de la posición 0 tomando como base el valor que está en esa posición 
vector1[0] = vector1[0] + 10
print(Fore.GREEN)
print(vector1)
# Actualizar el valor de la posición 0 tomando como base el valor que está en la posición 1
vector1[0] = vector1[1] + 11
print(Fore.CYAN)
print(vector1)