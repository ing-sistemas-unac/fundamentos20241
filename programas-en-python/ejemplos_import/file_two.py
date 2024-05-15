print(f"En file_two la variable __name__ tiene como valor {__name__}")

def function_three():
    print("Llamando a la función 3")

if __name__ == "__main__":
    print("File two se ejecuta directamente")
else:
    print("File two se ejecuta cuando se importa")