from modelo.restaurante import Restaurante
from modelo.combo import Combo
from modelo.gestor_restaurantes import GestorRestaurantes


class ControladorRestaurantes:

    def __init__(self, gestor_restaurantes: GestorRestaurantes):
        self._gestor_restaurantes = gestor_restaurantes
        print("[ControladorRestaurantes] Constructor: controlador creado")

    def __del__(self):
        print("[ControladorRestaurantes] Destructor: controlador eliminado")

    def registrar_restaurante(self, nombre: str, cedula_juridica: str,
                               direccion: str, tipo_comida: str):
        try:
            restaurante = Restaurante(nombre, cedula_juridica,
                                       direccion, tipo_comida)
            self._gestor_restaurantes.agregar(restaurante)
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
            return True, None
        except ValueError as e:
            return False, str(e)

    def ver_menu(self, cedula_juridica: str):
        restaurante = self._gestor_restaurantes.buscar_por_cedula(
            cedula_juridica)
        if restaurante is None:
            return None, "Restaurante no encontrado"
        return restaurante.menu.listar_combos(), None

    def listar_restaurantes(self) -> list:
        return self._gestor_restaurantes.listar()

    def buscar_restaurante(self, cedula_juridica: str):
        return self._gestor_restaurantes.buscar_por_cedula(cedula_juridica)