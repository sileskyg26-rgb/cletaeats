from abc import ABC, abstractmethod
from Modelo.Validaciones import validar_cedula, validar_no_vacio, validar_telefono, validar_correo


# ABSTRACCIÓN: Usuario es una clase abstracta (ABC = Abstract Base Class).
# No se puede crear un Usuario "a secas" (Usuario() daría error), solo sirve
# como molde para Cliente y Repartidor, que sí se pueden instanciar.
class Usuario(ABC):

    def __init__(self, cedula: str, nombre: str, direccion: str,
                 telefono: str, correo: str):
        validar_cedula(cedula)
        validar_no_vacio(nombre, "El nombre")
        validar_no_vacio(direccion, "La dirección")
        validar_telefono(telefono)
        validar_correo(correo)
        # ENCAPSULACIÓN: los datos (cedula, nombre, etc.) y las validaciones
        # que los protegen viven juntos, dentro de la misma clase. Nadie de
        # afuera puede meter una cédula o un correo inválido a la fuerza,
        # porque siempre pasa primero por las validaciones de acá arriba.
        self._cedula = cedula
        self._nombre = nombre
        self._direccion = direccion
        self._telefono = telefono
        self._correo = correo
        print(f"[Usuario] Constructor: se creó {self._nombre} ({self._cedula})")

    def __del__(self):
        # Destructor: se ejecuta cuando el objeto es eliminado / recolectado por el GC
        nombre = getattr(self, "_nombre", "?")
        cedula = getattr(self, "_cedula", "?")
        print(f"[Usuario] Destructor: se eliminó {nombre} ({cedula})")

    # TIPO DE ACCESO: self._cedula (con un guion bajo) es "protegido" por
    # convención de Python: en teoría solo debería tocarse desde adentro de
    # la clase o sus hijas (Cliente, Repartidor). Lo que sí es público es
    # esta property de acá abajo: "cedula", sin guion bajo, que es la puerta
    # oficial para leer/cambiar el dato desde afuera (ej. Vista/Controlador).
    # (Python no tiene un "privado" real como Java; si quisiéramos algo más
    # cerrado usaríamos doble guion bajo, ej. self.__cedula).
    @property
    def cedula(self) -> str:
        return self._cedula

    @cedula.setter
    def cedula(self, valor: str):
        validar_cedula(valor)
        self._cedula = valor

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str):
        validar_no_vacio(valor, "El nombre")
        self._nombre = valor

    @property
    def direccion(self) -> str:
        return self._direccion

    @direccion.setter
    def direccion(self, valor: str):
        validar_no_vacio(valor, "La dirección")
        self._direccion = valor

    @property
    def telefono(self) -> str:
        return self._telefono

    @telefono.setter
    def telefono(self, valor: str):
        validar_telefono(valor)
        self._telefono = valor

    @property
    def correo(self) -> str:
        return self._correo

    @correo.setter
    def correo(self, valor: str):
        validar_correo(valor)
        self._correo = valor

    # ABSTRACCIÓN (método abstracto): esta clase obliga a que Cliente y
    # Repartidor implementen su propio registrar(), pero no dice cómo — cada
    # una decide su propia forma de "registrarse". Si a Cliente o Repartidor
    # se les olvida definirlo, Python ni los deja crear el objeto.
    @abstractmethod
    def registrar(self):
        """Cada subclase (Cliente, Repartidor) define cómo se registra."""
        pass

    def __str__(self) -> str:
        return (f"Cédula: {self._cedula} | Nombre: {self._nombre} | "
                f"Dirección: {self._direccion} | Tel: {self._telefono} | "
                f"Correo: {self._correo}")