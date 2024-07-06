
def registrar_prestamo(pedidos):
    nombre = input("Ingrese el nombre del cliente: ")
    apellido = input("Ingrese el apellido del cliente: ")
    id_libro = input("Ingrese el id del libro: ")
    fecha_p = input("Fecha de prestamo: ")
    fecha_d = (input("Fecha de devolucion: "))
   

    pedido = {
        'nombre': nombre,
        'apellido': apellido,
        'id_libro': id_libro,
        'fecha_prestamo': fecha_p,
        'fecha_devolucion': fecha_d,
        
    }
    
    pedidos.append(pedido)
    print("Libro registrado exitosamente.")


def listar_prestamos(pedidos):
    if not pedidos:
        print("No hay pedidos registrados.")
        return

    for pedido in pedidos:
        print(f"Cliente: {pedido['nombre']} {pedido['apellido']}\n") 
        print(f"identificacion del libro: {pedido['id_libro']}\n")
        print(f"fecha de prestamo: {pedido['fecha_prestamo']}\n")
        print(f"fecha de devolucion : {pedido['fecha_devolucion']}\n")
        print("")


def imprimir_recibo(pedidos):
    if not pedidos:
        print("No hay pedidos registrados.")
        return
    
    id_libro = input("Ingrese el sector para generar la hoja de ruta: ")
    pedidos_id = [pedido for pedido in pedidos if pedido['id_libro'] == id_libro]
    
    if not pedidos_id:
        print(f"No hay préstamo registrado con ese id: {id_libro}.")
        return

    with open(f"hoja_de_ruta_id_libro.txt", "w") as file:
        for pedido in pedidos_id:
            file.write(f"Cliente: {pedido['nombre']} {pedido['apellido']}\n")
            file.write(f"Identificación del libro: {pedido['id_libro']}\n")
            file.write(f"Fecha de préstamo: {pedido['fecha_prestamo']}\n")
            file.write(f"Fecha de devolución: {pedido['fecha_devolucion']}\n")
            file.write("\n")
    
    print(f"Recibo de préstamo para el sector {id_libro} generado exitosamente.")


def salir():
    print("Saliendo del programa")