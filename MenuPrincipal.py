from GestorClientes import GestorClientes
from GestorRestarurantes import GestorRestaurantes
from GestorRepartidores import GestorRepartidores
from GestorPedidos import GestorPedidos
from GeneradorReportes import GeneradorReportes
from Cliente import Cliente
from Restaurante import Restaurante
from Repartidor import Repartidor
from Combo import Combo
from Factura import Factura


class MenuPrincipal:

    def __init__(self):
        self._gestor_clientes = GestorClientes()
        self._gestor_restaurantes = GestorRestaurantes()
        self._gestor_repartidores = GestorRepartidores()
        self._gestor_pedidos = GestorPedidos()
        self._generador_reportes = GeneradorReportes(
            self._gestor_clientes, self._gestor_restaurantes,
            self._gestor_repartidores, self._gestor_pedidos)
        print("[MenuPrincipal] Constructor: sistema listo")

    def __del__(self):
        print("[MenuPrincipal] Destructor: sistema cerrado")

    def registrar_cliente(self, cedula, nombre, direccion, telefono, correo, numero_tarjeta):
        cliente = Cliente(cedula, nombre, direccion, telefono, correo, numero_tarjeta)
        self._gestor_clientes.agregar(cliente)
        return cliente

    def registrar_restaurante(self, nombre, cedula_juridica, direccion, tipo_comida, combos_info):
        restaurante = Restaurante(nombre, cedula_juridica, direccion, tipo_comida)
        for numero, descripcion in combos_info:
            restaurante.menu.agregar_combo(Combo(numero, descripcion))
        self._gestor_restaurantes.agregar(restaurante)
        return restaurante

    def registrar_repartidor(self, cedula, nombre, direccion, telefono, correo, numero_tarjeta):
        repartidor = Repartidor(cedula, nombre, direccion, telefono, correo, numero_tarjeta)
        self._gestor_repartidores.agregar(repartidor)
        return repartidor

    def iniciar_sesion_cliente(self, cedula):
        cliente = self._gestor_clientes.buscar_por_cedula(cedula)
        if cliente is None:
            raise ValueError("Cliente no registrado, debe inscribirse primero")
        if not cliente.esta_activo():
            raise PermissionError("Cliente suspendido: no se acepta la solicitud")
        return cliente

    def ver_menu_restaurante(self, cedula_juridica):
        restaurante = self._gestor_restaurantes.buscar_por_cedula(cedula_juridica)
        if restaurante is None:
            raise ValueError("Restaurante no encontrado")
        return restaurante.menu.listar_combos()

    def hacer_pedido(self, cedula_cliente, cedula_juridica_restaurante, numeros_combos):
        cliente = self.iniciar_sesion_cliente(cedula_cliente)
        restaurante = self._gestor_restaurantes.buscar_por_cedula(cedula_juridica_restaurante)
        if restaurante is None:
            raise ValueError("Restaurante no encontrado")
        return self._gestor_pedidos.crear_pedido(cliente, restaurante, self._gestor_repartidores, numeros_combos)

    def entregar_pedido(self, pedido, km_recorridos, es_feriado=False):
        factura = Factura(pedido, km_recorridos, es_feriado)
        pedido.estado = "entregado"
        pedido.repartidor.estado = "disponible"
        return factura

    def registrar_queja(self, cedula_repartidor, descripcion):
        repartidor = self._gestor_repartidores.buscar_por_cedula(cedula_repartidor)
        if repartidor is None:
            raise ValueError("Repartidor no encontrado")
        repartidor.agregar_queja(descripcion)

    @property
    def reportes(self):
        return self._generador_reportes