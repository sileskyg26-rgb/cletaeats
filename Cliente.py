from usuario import Usuario


class Cliente(Usuario):

    def __init__(self, cedula: str = "", nombre: str = "", direccion: str = "",
                 telefono: str = "", correo: str = "", numero_tarjeta: str = "",
                 estado: str = "activo"):
        super().__init__(cedula, nombre, direccion, telefono, correo)
        self._numero_tarjeta = numero_tarjeta
        self._estado = estado
        self._pedidos = []
        print(f"[Cliente] Constructor: {self.nombre} inscrito como cliente")

    def __del__(self):
        print(f"[Cliente] Destructor: se eliminó el cliente {self.nombre}")

    @property
    def numero_tarjeta(self) -> str:
        return self._numero_tarjeta

    @numero_tarjeta.setter
    def numero_tarjeta(self, valor: str):
        self._numero_tarjeta = valor

    @property
    def estado(self) -> str:
        return self._estado

    @estado.setter
    def estado(self, valor: str):
        if valor not in ("activo", "suspendido"):
            raise ValueError("Estado inválido: debe ser 'activo' o 'suspendido'")
        self._estado = valor

    @property
    def pedidos(self) -> list:
        return self._pedidos

    def esta_activo(self) -> bool:
        return self._estado == "activo"

    def agregar_pedido(self, pedido):
        self._pedidos.append(pedido)

    def listar_pedidos(self) -> list:
        return self._pedidos

    def registrar(self):
        print(f"Cliente registrado: {self}")

    def __str__(self) -> str:
        return (f"{super().__str__()} | Tarjeta: {self._numero_tarjeta} | "
                f"Estado: {self._estado} | Pedidos: {len(self._pedidos)}")