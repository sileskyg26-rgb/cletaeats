from abc import ABC, abstractmethod


class ManejadorArchivo(ABC):

    @abstractmethod
    def guardar(self, lista_diccionarios: list):
        pass

    @abstractmethod
    def cargar(self) -> list:
        pass