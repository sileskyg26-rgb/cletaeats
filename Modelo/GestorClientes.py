from Modelo.GestorBase import GestorBase


class GestorClientes(GestorBase):


    def agregar(self, cliente):
        # Regla de negocio: no se debe repetir cédula
        if self.buscar_por_cedula(cliente.cedula) is not None:
            raise ValueError("Ya existe un cliente con esa cédula")
        self._lista.append(cliente)

    def listar(self) -> list:
        return self._lista

    def buscar_por_cedula(self, cedula: str):
        for cliente in self._lista:
            if cliente.cedula == cedula:
                return cliente
        return None


    def listar_activos(self) -> list:
        return [c for c in self._lista if c.estado == "activo"]

    def listar_suspendidos(self) -> list:
        return [c for c in self._lista if c.estado == "suspendido"]