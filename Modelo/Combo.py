class Combo:

    PRECIO_BASE = 4000
    INCREMENTO = 1000

    def __init__(self, numero: int = 1, descripcion: str = ""):
        if not 1 <= numero <= 9:
            raise ValueError("El número de combo debe estar entre 1 y 9")
        self._numero = numero
        self._descripcion = descripcion
        print(f"[Combo] Constructor: combo #{self._numero} creado")

    def __del__(self):
        numero = getattr(self, "_numero", "?")
        print(f"[Combo] Destructor: se eliminó el combo #{numero}")

    @property
    def numero(self) -> int:
        return self._numero

    @property
    def descripcion(self) -> str:
        return self._descripcion

    @descripcion.setter
    def descripcion(self, valor: str):
        self._descripcion = valor

    # OCULTAMIENTO: quien usa combo.precio no tiene ni idea (ni le importa)
    # que por detrás hay una fórmula (PRECIO_BASE + incremento por combo).
    # Para el que lo usa, "precio" se ve igual que si fuera un dato guardado
    # de una. Si mañana cambiamos la fórmula, nadie afuera se entera ni hay
    # que tocar nada más — el cálculo queda escondido acá adentro.
    @property
    def precio(self) -> float:
        return self.PRECIO_BASE + (self._numero - 1) * self.INCREMENTO

    # __str__ (el "toString" de Python): define qué se imprime cuando
    # hacés print(combo) o str(combo), en vez del típico texto feo tipo
    # "<Combo object at 0x000001A2B...>". Cada clase del proyecto tiene el
    # suyo (Cliente, Pedido, Factura...), pero este es el ejemplo más corto.
    def __str__(self) -> str:
        return f"Combo #{self._numero} ({self._descripcion}) - ₡{self.precio:,.2f}"