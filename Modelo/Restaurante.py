from MenuRestaurante import MenuRestaurante


class Restaurante:

    def __init__(self, nombre: str = "", cedula_juridica: str = "",
                 direccion: str = "", tipo_comida: str = ""):
        self._nombre = nombre
        self._cedula_juridica = cedula_juridica
        self._direccion = direccion
        self._tipo_comida = tipo_comida
        self._menu = MenuRestaurante()
        print(f"[Restaurante] Constructor: {self._nombre} inscrito")

    def __del__(self):
        nombre = getattr(self, "_nombre", "?")
        print(f"[Restaurante] Destructor: se eliminó el restaurante {nombre}")

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str):
        self._nombre = valor

    @property
    def cedula_juridica(self) -> str:
        return self._cedula_juridica

    @cedula_juridica.setter
    def cedula_juridica(self, valor: str):
        self._cedula_juridica = valor

    @property
    def direccion(self) -> str:
        return self._direccion

    @direccion.setter
    def direccion(self, valor: str):
        self._direccion = valor

    @property
    def tipo_comida(self) -> str:
        return self._tipo_comida

    @tipo_comida.setter
    def tipo_comida(self, valor: str):
        self._tipo_comida = valor

    @property
    def menu(self) -> MenuRestaurante:
        return self._menu

    def __str__(self) -> str:
        return (f"Restaurante: {self._nombre} ({self._tipo_comida}) | "
                f"Cédula jurídica: {self._cedula_juridica} | Dirección: {self._direccion}")