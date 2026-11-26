# persistencia/viaje_dao.py
from dominio.viaje import Viaje
from persistencia.conexion import abrir_conexion


class ViajeDAO:
    @staticmethod
    def _fila_a_viaje(fila) -> Viaje:
        return Viaje(
            id_viaje=fila[0],
            destino=fila[1],
            cliente=fila[2],
            fecha=fila[3],
            precio=fila[4],
        )

    @staticmethod
    def insertar(viaje: Viaje) -> Viaje:
        sql = "INSERT INTO viaje (destino, cliente, fecha, precio) VALUES (?, ?, ?, ?)"
        with abrir_conexion() as conexion:
            cursor = conexion.execute(
                sql, (viaje.destino, viaje.cliente, viaje.fecha, viaje.precio)
            )
            conexion.commit()
            viaje.id_viaje = cursor.lastrowid
        return viaje

    @staticmethod
    def listar() -> list[Viaje]:
        sql = "SELECT id_viaje, destino, cliente, fecha, precio FROM viaje ORDER BY id_viaje"
        with abrir_conexion() as conexion:
            filas = conexion.execute(sql).fetchall()
        return [ViajeDAO._fila_a_viaje(f) for f in filas]

    @staticmethod
    def buscar_por_id(id_viaje: int) -> Viaje | None:
        sql = "SELECT id_viaje, destino, cliente, fecha, precio FROM viaje WHERE id_viaje = ?"
        with abrir_conexion() as conexion:
            fila = conexion.execute(sql, (id_viaje,)).fetchone()
        return None if fila is None else ViajeDAO._fila_a_viaje(fila)

    @staticmethod
    def actualizar(viaje: Viaje) -> bool:
        sql = (
            "UPDATE viaje SET destino = ?, cliente = ?, fecha = ?, precio = ? "
            "WHERE id_viaje = ?"
        )
        with abrir_conexion() as conexion:
            cursor = conexion.execute(
                sql,
                (viaje.destino, viaje.cliente, viaje.fecha, viaje.precio, viaje.id_viaje),
            )
            conexion.commit()
            return cursor.rowcount > 0

    @staticmethod
    def eliminar(id_viaje: int) -> bool:
        sql = "DELETE FROM viaje WHERE id_viaje = ?"
        with abrir_conexion() as conexion:
            cursor = conexion.execute(sql, (id_viaje,))
            conexion.commit()
            return cursor.rowcount > 0
