# main.py
from menus.menu_viaje import menu_viajes
from persistencia.conexion import crear_tabla


def main():
    crear_tabla()
    try:
        menu_viajes()
    except (KeyboardInterrupt, EOFError):
        print("\nHasta luego.")


if __name__ == "__main__":
    main()
