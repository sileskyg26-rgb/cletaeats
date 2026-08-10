from queja import Queja


class ListaQuejas:

    def __init__(self):
        self._quejas = []
        print("[ListaQuejas] Constructor: lista creada")

    def __del__(self):
        print("[ListaQuejas] Destructor: se eliminó la lista")

    @property
    def quejas(self) -> list:
        return self._quejas

    def agregar_queja(self, queja: Queja):
        if not isinstance(queja, Queja):
            raise TypeError("Solo se pueden agregar objetos Queja")
        self._quejas.append(queja)

    def cantidad(self) -> int:
        return len(self._quejas)

    def listar(self) -> list:
        return [str(q) for q in self._quejas]

    def __str__(self) -> str:
        return "\n".join(self.listar()) if self._quejas else "Sin quejas registradas"