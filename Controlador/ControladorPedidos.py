from Modelo.GestorPedidos import GestorPedidos
from Modelo.GestorClientes import GestorClientes
from Modelo.GestorRestaurantes import GestorRestaurantes
from Modelo.GestorRepartidores import GestorRepartidores
from Modelo.Factura import Factura


class ControladorPedidos:

    def __init__(self, gestor_pedidos: GestorPedidos,
                 gestor_clientes: GestorClientes,
                 gestor_restaurantes: GestorRestaurantes,
                 gestor_repartidores: GestorRepartidores,
                 controlador_principal=None):
        self._gestor_pedidos = gestor_pedidos
        self._gestor_clientes = gestor_clientes
        self._gestor_restaurantes = gestor_restaurantes
        self._gestor_repartidores = gestor_repartidores
        self._controlador_principal = controlador_principal
        print("[ControladorPedidos] Constructor: controlador creado")

    def __del__(self):
        print("[ControladorPedidos] Destructor: controlador eliminado")

    def _guardar(self):
        if self._controlador_principal is not None:
            self._controlador_principal.guardar_todo()

    def hacer_pedido(self, cedula_cliente: str,
                      cedula_juridica_restaurante: str,
                      numeros_combos: list):
        cliente = self._gestor_clientes.buscar_por_cedula(cedula_cliente)
        if cliente is None:
            return None, "Cliente no registrado, debe inscribirse primero"

        restaurante = self._gestor_restaurantes.buscar_por_cedula(
            cedula_juridica_restaurante)
        if restaurante is None:
            return None, "Restaurante no encontrado"

        try:
            pedido = self._gestor_pedidos.crear_pedido(
                cliente, restaurante, self._gestor_repartidores,
                numeros_combos)
            self._guardar()
            return pedido, None
        except (PermissionError, ValueError, RuntimeError) as e:
            return None, str(e)

    def entregar_pedido(self, id_pedido: int, km_recorridos: float,
                         es_feriado: bool = False):
        pedido = self._gestor_pedidos.buscar_por_id(id_pedido)
        if pedido is None:
            return None, "Pedido no encontrado"

        try:
            factura = Factura(pedido, km_recorridos, es_feriado)
            pedido.estado = "entregado"
            pedido.repartidor.estado = "disponible"
            self._guardar()
            return factura, None
        except ValueError as e:
            return None, str(e)

    def listar_pedidos_cliente(self, cedula_cliente: str) -> list:
        return self._gestor_pedidos.buscar_por_cedula(cedula_cliente)

    def buscar_pedido(self, id_pedido: int):
        return self._gestor_pedidos.buscar_por_id(id_pedido)

    def listar_pedidos(self) -> list:
        return self._gestor_pedidos.listar()