from datetime import datetime


class Queja:

    def __init__(self, descripcion: str = "", cedula_cliente: str = "", fecha: datetime = None):
        self._descripcion = descripcion
        self._cedula_cliente = cedula_cliente
        self._fecha = fecha if fecha is not None else datetime.now()
        print(f"[Queja] Constructor: queja registrada")

    def __del__(self):
        print("[Queja] Destructor: se eliminó la queja")

    @property
    def descripcion(self) -> str:
        return self._descripcion

    @property
    def cedula_cliente(self) -> str:
        return self._cedula_cliente

    @property
    def fecha(self) -> datetime:
        return self._fecha

    def __str__(self) -> str:
        return f"[{self._fecha.strftime('%d/%m/%Y %H:%M')}] {self._descripcion}"