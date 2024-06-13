# -------------------------------------------------------------------------
class Factura:
    def __init__(self, usuario, producto, precio):
        self.__usuario = usuario
        self.__producto = producto
        self.__precio= precio

    def set_usuario(self, usuario):
        self.__usuario = usuario
    def get_usuario(self):
        return self.__usuario
    
    def set_producto(self, producto):
        self.__producto = producto
    def get_producto(self):
        return self.__producto

    def set_precio(self, precio):
        self.__precio = precio
    def get_precio(self):
        return self.__precio
    

# Functions -------------------------------------------------------
def facturacion_total():
    sumaProd = 0
    with open('db/factura.txt','r') as file:
        for line in file:
            partes = line.strip().split(',')
            total = int(partes[2])
            sumaProd += total
    print(f"\nEl total Facturado es de: {sumaProd}€\n")


def facturacion_usuario():
    sumaProd = 0
    user = input("Dime el usuario: ")
    with open('db/factura.txt','r') as file:
        for line in file:
            partes = line.strip().split(',')
            if user == partes[0]:
                total = int(partes[2])
                sumaProd += total
    print(f"\nEl total Facturado por el Usuario {user}, es de: {sumaProd}€\n")