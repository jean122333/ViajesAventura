# menus/menu_viaje.py
from dominio.viaje import Viaje
from persistencia.viaje_dao import ViajeDAO


def _pedir_texto(mensaje: str, obligatorio: bool = True) -> str:
    while True:
        valor = input(f"{mensaje}: ").strip()
        if valor or not obligatorio:
            return valor
        print("Este campo es obligatorio.")


def _pedir_entero(mensaje: str) -> int:
    while True:
        try:
            return int(input(f"{mensaje}: ").strip())
        except ValueError:
            print("Debe ingresar un número entero válido.")


def _pedir_precio(mensaje: str, obligatorio: bool = True) -> float | None:
    while True:
        entrada = input(f"{mensaje}: ").strip()
        if not entrada and not obligatorio:
            return None
        try:
            precio = float(entrada)
            if precio <= 0:
                print("El precio debe ser mayor que 0.")
                continue
            return precio
        except ValueError:
            print("Debe ingresar un monto numérico válido.")


def registrar_viaje():
    print("\n--- Registrar viaje ---")
    destino = _pedir_texto("Destino")
    cliente = _pedir_texto("Cliente")
    fecha = _pedir_texto("Fecha (ej. 2026-12-15)")
    precio = _pedir_precio("Precio")

    viaje = Viaje(destino=destino, cliente=cliente, fecha=fecha, precio=precio)
    ViajeDAO.insertar(viaje)
    print("Viaje registrado:", viaje.mostrar_datos())


def listar_viajes():
    print("\n--- Listado de viajes ---")
    viajes = ViajeDAO.listar()
    if not viajes:
        print("No hay viajes registrados.")
        return
    for viaje in viajes:
        print(" ", viaje.mostrar_datos())


def buscar_viaje():
    print("\n--- Buscar viaje ---")
    id_viaje = _pedir_entero("ID del viaje")
    viaje = ViajeDAO.buscar_por_id(id_viaje)
    if viaje is None:
        print("Viaje no encontrado.")
    else:
        print("Encontrado:", viaje.mostrar_datos())


def actualizar_viaje():
    print("\n--- Actualizar viaje ---")
    id_viaje = _pedir_entero("ID del viaje a actualizar")
    viaje = ViajeDAO.buscar_por_id(id_viaje)
    if viaje is None:
        print("Viaje no encontrado.")
        return

    print("Datos actuales:", viaje.mostrar_datos())
    print("Deje vacío un campo para mantener su valor actual.")
    destino = _pedir_texto("Nuevo destino", obligatorio=False)
    cliente = _pedir_texto("Nuevo cliente", obligatorio=False)
    fecha = _pedir_texto("Nueva fecha", obligatorio=False)
    precio = _pedir_precio("Nuevo precio", obligatorio=False)

    if destino:
        viaje.destino = destino
    if cliente:
        viaje.cliente = cliente
    if fecha:
        viaje.fecha = fecha
    if precio is not None:
        viaje.precio = precio

    ViajeDAO.actualizar(viaje)
    print("Viaje actualizado:", viaje.mostrar_datos())


def eliminar_viaje():
    print("\n--- Eliminar viaje ---")
    id_viaje = _pedir_entero("ID del viaje a eliminar")
    viaje = ViajeDAO.buscar_por_id(id_viaje)
    if viaje is None:
        print("Viaje no encontrado.")
        return

    print("Se eliminará:", viaje.mostrar_datos())
    confirmacion = input("¿Confirmar eliminación? (s/n): ").strip().lower()
    if confirmacion == "s":
        ViajeDAO.eliminar(id_viaje)
        print("Viaje eliminado correctamente.")
    else:
        print("Operación cancelada.")


def menu_viajes():
    opciones = {
        "1": registrar_viaje,
        "2": listar_viajes,
        "3": buscar_viaje,
        "4": actualizar_viaje,
        "5": eliminar_viaje,
    }

    while True:
        print("\n=== AGENCIA DE VIAJES - CRUD ===")
        print("1. Registrar viaje")
        print("2. Listar viajes")
        print("3. Buscar viaje por ID")
        print("4. Actualizar viaje")
        print("5. Eliminar viaje")
        print("0. Salir")

        opcion = input("Seleccione una opción: ").strip()
        if opcion == "0":
            print("Hasta luego.")
            break
        accion = opciones.get(opcion)
        if accion:
            try:
                accion()
            except ValueError as error:
                print("Error de validación:", error)
        else:
            print("Opción no válida.")
