from Modelo.Cliente import Cliente
from Modelo.GestorClientes import GestorClientes


class ControladorClientes:

    def __init__(self, gestor_clientes: GestorClientes):
        self._gestor_clientes = gestor_clientes
        print("[ControladorClientes] Constructor: controlador creado")

    def __del__(self):
        print("[ControladorClientes] Destructor: controlador eliminado")

    def registrar_cliente(self, cedula: str, nombre: str, direccion: str,
                           telefono: str, correo: str, numero_tarjeta: str):
        try:
            cliente = Cliente(cedula, nombre, direccion, telefono,
                               correo, numero_tarjeta)
            self._gestor_clientes.agregar(cliente)
            return cliente, None
        except ValueError as e:
            return None, str(e)

    def iniciar_sesion(self, cedula: str):
        cliente = self._gestor_clientes.buscar_por_cedula(cedula)
        if cliente is None:
            return None, "Cliente no registrado, debe inscribirse primero"
        if not cliente.esta_activo():
            return None, "Cliente suspendido: no se acepta la solicitud"
        return cliente, None

    def listar_clientes(self) -> list:
        return self._gestor_clientes.listar()

    def listar_activos(self) -> list:
        return self._gestor_clientes.listar_activos()

    def listar_suspendidos(self) -> list:
        return self._gestor_clientes.listar_suspendidos()

    def suspender_cliente(self, cedula: str):
        cliente = self._gestor_clientes.buscar_por_cedula(cedula)
        if cliente is None:
            return False, "Cliente no encontrado"
        try:
            cliente.estado = "suspendido"
            return True, None
        except ValueError as e:
            return False, str(e)

    def activar_cliente(self, cedula: str):
        cliente = self._gestor_clientes.buscar_por_cedula(cedula)
        if cliente is None:
            return False, "Cliente no encontrado"
        try:
            cliente.estado = "activo"
            return True, None
        except ValueError as e:
            return False, str(e)