import re

PATRON_CEDULA = re.compile(r"^\d[\d-]{6,14}\d$")
PATRON_TELEFONO = re.compile(r"^\d[\d-]{5,10}\d$")
PATRON_CORREO = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
PATRON_TARJETA = re.compile(r"^\d[\d-]{10,20}\d$")


def validar_no_vacio(valor: str, nombre_campo: str):
    if not valor or not str(valor).strip():
        raise ValueError(f"{nombre_campo} no puede estar vacío")


def validar_cedula(valor: str, nombre_campo: str = "La cédula"):
    validar_no_vacio(valor, nombre_campo)
    if not PATRON_CEDULA.match(valor):
        raise ValueError(f"{nombre_campo} debe contener solo números y guiones (mínimo 8 dígitos)")


def validar_telefono(valor: str):
    validar_no_vacio(valor, "El teléfono")
    if not PATRON_TELEFONO.match(valor):
        raise ValueError("El teléfono debe contener solo números y guiones (mínimo 7 dígitos)")


def validar_correo(valor: str):
    validar_no_vacio(valor, "El correo")
    if not PATRON_CORREO.match(valor):
        raise ValueError("El correo electrónico no tiene un formato válido")


def validar_numero_tarjeta(valor: str):
    validar_no_vacio(valor, "El número de tarjeta")
    if not PATRON_TARJETA.match(valor):
        raise ValueError("El número de tarjeta debe contener solo números y guiones (mínimo 12 dígitos)")
