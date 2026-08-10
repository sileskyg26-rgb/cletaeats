from abc import ABC, abstractmethod


class GestorBase(ABC):
   

    def __init__(self):
        self._lista = []
        print(f"[{self.__class__.__name__}] Constructor: gestor creado")

    def __del__(self):
        print(f"[{self.__class__.__name__}] Destructor: gestor eliminado")

    # ---------- Métodos abstractos ----------
    @abstractmethod
    def agregar(self, elemento):
        """Cada Gestor hijo define sus propias validaciones antes de agregar."""
        pass

    @abstractmethod
    def listar(self) -> list:
        """Devuelve la lista completa manejada por el Gestor."""
        pass

    @abstractmethod
    def buscar_por_cedula(self, cedula: str):
        """Busca un elemento por su identificador (cédula, cédula jurídica,
        o cédula del cliente dueño del pedido, según el Gestor)."""
        pass

    # ---------- Método concreto compartido ----------
    def cantidad(self) -> int:
        return len(self._lista)