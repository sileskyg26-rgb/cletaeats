from modelo.repartidor import Repartidor
from modelo.gestor_repartidores import GestorRepartidores


class ControladorRepartidores:

    def __init__(self, gestor_repartidores: GestorRepartidores):
        self._gestor_repartidores = gestor_repartidores
        print("[ControladorRepartidores] Constructor: controlador creado")

    def __del__(self):
        print("[ControladorRepartidores] Destructor: controlador eliminado")

    def registrar_repartidor(self, cedula: str, nombre: str, direccion: str,
                              telefono: str, correo: str,
                              numero_tarjeta: str):
        try:
            repartidor = Repartidor(cedula, nombre, direccion, telefono,
                                     correo, numero_tarjeta)
            self._gestor_repartidores.agregar(repartidor)
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
        return True, None

    def cambiar_estado(self, cedula_repartidor: str, nuevo_estado: str):
        repartidor = self._gestor_repartidores.buscar_por_cedula(
            cedula_repartidor)
        if repartidor is None:
            return False, "Repartidor no encontrado"
        try:
            repartidor.estado = nuevo_estado
            return True, None
        except ValueError as e:
            return False, str(e)