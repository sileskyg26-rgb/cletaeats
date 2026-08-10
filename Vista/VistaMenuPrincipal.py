import streamlit as st

class VistaMenuPrincipal:

    OPCIONES = [
        "Restaurantes",
        "Repartidores",
        "Hacer pedido",
        "Mis pedidos",
        "Reportes",
        "Cerrar sesion",
    ]

    def __init__(self, vista_restaurante, vista_repartidor, vista_pedido, vista_reportes):
        self._vista_restaurante = vista_restaurante
        self._vista_repartidor = vista_repartidor
        self._vista_pedido = vista_pedido
        self._vista_reportes = vista_reportes

    def mostrar(self):
        cliente = st.session_state.get("cliente_actual")

        st.sidebar.title("CletaEats")
        st.sidebar.write(f"Cliente: {cliente.nombre}")
        opcion = st.sidebar.radio("Menu", self.OPCIONES)

        if opcion == "Restaurantes":
            self._vista_restaurante.mostrar()
        elif opcion == "Repartidores":
            self._vista_repartidor.mostrar()
        elif opcion == "Hacer pedido":
            self._vista_pedido.mostrar_formulario_pedido()
        elif opcion == "Mis pedidos":
            self._vista_pedido.mostrar_pedidos_cliente()
        elif opcion == "Reportes":
            self._vista_reportes.mostrar()
        elif opcion == "Cerrar sesion":
            self._cerrar_sesion()

    def _cerrar_sesion(self):
        st.session_state.pop("cliente_actual", None)
        st.rerun()