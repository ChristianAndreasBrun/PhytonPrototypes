# frutas = {
#     'Platano': 1.35,
#     'Manzana': 0.80,
#     'Pera': 0.85,
#     'Naranja': 0.70,
# }

# fruta = input("Introduce la futa deseada: ")
# kg = float(input("Cuantos kilos quieres?: "))

# if fruta in frutas:
#     print (kg, 'Kilos de ', fruta, ' valen', frutas[fruta]*kg,'€')
# else:
#     print("La fruta ", fruta, " no existe!")

# -----------------------------------------------------------------------------------------------
curso = {
    'Matematicas': 6,
    'Fisica': 4,
    'Quimica': 5
}

total_creditos = 0
for asignatura, creditos in curso.items():
#    print(curso.items())
    print(asignatura, 'tiene: ', creditos, ' creditos' )
    total_creditos += creditos

print("El numero total de creditos son: ", total_creditos)