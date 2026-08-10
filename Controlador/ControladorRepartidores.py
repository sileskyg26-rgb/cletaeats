from Modelo.Repartidor import Repartidor
from Modelo.GestorRepartidores import GestorRepartidores


class ControladorRepartidores:

    def __init__(self, gestor_repartidores: GestorRepartidores, controlador_principal=None):
        self._gestor_repartidores = gestor_repartidores
        self._controlador_principal = controlador_principal
        print("[ControladorRepartidores] Constructor: controlador creado")

    def __del__(self):
        print("[ControladorRepartidores] Destructor: controlador eliminado")

    def _guardar(self):
        if self._controlador_principal is not None:
            self._controlador_principal.guardar_todo()

    def registrar_repartidor(self, cedula: str, nombre: str, direccion: str,
                              telefono: str, correo: str,
                              numero_tarjeta: str):
        try:
            repartidor = Repartidor(cedula, nombre, direccion, telefono,
                                     correo, numero_tarjeta)
            self._gestor_repartidores.agregar(repartidor)
            self._guardar()
            return repartidor, None
        except ValueError as e:
            return None, str(e)

    def listar_repartidores(self) -> list:
        return self._gestor_repartidores.listar()

    def listar_sin_amonestaciones(self) -> list:
        return self._gestor_repartidores.listar_sin_amonestaciones()

    def registrar_queja(self, cedula_repartidor: str, descripcion: str,
                         cedula_cliente: str = ""):
        repartidor = self._gestor_repartidores.buscar_por_cedula(
            cedula_repartidor)
        if repartidor is None:
            return False, "Repartidor no encontrado"
        repartidor.agregar_queja(descripcion, cedula_cliente)
        self._guardar()
        return True, None

    def cambiar_estado(self, cedula_repartidor: str, nuevo_estado: str):
        repartidor = self._gestor_repartidores.buscar_por_cedula(
            cedula_repartidor)
        if repartidor is None:
            return False, "Repartidor no encontrado"
        try:
            repartidor.estado = nuevo_estado
            self._guardar()
            return True, None
        except ValueError as e:
            return False, str(e)