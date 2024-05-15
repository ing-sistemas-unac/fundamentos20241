import funcion_user

def inicio_admin():
    contraseña = int(input("Por favor ingresa tu contraseña "))
    if contraseña == 1234:
        print("Ingreso correcto")
        print("Bienvenido usuario admin")
    else:
        print("Contraseña incorrecta") 
        funcion_user.inicio_user()

if __name__ == "__main__":
    inicio_admin()
    

