import os

from Modelo.GestorClientes import GestorClientes
from Modelo.GestorRestaurantes import GestorRestaurantes
from Modelo.GestorRepartidores import GestorRepartidores
from Modelo.GestorPedidos import GestorPedidos
from Modelo.GeneradorReportes import GeneradorReportes
from Modelo.ArchivoTexto import ArchivoTexto

from Modelo.Cliente import Cliente
from Modelo.Restaurante import Restaurante
from Modelo.Repartidor import Repartidor
from Modelo.Combo import Combo


CARPETA_DATOS = os.path.join(os.path.dirname(__file__), "..", "datos")


class ControladorPrincipal:

    def __init__(self):
        # ---- Gestores (lógica de negocio) ----
        self._gestor_clientes = GestorClientes()
        self._gestor_restaurantes = GestorRestaurantes()
        self._gestor_repartidores = GestorRepartidores()
        self._gestor_pedidos = GestorPedidos()
        self._generador_reportes = GeneradorReportes(
            self._gestor_clientes, self._gestor_restaurantes,
            self._gestor_repartidores, self._gestor_pedidos)

        # ---- Persistencia (acceso a datos) ----
        self._archivo_clientes = ArchivoTexto(
            os.path.join(CARPETA_DATOS, "clientes.txt"))
        self._archivo_restaurantes = ArchivoTexto(
            os.path.join(CARPETA_DATOS, "restaurantes.txt"))
        self._archivo_repartidores = ArchivoTexto(
            os.path.join(CARPETA_DATOS, "repartidores.txt"))

        self.cargar_todo()
        print("[ControladorPrincipal] Constructor: sistema listo")

    def __del__(self):
        print("[ControladorPrincipal] Destructor: sistema cerrado")

    # ---------- Propiedades de solo lectura (para los demás controladores) ----------
    @property
    def gestor_clientes(self) -> GestorClientes:
        return self._gestor_clientes

    @property
    def gestor_restaurantes(self) -> GestorRestaurantes:
        return self._gestor_restaurantes

    @property
    def gestor_repartidores(self) -> GestorRepartidores:
        return self._gestor_repartidores

    @property
    def gestor_pedidos(self) -> GestorPedidos:
        return self._gestor_pedidos

    @property
    def reportes(self) -> GeneradorReportes:
        return self._generador_reportes

    # ---------- Persistencia ----------
    def guardar_todo(self):
        """Vuelca clientes, restaurantes y repartidores a archivo de texto.
        No sobrescribe pedidos: el enunciado los reconstruye en memoria en
        cada corrida a partir de las cédulas/combos, ya que Pedido guarda
        referencias a objetos (Cliente, Restaurante, Repartidor)."""
        try:
            self._archivo_clientes.guardar([
                {
                    "cedula": c.cedula, "nombre": c.nombre,
                    "direccion": c.direccion, "telefono": c.telefono,
                    "correo": c.correo, "numero_tarjeta": c.numero_tarjeta,
                    "estado": c.estado,
                }
                for c in self._gestor_clientes.listar()
            ])

            self._archivo_restaurantes.guardar([
                {
                    "nombre": r.nombre, "cedula_juridica": r.cedula_juridica,
                    "direccion": r.direccion, "tipo_comida": r.tipo_comida,
                    "combos": ";".join(
                        f"{c.numero}:{c.descripcion}" for c in r.menu.combos),
                }
                for r in self._gestor_restaurantes.listar()
            ])

            self._archivo_repartidores.guardar([
                {
                    "cedula": rep.cedula, "nombre": rep.nombre,
                    "direccion": rep.direccion, "telefono": rep.telefono,
                    "correo": rep.correo,
                    "numero_tarjeta": rep.numero_tarjeta,
                    "estado": rep.estado,
                    "numero_amonestaciones": rep.numero_amonestaciones,
                }
                for rep in self._gestor_repartidores.listar()
            ])
            return True, None
        except Exception as e:
            return False, str(e)

    def cargar_todo(self):
        """Reconstruye clientes, restaurantes y repartidores desde archivo
        al arrancar el sistema."""
        try:
            for datos in self._archivo_clientes.cargar():
                cliente = Cliente(
                    datos["cedula"], datos["nombre"], datos["direccion"],
                    datos["telefono"], datos["correo"],
                    datos["numero_tarjeta"], datos.get("estado", "activo"))
                self._gestor_clientes.agregar(cliente)

            for datos in self._archivo_restaurantes.cargar():
                restaurante = Restaurante(
                    datos["nombre"], datos["cedula_juridica"],
                    datos["direccion"], datos["tipo_comida"])
                combos_str = datos.get("combos", "")
                if combos_str:
                    for par in combos_str.split(";"):
                        numero_str, _, descripcion = par.partition(":")
                        restaurante.menu.agregar_combo(
                            Combo(int(numero_str), descripcion))
                self._gestor_restaurantes.agregar(restaurante)

            for datos in self._archivo_repartidores.cargar():
                repartidor = Repartidor(
                    datos["cedula"], datos["nombre"], datos["direccion"],
                    datos["telefono"], datos["correo"],
                    datos["numero_tarjeta"],
                    datos.get("estado", "disponible"))
                self._gestor_repartidores.agregar(repartidor)
            return True, None
        except Exception as e:
            return False, str(e)