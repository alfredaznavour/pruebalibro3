# Importar las funciones desde el archivo de funciones
from funciones3 import registrar_prestamo, listar_prestamos, imprimir_recibo, salir

# Lista para almacenar los pedidos
pedidos = []

# Programa principal
while True:
    print("\nSistema de libreria antartica")
    print("1. Registrar prestamo")
    print("2. Listar todos los prestamos")
    print("3. Imprimir recibo de prestamo")
    print("4. Salir del programa")
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        registrar_prestamo(pedidos)
    elif opcion == '2':
        listar_prestamos(pedidos)
    elif opcion == '3':
        imprimir_recibo(pedidos)
    elif opcion == '4':
        salir()
        break
    else:
        print("Opción no válida. Intente de nuevo.")