 

from Modelo.GeneradorReportes import GeneradorReportes


class ControladorReportes:

    def __init__(self, generador_reportes: GeneradorReportes):
        self._generador_reportes = generador_reportes
        print("[ControladorReportes] Constructor: controlador creado")

    def __del__(self):
        print("[ControladorReportes] Destructor: controlador eliminado")

    # ---- e) / f) Listados de clientes por estado ----
    def clientes_activos(self) -> list:
        return self._generador_reportes.listado_clientes_activos()

    def clientes_suspendidos(self) -> list:
        return self._generador_reportes.listado_clientes_suspendidos()

    # ---- g) Repartidores con cero amonestaciones ----
    def repartidores_sin_amonestaciones(self) -> list:
        return self._generador_reportes.listado_repartidores_sin_amonestaciones()

    # ---- h) Listado de restaurantes ----
    def listado_restaurantes(self) -> list:
        return self._generador_reportes.listado_restaurantes()

    # ---- i) / l) Restaurante con más / menos pedidos ----
    def restaurante_mayor_pedidos(self):
        return self._generador_reportes.restaurante_mayor_pedidos()

    def restaurante_menor_pedidos(self):
        return self._generador_reportes.restaurante_menor_pedidos()

    # ---- j) / k) Montos vendidos ----
    def monto_total_por_restaurante(self) -> dict:
        return self._generador_reportes.monto_total_por_restaurante()

    def monto_total_general(self) -> float:
        return self._generador_reportes.monto_total_general()

    # ---- m) Quejas por repartidor ----
    def quejas_por_repartidor(self) -> dict:
        return self._generador_reportes.quejas_por_repartidor()

    # ---- n) Pedidos por cliente ----
    def pedidos_por_cliente(self) -> dict:
        return self._generador_reportes.pedidos_por_cliente()

    # ---- o) Cliente con mayor número de pedidos ----
    def cliente_mayor_pedidos(self):
        return self._generador_reportes.cliente_mayor_pedidos()

    # ---- p) Hora pico ----
    def hora_pico(self):
        return self._generador_reportes.hora_pico()