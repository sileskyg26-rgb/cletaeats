from Modelo.Usuario import Usuario
from Modelo.Queja import Queja
from Modelo.ListaQuejas import ListaQuejas
from Modelo.Validaciones import validar_numero_tarjeta


class Repartidor(Usuario):

    COSTO_KM_HABIL = 1000
    COSTO_KM_FERIADO = 1500
    MAX_AMONESTACIONES = 4

    _contador_id = 1

    # CONSTRUCTOR default Y "sobrecargado" en uno solo: Python no permite
    # tener dos __init__ distintos como en Java (uno vacío y otro con datos),
    # así que usamos valores por defecto ("" y "disponible") para lograr lo
    # mismo. Repartidor() crea uno vacío (constructor default); y
    # Repartidor("123", "Juan", ...) lo crea ya con todos los datos (como si
    # fuera un constructor "sobrecargado"), sin escribir un segundo método.
    def __init__(self, cedula: str = "", nombre: str = "", direccion: str = "",
                 telefono: str = "", correo: str = "", numero_tarjeta: str = "",
                 estado: str = "disponible"):
        validar_numero_tarjeta(numero_tarjeta)
        self._id = Repartidor._contador_id
        Repartidor._contador_id += 1
        super().__init__(cedula, nombre, direccion, telefono, correo)
        self._numero_tarjeta = numero_tarjeta
        self._estado = estado
        self._distancia_pedido = 0.0
        self._km_recorridos_diarios = 0.0
        self._numero_amonestaciones = 0
        self._lista_quejas = ListaQuejas()
        print(f"[Repartidor] Constructor: {self.nombre} inscrito como repartidor")

    def __del__(self):
        nombre = getattr(self, "_nombre", "?")
        print(f"[Repartidor] Destructor: se eliminó el repartidor {nombre}")

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

    @property
    def estado(self) -> str:
        return self._estado

    @estado.setter
    def estado(self, valor: str):
        if valor not in ("disponible", "ocupado"):
            raise ValueError("Estado inválido: debe ser 'disponible' u 'ocupado'")
        self._estado = valor

    @property
    def distancia_pedido(self) -> float:
        return self._distancia_pedido

    @distancia_pedido.setter
    def distancia_pedido(self, valor: float):
        self._distancia_pedido = valor

    @property
    def km_recorridos_diarios(self) -> float:
        return self._km_recorridos_diarios

    @km_recorridos_diarios.setter
    def km_recorridos_diarios(self, valor: float):
        self._km_recorridos_diarios = valor

    @property
    def numero_amonestaciones(self) -> int:
        return self._numero_amonestaciones

    def calcular_costo_transporte(self, es_feriado: bool = False) -> float:
        costo_km = self.COSTO_KM_FERIADO if es_feriado else self.COSTO_KM_HABIL
        return self._distancia_pedido * costo_km

    def esta_disponible(self) -> bool:
        return self._estado == "disponible" and not self.debe_salir_de_la_empresa()

    def agregar_amonestacion(self):
        self._numero_amonestaciones += 1
        if self.debe_salir_de_la_empresa():
            print(f"AVISO: {self.nombre} alcanzó {self._numero_amonestaciones} "
                  f"amonestaciones y debe abandonar la empresa.")

    def debe_salir_de_la_empresa(self) -> bool:
        return self._numero_amonestaciones >= self.MAX_AMONESTACIONES

    def restaurar_amonestaciones(self, cantidad: int):
        """Restaura el conteo de amonestaciones al recargar desde archivo,
        sin disparar el aviso de salida de la empresa."""
        self._numero_amonestaciones = cantidad

    def agregar_queja(self, descripcion: str, cedula_cliente: str = ""):
        queja = Queja(descripcion, cedula_cliente)
        self._lista_quejas.agregar_queja(queja)
        self.agregar_amonestacion()

    def cargar_queja(self, descripcion: str, cedula_cliente: str, fecha):
        """Reconstruye una queja ya existente (desde archivo) sin volver
        a sumar amonestación, dado que numero_amonestaciones ya se carga
        por su cuenta desde el archivo de repartidores."""
        queja = Queja(descripcion, cedula_cliente, fecha)
        self._lista_quejas.agregar_queja(queja)

    def listar_quejas(self) -> list:
        return self._lista_quejas.listar()

    @property
    def quejas_registradas(self) -> list:
        return self._lista_quejas.quejas

    def registrar(self):
        print(f"Repartidor registrado: {self}")

    def __str__(self) -> str:
        return (f"ID: {self._id} | {super().__str__()} | Tarjeta: {self._numero_tarjeta} | "
                f"Estado: {self._estado} | Amonestaciones: {self._numero_amonestaciones} | "
                f"Km recorridos hoy: {self._km_recorridos_diarios}")