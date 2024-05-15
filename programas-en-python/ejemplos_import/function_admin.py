import function_user

def inicio_admin():
    print("Este es el login de administrador")
    print("Ingrese su contraseña para iniciar sesión")
    contraseña = int(input())
    if contraseña == 1234: 
        print("Bienvenido ADMIN")
    else:
        print("Contraseña inválida")
        function_user.inicio_user()

if __name__ == "__main__":
    inicio_admin()