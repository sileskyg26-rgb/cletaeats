from gestor_base import GestorBase


class GestorRepartidores(GestorBase):

    def agregar(self, repartidor):
        if self.buscar_por_cedula(repartidor.cedula) is not None:
            raise ValueError("Ya existe un repartidor con esa cédula")
        self._lista.append(repartidor)

    def listar(self) -> list:
        return self._lista

    def buscar_por_cedula(self, cedula: str):
        for repartidor in self._lista:
            if repartidor.cedula == cedula:
                return repartidor
        return None

    def listar_sin_amonestaciones(self) -> list:
        return [r for r in self._lista if r.numero_amonestaciones == 0]

    def primer_disponible(self):
        for repartidor in self._lista:
            if repartidor.esta_disponible():
                return repartidor
        return None