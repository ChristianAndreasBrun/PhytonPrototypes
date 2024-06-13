import Usuarios
import Productos
import Facturas

# Menu Administrador --------------------------------------------------------------
def menu_admin(usuario):
    continuar = True
    while continuar:
        print(f"Menu usuario - {usuario.get_usuario()}:")
        print("1. Crear producto")
        print("2. Modificar producto")
        print("3. Eliminar usuario")
        print("4. Ver facturación de usuario")
        print("5. Ver facturación total")
        print("6. Cerrar sesion")

        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            Productos.crear_producto()
        elif opcion == "2":
            Productos.modificar_producto()
        elif opcion == "3":
            Usuarios.eliminar_usuario()
        elif opcion == "4":
            Facturas.facturacion_usuario()
        elif opcion == "5":
            Facturas.facturacion_total()
        elif opcion == "6":
            print("Se ha cerrado la sesion.")
            break
        else:
            print("Opción inválida. Inténtalo de nuevo.")



# Menu Cliente --------------------------------------------------------------
def menu_cliente(usuario):
    continuar = True
    while continuar:
        print(f"Menu cliente - {usuario.get_usuario()}:")
        print("1. Ver productos")
        print("2. Comprar producto")
        print("3. Modificar mis datos")
        print("4. Cerrar sesion")

        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            Productos.mostrar_productos()
        elif opcion == "2":
            Productos.comprar_producto(usuario)
        elif opcion == "3":
            Usuarios.modificar_datos(usuario)
        elif opcion == "4":
            print("Se ha cerrado la sesion.")
            break
        else:
            print("Opción inválida. Inténtalo de nuevo.")