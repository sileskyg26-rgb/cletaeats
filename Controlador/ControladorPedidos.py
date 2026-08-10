from modelo.gestor_pedidos import GestorPedidos
from modelo.gestor_clientes import GestorClientes
from modelo.gestor_restaurantes import GestorRestaurantes
from modelo.gestor_repartidores import GestorRepartidores
from modelo.factura import Factura


class ControladorPedidos:

    def __init__(self, gestor_pedidos: GestorPedidos,
                 gestor_clientes: GestorClientes,
                 gestor_restaurantes: GestorRestaurantes,
                 gestor_repartidores: GestorRepartidores):
        self._gestor_pedidos = gestor_pedidos
        self._gestor_clientes = gestor_clientes
        self._gestor_restaurantes = gestor_restaurantes
        self._gestor_repartidores = gestor_repartidores
        print("[ControladorPedidos] Constructor: controlador creado")

    def __del__(self):
        print("[ControladorPedidos] Destructor: controlador eliminado")

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
            return factura, None
        except ValueError as e:
            return None, str(e)

    def listar_pedidos_cliente(self, cedula_cliente: str) -> list:
        return self._gestor_pedidos.buscar_por_cedula(cedula_cliente)

    def buscar_pedido(self, id_pedido: int):
        return self._gestor_pedidos.buscar_por_id(id_pedido)

    def listar_pedidos(self) -> list:
        return self._gestor_pedidos.listar()