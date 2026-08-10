import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st

from Controlador.ControladorPrincipal import ControladorPrincipal
from Controlador.ControladorClientes import ControladorClientes
from Controlador.ControladorRestaurantes import ControladorRestaurantes
from Controlador.ControladorRepartidores import ControladorRepartidores
from Controlador.ControladorPedidos import ControladorPedidos
from Controlador.ControladorReportes import ControladorReportes

from Vista.VistaLogin import VistaLogin
from Vista.VistaMenuPrincipal import VistaMenuPrincipal
from Vista.VistaRestaurante import VistaRestaurante
from Vista.VistaRepartidor import VistaRepartidor
from Vista.VistaPedido import VistaPedido
from Vista.VistaReportes import VistaReportes


class App:

    def __init__(self):
        self._inicializar_controladores()
        self._inicializar_vistas()

    def _inicializar_controladores(self):
        if "controlador_principal" not in st.session_state:
            st.session_state["controlador_principal"] = ControladorPrincipal()

        principal = st.session_state["controlador_principal"]

        # CREACIÓN DE OBJETOS: acá es donde se instancian los objetos
        # principales del sistema (cada Controlador es un objeto nuevo,
        # creado a partir de su clase con paréntesis, como Cliente() o
        # Combo() en cualquier otro lado del código). Como esto es una app
        # de Streamlit y no un script de consola, este método hace el papel
        # que haría un "main": es el punto donde arranca todo.
        self._controlador_clientes = ControladorClientes(principal.gestor_clientes, principal)
        self._controlador_restaurantes = ControladorRestaurantes(principal.gestor_restaurantes, principal)
        self._controlador_repartidores = ControladorRepartidores(principal.gestor_repartidores, principal)
        self._controlador_pedidos = ControladorPedidos(
            principal.gestor_pedidos,
            principal.gestor_clientes,
            principal.gestor_restaurantes,
            principal.gestor_repartidores,
            principal,
        )
        self._controlador_reportes = ControladorReportes(principal.reportes)

    def _inicializar_vistas(self):
        self._vista_login = VistaLogin(self._controlador_clientes)
        self._vista_restaurante = VistaRestaurante(self._controlador_restaurantes)
        self._vista_repartidor = VistaRepartidor(self._controlador_repartidores)
        self._vista_pedido = VistaPedido(self._controlador_pedidos, self._controlador_restaurantes)
        self._vista_reportes = VistaReportes(self._controlador_reportes)
        self._vista_menu_principal = VistaMenuPrincipal(
            self._vista_restaurante, self._vista_repartidor,
            self._vista_pedido, self._vista_reportes
        )

    def ejecutar(self):
        st.set_page_config(page_title="CletaEats", layout="wide")

        if "cliente_actual" not in st.session_state:
            self._vista_login.mostrar()
        else:
            self._vista_menu_principal.mostrar()


# Este if es el equivalente en Python al "main" de otros lenguajes: el
# código de acá adentro solo corre cuando este archivo se ejecuta
# directamente (streamlit run Vista/app.py), no cuando otro archivo lo
# importa. App() crea el objeto principal de la aplicación.
if __name__ == "__main__":
    App().ejecutar()