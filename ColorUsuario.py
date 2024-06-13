# print ("1: Añadior color")
# print ("2: Mostrar listado color")

# opcion = input("Dime que quieres hacer")
# if(opcion == 1):
#     addcolor()
# elif(opcion == 2):
#     listado()



#------------------------------------------------------------------------------------------------------------
import random
# Diccionarios
users = [
    {'Nombre': 'Josep'},
    {'Nombre': 'Claudio'},
    {'Nombre': 'Isabel'},
    {'Nombre': 'Sheila'}
]

colores = ['amarillo','azul','verde','rojo']


# Funccion_Añadir Color
def add_color():
    color_actual = input("Introdce un color: ").lower
    print (color_actual)
    while(color_actual in colores):
        print("El color ya existe!")
        add_color()
    else:
        colores.append(color_actual)
        print("El color introducido es correcto")
    return True

# Funccion_Mostrar Color
def show_colors():
    for color in colores:
        print("Color: ", color)
    return True

# Funccion_Ordenar Color
def order_colors():
    colores.sort()
    return True

# Funccion_Añadir Usuario
def add_user():
    usuario_actual = input("Intorduce nombre usuario")
    diccionarioUsuario = {"Nombre": usuario_actual}
    if diccionarioUsuario in users:
        print("El usuario ya existe")
    else:
        users.append(diccionarioUsuario)
        print("Usuario agregado")
        if(len(users)>len(colores)):
            add_color()
    return True

# Funccion_Asignar Color
def asing_color():
    colores_temporal = colores.copy()
    for usuario in users:
        numAleatorio = random.randint(0,len(colores_temporal)-1)
        usuario['Color'] = colores_temporal[numAleatorio]
        colores_temporal.remove(usuario['Color'])
        print("Usuario ->",usuario['Nombre'],"Color ->",usuario['Color'])
    return True

# Funccion_Eliminar Usuario
def delete_user():
    if(len(users)>0):
        usuarios_temporal = users.copy()
        usuarios_temporal = sorted(usuarios_temporal, key=lambda k: k['Nombre'])
        print("Que usuario se va a elimniar")
        i = 0
        for users in usuarios_temporal:
            print("indice", i, "usuario: ", users['Nombre'])
            i += 1
            seleccion = -1
        while(seleccion <0 or seleccion > len(users)-1):
            try:
                seleccion = int(input("Seleccione un indice de la lista anterior"))
            except ValueError:
                print("No teclear letras!")
            users.remove(usuarios_temporal[seleccion])
            print("Usuario -> ", usuarios_temporal[seleccion]['Nombre'], " Borrado correctamente")
        else:
            print("No existen usuarios para eliminar")
    return True

# Funccion_Mostrar Usuario
def shoiw_user():
    i = 0
    for usuario in users:
        print("indice ", i, " Usuario: ", users['Nombre'])
        i += 1
    return True

# Funccion_Salir
def exit():
    print("Adios")
    return False



# Menu
def switch (option):
    dictionary = {
        "1": "add_color()",
        "2": "show_colors()",
        "3": "order_colors()",
        "4": "add_user()",
        "5": "asign_color()",
        "6": "delete_user()",
        "7": "show_users()",
        "8": "exit()"
    }
    return eval(dictionary.get(option))

continuar = True

while(continuar):
    print("""Seleccionar una opcion:
    1) Añadir colores a la lista
    2) Mostrar listado de colores
    3) Ordenar listado de colores alfabeticamente
    4) Añadir usuario
    5) Asignar colores a cada usuario
    6) Eliminar usuario
    7) Mostrar usuarios
    8) Salir
    """)

    option = input()
    try:
        continuar = switch(option)
    except Exception as a:
        print("Selecciona una opcion valida", a)
