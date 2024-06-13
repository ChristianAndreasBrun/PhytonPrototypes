# -------------------------------------------------------------------------
class Usuario():
    def __init__(self, nombre, apellido, usuario, password, rol: str ="cliente"):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__usuario = usuario
        self.__password = password
        self.__rol = rol
        
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self, nombre):
        self.__nombre = nombre
        
    def get_apellido(self):
        return self.__apellido
    def set_apellido(self, apellido):
        self.__apellido = apellido

    def get_usuario(self):
        return self.__usuario
    def set_usuario(self, usuario):
        self.__usuario = usuario

    def get_password(self):
        return self.__password
    def set_password(self, password):
        self.__password = password

    def get_rol(self):
        return self.__rol
    def set_rol(self, rol):
        self.__rol = rol


# -------------------------------------------------------------------------
def guardar_usuario():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    usuario = input("Nombre de usuario: ")
    password = input("Contraseña: ")
    rol = "cliente"
    usuario = Usuario(nombre, apellido, usuario, password, rol)
    with open("db/usuarios.txt", "a") as file:
        file.write(f"{usuario.get_nombre()},{usuario.get_apellido()},{usuario.get_usuario()},{usuario.get_password()},{usuario.get_rol()}\n")
    print(f"Registro completado. Bienvenido {usuario.get_usuario()}! \n")


def buscar_usuario(usuario, password):
    with open("db/usuarios.txt", "r") as file:
        lineas = file.readlines()
        for linea in lineas:
            partes = linea.strip().split(",")
            if partes[2] == usuario and partes[3] == password:       
                user = Usuario(partes[0], partes[1], partes[2], partes[3], partes[4])
                return user
            

def modificar_datos(usuario):
    continuar = True
    while continuar:
        print("Dime que quieres cambiar:")
        print("1. Nombre")
        print("2. Apellido")
        print("3. Usuario")
        print("4. Contraseña")
        print("5. Salir")
        opcion = input("Opcion seleccionada: ")

        if opcion == "1":
            name = input("Introduce el nuevo Nombre: ")
            with open("db/usuarios.txt", "r") as file:
                lines = file.readlines()
            with open("db/usuarios.txt", "w") as file:
                for line in lines:
                    partes = line.strip().split(',')
                    if usuario.get_nombre() == partes[0]:
                        line = line.replace(usuario.get_nombre(), name)
                        usuario.set_nombre(name)
                    file.write(line)
            print("Se ha cambiado el Nombre! \n")

        elif opcion == "2":
            surname = input("Introduce el nuevo Apellido: ")
            with open("db/usuarios.txt", "r") as file:
                lines = file.readlines()
            with open("db/usuarios.txt", "w") as file:
                for line in lines:
                    partes = line.strip().split(',')
                    if usuario.get_apellido() == partes[1]:
                        line = line.replace(usuario.get_apellido(), surname)
                        usuario.set_apellido(surname)
                    file.write(line)
            print("Se ha cambiado el Apellido! \n")

        elif opcion == "3":
            user = input("Introduce el nuevo nombre de Usuario: ")
            with open("db/usuarios.txt", "r") as file:
                lines = file.readlines()
            with open("db/usuarios.txt", "w") as file:
                for line in lines:
                    partes = line.strip().split(',')
                    if usuario.get_usuario() == partes[2]:
                        line = line.replace(usuario.get_usuario(), user)
                        usuario.set_usuario(user)
                    file.write(line)
            print("Se ha cambiado el Usuario! \n")

        elif opcion == "4":
            passwrd = input("Introduce la nueva Contraseña: ")
            with open("db/usuarios.txt", "r") as file:
                lines = file.readlines()
            with open("db/usuarios.txt", "w") as file:
                for line in lines:
                    partes = line.strip().split(',')
                    if usuario.get_password() == partes[3]:
                        line = line.replace(usuario.get_password(), passwrd)
                        usuario.set_password(passwrd)
                    file.write(line)
            print("Se ha cambiado la Contraseña! \n")

        elif opcion == "5":
            print("Volviendo al menu Cliente...\n")
            break
        else:
            print("Opcion no valida. Seleccione una opcion valida.\n")

    

def eliminar_usuario():
    user = input("Dime el usuario a elimniar: ")
    with open('db/usuarios.txt', 'r') as file:
        lines = file.readlines()
    with open('db/usuarios.txt', 'w') as file:
        for line in lines:
            if user not in line:
                file.write(line)
    print(f"El usuario {user} ha sido eliminado.\n")