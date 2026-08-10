from Modelo.GestorBase import GestorBase
from Modelo.Pedido import Pedido


class GestorPedidos(GestorBase):

    def agregar(self, pedido):
        self._lista.append(pedido)

    def listar(self) -> list:
        return self._lista

    def buscar_por_cedula(self, cedula: str) -> list:
        return [p for p in self._lista if p.cliente.cedula == cedula]

    def buscar_por_id(self, id_pedido: int):
        for pedido in self._lista:
            if pedido.id == id_pedido:
                return pedido
        return None

    def crear_pedido(self, cliente, restaurante, gestor_repartidores, numeros_combos: list):
        if not cliente.esta_activo():
            raise PermissionError("El cliente está suspendido, no se acepta la solicitud")
        if not numeros_combos:
            raise ValueError("El pedido debe incluir al menos un combo")

        combos = [restaurante.menu.obtener_combo(n) for n in numeros_combos]

        repartidor = gestor_repartidores.primer_disponible()
        if repartidor is None:
            raise RuntimeError("No hay repartidores disponibles en este momento")

        pedido = Pedido(cliente, restaurante, repartidor, combos)
        repartidor.estado = "ocupado"
        self.agregar(pedido)
        return pedido