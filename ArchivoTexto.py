import os
from manejador_archivos import ManejadorArchivos


class ArchivoTexto(ManejadorArchivos):

    def __init__(self, ruta_archivo: str):
        self._ruta_archivo = ruta_archivo
        carpeta = os.path.dirname(self._ruta_archivo)
        if carpeta and not os.path.exists(carpeta):
            os.makedirs(carpeta)
        if not os.path.exists(self._ruta_archivo):
            open(self._ruta_archivo, "w", encoding="utf-8").close()
        print(f"[ArchivoTexto] Constructor: archivo {ruta_archivo} listo")

    def __del__(self):
        print("[ArchivoTexto] Destructor: archivo cerrado")

    def guardar(self, lista_diccionarios: list):
        with open(self._ruta_archivo, "w", encoding="utf-8") as f:
            for diccionario in lista_diccionarios:
                linea = "|".join(f"{clave}={valor}" for clave, valor in diccionario.items())
                f.write(linea + "\n")

    def cargar(self) -> list:
        resultado = []
        with open(self._ruta_archivo, "r", encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if not linea:
                    continue
                diccionario = {}
                for par in linea.split("|"):
                    clave, _, valor = par.partition("=")
                    diccionario[clave] = valor
                resultado.append(diccionario)
        return resultado