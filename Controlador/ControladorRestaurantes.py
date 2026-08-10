from Modelo.Restaurante import Restaurante
from Modelo.Combo import Combo
from Modelo.GestorRestaurantes import GestorRestaurantes

class ControladorRestaurantes:

    def __init__(self, gestor_restaurantes: GestorRestaurantes, controlador_principal=None):
        self._gestor_restaurantes = gestor_restaurantes
        self._controlador_principal = controlador_principal
        print("[ControladorRestaurantes] Constructor: controlador creado")

    def __del__(self):
        print("[ControladorRestaurantes] Destructor: controlador eliminado")

    def _guardar(self):
        if self._controlador_principal is not None:
            self._controlador_principal.guardar_todo()

    def registrar_restaurante(self, nombre: str, cedula_juridica: str,
                               direccion: str, tipo_comida: str):
        try:
            restaurante = Restaurante(nombre, cedula_juridica,
                                       direccion, tipo_comida)
            self._gestor_restaurantes.agregar(restaurante)
            self._guardar()
            return restaurante, None
        except ValueError as e:
            return None, str(e)

    def agregar_combo(self, cedula_juridica: str, numero: int,
                       descripcion: str):
        restaurante = self._gestor_restaurantes.buscar_por_cedula(
            cedula_juridica)
        if restaurante is None:
            return False, "Restaurante no encontrado"
        try:
            combo = Combo(numero, descripcion)
            restaurante.menu.agregar_combo(combo)
            self._guardar()
            return True, None
        except ValueError as e:
            return False, str(e)

    def ver_menu(self, cedula_juridica: str):
        """Devuelve la lista de objetos Combo del restaurante (no texto),
        para que la vista use combo.numero, combo.descripcion y combo.precio
        sin depender del formato de __str__."""
        restaurante = self._gestor_restaurantes.buscar_por_cedula(
            cedula_juridica)
        if restaurante is None:
            return None, "Restaurante no encontrado"
        return restaurante.menu.combos, None

    def listar_restaurantes(self) -> list:
        return self._gestor_restaurantes.listar()

    def buscar_restaurante(self, cedula_juridica: str):
        return self._gestor_restaurantes.buscar_por_cedula(cedula_juridica)