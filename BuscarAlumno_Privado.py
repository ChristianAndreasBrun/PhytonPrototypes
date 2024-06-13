class Alumno:
    def __init__(self, nombre, apellido, nota):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__nota = nota

    def get_nombre(self):
        return self.__nombre
    def set_nombre(self, nombre):
        self.__nombre = nombre
        
    def get_apellido(self):
        return self.__apellido
    def set_apellido(self, apellido):
        self.__apellido = apellido

    def get_nota(self):
        return self.__nota
    def set_nota(self, nota):
        self.__nota = nota


def guardar_datos(alumno):
    with open('alumnos.txt','a') as archivo:
        archivo.write(f"{alumno.get_nombre()},{alumno.get_apellido()},{alumno.get_nota()} \n")

def buscar_datos():
    nombre = input("Dime el nombre del alumno: ")
    with open('alumnos.txt','r') as archivo:
        for linea in archivo:
            partes = linea.strip().split(',')
            if(partes[0] == nombre):
                print(partes[2])


nombre = input("Dime tu nombre: ")
apellido = input("Dime tu apellido: ")
nota = input("Dime tu nota: ")


alumno = Alumno(nombre, apellido, nota)
# guardar_datos(alumno)
buscar_datos()