class User:
    def __init__(self, nombre, apellidos, usuario, password):
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__usuario = usuario
        self.__password = password


    def set_nombre(self, nombre):
        self.__nombre = nombre
    def get_nombre(self):
        return self.__nombre
    
    def set_apellidos(self, apellidos):
        self.__apellidos = apellidos
    def get_apellidos(self):
        return self.__apellidos

    def set_usuario(self, usuario):
        self.__usuario = usuario
    def get_usuario(self):
        return self.__usuario

    def set_pass(self, password):
        self.__password = password
    def get_pass(self):
        return self.__password


# -------------------------------------------------------------------------------------
def add_user():
    nombre = input("Dime tu nombre: ")
    apellidos = input("Dime tus apellidos: ")
    usuario = input("Dime tu nombre de usuario: ")
    password = input("Introduce una contraseña: ")

    usuario = User(nombre, apellidos, usuario, password)
    print(usuario.apellidos)
    f = open ('usuario.txt','w+')
    f.write(usuario.apellidos)
    f.close


def exit():
    print("Adios!")
    return False

# -------------------------------------------------------------------------------------

def switch(opcion):
    diccionario = {
        "1": "add_user()",
        "2": "show_user()",
        "3": "exit()",
    }
    return eval(diccionario.get(opcion))

continuar = True

while(continuar):
    print("""Seleciona una opcion:
    1) Añadir Usuairos
    2) Mostrar Usuairos
    3) Salir
    """)
    opcion = input()
    try:
        continuar = switch(opcion)
    except Exception as a:
        print("Selecciona una opcion valida!", a)