from Modelo.Usuario import Usuario
from Modelo.Validaciones import validar_numero_tarjeta


# HERENCIA: Cliente "hereda" de Usuario, así que ya viene con cédula,
# nombre, dirección, teléfono y correo (y sus validaciones) gratis, sin
# tener que volver a escribirlos acá. Solo agregamos lo que le hace falta
# de más a un cliente puntual: tarjeta, estado y pedidos.
class Cliente(Usuario):

    _contador_id = 1

    def __init__(self, cedula: str = "", nombre: str = "", direccion: str = "",
                 telefono: str = "", correo: str = "", numero_tarjeta: str = "",
                 estado: str = "activo"):
        validar_numero_tarjeta(numero_tarjeta)
        self._id = Cliente._contador_id
        Cliente._contador_id += 1
        super().__init__(cedula, nombre, direccion, telefono, correo)
        self._numero_tarjeta = numero_tarjeta
        self._estado = estado
        self._pedidos = []
        print(f"[Cliente] Constructor: {self.nombre} inscrito como cliente")

    def __del__(self):
        nombre = getattr(self, "_nombre", "?")
        print(f"[Cliente] Destructor: se eliminó el cliente {nombre}")

    @property
    def id(self) -> int:
        return self._id

    @property
    def numero_tarjeta(self) -> str:
        return self._numero_tarjeta

    @numero_tarjeta.setter
    def numero_tarjeta(self, valor: str):
        validar_numero_tarjeta(valor)
        self._numero_tarjeta = valor

    # PROPIEDADES (get y set): "estado" se ve como si fuera un atributo
    # normal (cliente.estado = "suspendido"), pero por detrás son dos
    # métodos. El get (arriba) solo devuelve el valor; el set (abajo) revisa
    # que el valor sea válido ANTES de guardarlo. Así evitamos que a alguien
    # se le ocurra poner cliente.estado = "banana".
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

    # POLIMORFISMO: este registrar() es el mismo método "abstracto" que
    # definimos en Usuario, pero acá cada clase lo hace a su manera —
    # Repartidor tiene su propio registrar() con un mensaje distinto. Si en
    # algún lado del código tenés una lista mezclada de Clientes y
    # Repartidores y les llamás .registrar() a todos por igual, cada uno va
    # a responder con SU versión, sin que vos tengas que preguntar "¿sos
    # cliente o repartidor?" antes de llamarlo.
    def registrar(self):
        print(f"Cliente registrado: {self}")

    def __str__(self) -> str:
        return (f"ID: {self._id} | {super().__str__()} | Tarjeta: {self._numero_tarjeta} | "
                f"Estado: {self._estado} | Pedidos: {len(self._pedidos)}")