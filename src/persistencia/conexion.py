# persistencia/conexion.py
import sqlite3
from pathlib import Path

RUTA_BD = Path(__file__).resolve().parent.parent / "agencia_viajes.db"


def abrir_conexion():
    return sqlite3.connect(RUTA_BD)


def crear_tabla():
    with abrir_conexion() as conexion:
        conexion.execute(
            """
            CREATE TABLE IF NOT EXISTS viaje (
                id_viaje INTEGER PRIMARY KEY AUTOINCREMENT,
                destino TEXT NOT NULL,
                cliente TEXT NOT NULL,
                fecha TEXT NOT NULL,
                precio REAL NOT NULL
            )
            """
        )
        conexion.commit()
