from abc import ABC, abstractmethod


class Usuario(ABC):
   
    def __init__(self, cedula: str, nombre: str, direccion: str,
                 telefono: str, correo: str):
        self._cedula = cedula
        self._nombre = nombre
        self._direccion = direccion
        self._telefono = telefono
        self._correo = correo
        print(f"[Usuario] Constructor: se creó {self._nombre} ({self._cedula})")

    def __del__(self):
        # Destructor: se ejecuta cuando el objeto es eliminado / recolectado por el GC
        print(f"[Usuario] Destructor: se eliminó {self._nombre} ({self._cedula})")

    @property
    def cedula(self) -> str:
        return self._cedula

    @cedula.setter
    def cedula(self, valor: str):
        self._cedula = valor

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str):
        self._nombre = valor

    @property
    def direccion(self) -> str:
        return self._direccion

    @direccion.setter
    def direccion(self, valor: str):
        self._direccion = valor

    @property
    def telefono(self) -> str:
        return self._telefono

    @telefono.setter
    def telefono(self, valor: str):
        self._telefono = valor

    @property
    def correo(self) -> str:
        return self._correo

    @correo.setter
    def correo(self, valor: str):
        self._correo = valor

    @abstractmethod
    def registrar(self):
        """Cada subclase (Cliente, Repartidor) define cómo se registra."""
        pass

    def __str__(self) -> str:
        return (f"Cédula: {self._cedula} | Nombre: {self._nombre} | "
                f"Dirección: {self._direccion} | Tel: {self._telefono} | "
                f"Correo: {self._correo}")