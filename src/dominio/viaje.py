# dominio/viaje.py
class Viaje:
    def __init__(
        self,
        destino: str,
        cliente: str,
        fecha: str,
        precio: float,
        id_viaje: int | None = None,
    ):
        self.id_viaje = id_viaje
        self.destino = destino
        self.cliente = cliente
        self.fecha = fecha
        self.precio = precio

    @property
    def destino(self) -> str:
        return self._destino

    @destino.setter
    def destino(self, valor: str):
        valor = valor.strip()
        if not valor:
            raise ValueError("El destino no puede estar vacío.")
        self._destino = valor

    @property
    def cliente(self) -> str:
        return self._cliente

    @cliente.setter
    def cliente(self, valor: str):
        valor = valor.strip()
        if not valor:
            raise ValueError("El nombre del cliente no puede estar vacío.")
        self._cliente = valor

    @property
    def fecha(self) -> str:
        return self._fecha

    @fecha.setter
    def fecha(self, valor: str):
        valor = valor.strip()
        if not valor:
            raise ValueError("La fecha no puede estar vacía.")
        self._fecha = valor

    @property
    def precio(self) -> float:
        return self._precio

    @precio.setter
    def precio(self, valor: float):
        valor = float(valor)
        if valor <= 0:
            raise ValueError("El precio debe ser mayor que 0.")
        self._precio = valor

    def mostrar_datos(self) -> str:
        return (
            f"ID: {self.id_viaje} | Destino: {self.destino} | "
            f"Cliente: {self.cliente} | Fecha: {self.fecha} | "
            f"Precio: ${self.precio:,.2f}"
        )
