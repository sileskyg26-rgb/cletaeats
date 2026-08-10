from Combo import Combo


class MenuRestaurante:

    def __init__(self):
        self._combos = []
        print("[MenuRestaurante] Constructor: menú creado")

    def __del__(self):
        print("[MenuRestaurante] Destructor: se eliminó el menú")

    @property
    def combos(self) -> list:
        return self._combos

    def agregar_combo(self, combo: Combo):
        self._combos.append(combo)

    def obtener_combo(self, numero: int) -> Combo:
        for combo in self._combos:
            if combo.numero == numero:
                return combo
        raise ValueError(f"El menú no tiene el combo #{numero}")

    def listar_combos(self) -> list:
        return [str(combo) for combo in self._combos]

    def __str__(self) -> str:
        return "\n".join(self.listar_combos()) if self._combos else "Menú vacío"