from Modelo.Combo import Combo


# Esta es la clase Menu que pide el enunciado: agrupa todos los Combos
# de UN restaurante. En vez de que Restaurante guarde una lista de combos
# suelta por su cuenta, le delegamos esa responsabilidad a esta clase
# aparte (así cada clase hace una sola cosa y la hace bien).
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