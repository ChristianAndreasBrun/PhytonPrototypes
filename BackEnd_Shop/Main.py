import Usuarios
import Menus

# -------------------------------------------------------------------------
def registro_usuario():
    print("Por favor, complete los siguientes datos para registrarse:")
    Usuarios.guardar_usuario()
   

def login():
    print("Ingrese sus credenciales:")
    usuario = input("Nombre de usuario: ")
    password = input("Contraseña: ")
    usuario_encontrado = Usuarios.buscar_usuario(usuario, password)
    if usuario_encontrado:
        print(f"\nBienvenido/a {usuario_encontrado.get_nombre()} {usuario_encontrado.get_apellido()}!")
        return usuario_encontrado
    else:
        print("Credenciales incorrectas. Por favor, intente nuevamente.")
        return None
    


# Menu Login --------------------------------------------------------------
def menu_login():
    continuar = True
    while continuar:
        print("Seleccione una opción:")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Salir")
        opcion = input("Opcion seleccionada: ")
        if opcion == "1":
            registro_usuario()
        elif opcion == "2":
            usuario_actual = login()
            if usuario_actual:
                if usuario_actual.get_rol() == "admin":
                    Menus.menu_admin(usuario_actual)
                else:
                    Menus.menu_cliente(usuario_actual)
            else:
                print("no  existe")
        elif opcion == "3":
            print("Hasta la proxima!")
            break
        else:
            print("Opcion no valida. Seleccione una opcion valida.")
menu_login()