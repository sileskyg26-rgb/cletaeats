from gestor_base import GestorBase


class GestorRestaurantes(GestorBase):
    

    def agregar(self, restaurante):
        # Regla de negocio: no se debe repetir cédula jurídica
        if self.buscar_por_cedula(restaurante.cedula_juridica) is not None:
            raise ValueError("Ya existe un restaurante con esa cédula jurídica")
        self._lista.append(restaurante)

    def listar(self) -> list:
        return self._lista

    def buscar_por_cedula(self, cedula_juridica: str):
        for restaurante in self._lista:
            if restaurante.cedula_juridica == cedula_juridica:
                return restaurante
        return None