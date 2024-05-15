import file_two

print(f"En file_one la variable __name__ tiene como valor {__name__}")

def function_one():
    print("Llamando a la función 1")

def function_two():
    print("Llamando a la función 2")

if __name__ == "__main__":
    print("File one se ejecuta directamente")
    function_two()
    file_two.function_three()
else:
    print("File one se ejecuta cuando se importa")

    