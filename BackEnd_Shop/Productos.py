# -------------------------------------------------------------------------
class Producto:
    def __init__(self, id, nombre, precio):
        self.__id = id
        self.__nombre = nombre
        self.__precio= precio

    def set_id(self, id):
        self.__id = id
    def get_id(self):
        return self.__id
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
    def get_nombre(self):
        return self.__nombre

    def set_precio(self, precio):
        self.__precio = precio
    def get_precio(self):
        return self.__precio
    

# -------------------------------------------------------------------------
def mostrar_productos():
    with open("db/productos.txt","r") as file:
        for line in file:
            partes = line.strip().split(',')
            producto = Producto(partes[0], partes[1], partes[2])
            print(producto.get_id()+". "+producto.get_nombre(),"-",producto.get_precio()+"€")
    

def crear_producto():
    id = input("Introduce el numero ID: ")
    nombre = input("Introduce el Nombre: ")
    precio = input("Introduce el Precio: ")
    producto = Producto(id, nombre, precio)
    with open('db/productos.txt','a') as file:
        file.write(f"{producto.get_id()},{producto.get_nombre()},{producto.get_precio()} \n")
    print("Se ha creado el producto! \n", file)


def comprar_producto(usuario):
    mostrar_productos()
    id = input("Introduce el numero ID: ")
    with open('db/productos.txt', 'r') as file:
        for line in file:
            partes = line.strip().split(',')
            if id == partes[0]:
                producto = Producto(partes[0], partes[1], partes[2])
    with open('db/factura.txt','a') as file:
        file.write(f"{usuario.get_usuario()},{producto.get_id()},{producto.get_precio()} \n")
    print("Se ha comprado el producto! \n")
    

def modificar_producto():
    id_producto = input("Introduce el numero ID del producto: ")
    continuar = True
    while continuar:
        print("Dime que quieres cambiar:")
        print("1. Nombre")
        print("2. Precio")
        print("3. Salir")
        opcion = input("Opcion seleccionada: ")

        with open('db/productos.txt', 'r') as file:
            for line in file:
                partes = line.strip().split(',')
                id = partes[0]
                if id == id_producto:
                    id = partes[0]
                    nombre = partes[1]
                    precio = partes[2]
                    producto = Producto(id, nombre, precio)


        if opcion == "1":
            p_name = input("Dime el nuevo Nombre: ")
            with open("db/productos.txt", "r") as file:
                lines = file.readlines()
            with open("db/productos.txt", "w") as file:
                for line in lines:
                    partes = line.strip().split(',')
                    if producto.get_id() == partes[0]:
                        producto.set_nombre(p_name)
                        line = line.replace(partes[1], p_name)
                    file.write(line)
            print(f"Se ha cambiado el nombre a {p_name}! \n")

        elif opcion == "2":
            price = input("Dime el nuevo Precio: ")
            with open("db/productos.txt", "r") as file:
                lines = file.readlines()
            with open("db/productos.txt", "w") as file:
                for line in lines:
                    partes = line.strip().split(',')
                    if producto.get_id() == partes[0]:
                        producto.set_precio(price)
                        line = f"{producto.get_id()},{producto.get_nombre()},{producto.get_precio()}\n"
                    file.write(line)
            print(f"Se ha cambiado el precio del producto a {price}€!\n")

        elif opcion == "3":
            print("Volviendo al menu Cliente...\n")
            break
        else:
            print("Opcion no valida. Seleccione una opcion valida.\n")