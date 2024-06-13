class Alumno:
    def __init__(self, nombre, apellido, nota):
        self.nombre = nombre
        self.apellido = apellido
        self.nota = nota

def guardar_datos(alumno):
    with open('alumnos.txt','a') as archivo:
        archivo.write(f"{alumno.nombre},{alumno.apellido},{alumno.nota} \n")#la f formatea el documento

nombre = input("Dime tu nombre: ")
apellido = input("Dime tu apellido: ")
nota = input("Dime tu nota: ")

alumno = Alumno(nombre, apellido, nota)
guardar_datos(alumno)

