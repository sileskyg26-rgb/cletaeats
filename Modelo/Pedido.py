from datetime import datetime


class Pedido:

    ESTADOS_VALIDOS = ("en preparación", "en camino", "suspendido", "entregado")
    _contador_id = 1

    def __init__(self, cliente, restaurante, repartidor, combos: list):
        self._id = Pedido._contador_id
        Pedido._contador_id += 1
        self._cliente = cliente
        self._restaurante = restaurante
        self._repartidor = repartidor
        self._combos = combos
        self._hora_inicio = datetime.now()
        self._hora_entrega = None
        self._estado = "en preparación"
        print(f"[Pedido] Constructor: pedido #{self._id} creado")

    def __del__(self):
        id_pedido = getattr(self, "_id", "?")
        print(f"[Pedido] Destructor: se eliminó el pedido #{id_pedido}")

    @property
    def id(self) -> int:
        return self._id

    @property
    def cliente(self):
        return self._cliente

    @property
    def restaurante(self):
        return self._restaurante

    @property
    def repartidor(self):
        return self._repartidor

    @property
    def combos(self) -> list:
        return self._combos

    @property
    def hora_inicio(self) -> datetime:
        return self._hora_inicio

    @property
    def hora_entrega(self) -> datetime:
        return self._hora_entrega

    @property
    def estado(self) -> str:
        return self._estado

    @estado.setter
    def estado(self, valor: str):
        if valor not in self.ESTADOS_VALIDOS:
            raise ValueError(f"Estado inválido: debe ser uno de {self.ESTADOS_VALIDOS}")
        self._estado = valor
        if valor == "entregado":
            self._hora_entrega = datetime.now()

    def __str__(self) -> str:
        return (f"Pedido #{self._id} | Cliente: {self._cliente.nombre} | "
                f"Restaurante: {self._restaurante.nombre} | Estado: {self._estado}")