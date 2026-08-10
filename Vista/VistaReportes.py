import streamlit as st

class VistaReportes:

    OPCIONES = [
        "Clientes activos",
        "Clientes suspendidos",
        "Repartidores sin amonestaciones",
        "Listado de restaurantes",
        "Restaurante con mas pedidos",
        "Restaurante con menos pedidos",
        "Monto total por restaurante",
        "Monto total general",
        "Quejas por repartidor",
        "Pedidos por cliente",
        "Cliente con mas pedidos",
        "Hora pico",
    ]

    def __init__(self, controlador_reportes):
        self._controlador_reportes = controlador_reportes

    def mostrar(self):
        st.header("Reportes")

        opcion = st.selectbox("Seleccione un reporte", self.OPCIONES)

        if st.button("Generar reporte"):
            self._mostrar_reporte(opcion)

    def _mostrar_reporte(self, opcion: str):
        if opcion == "Clientes activos":
            self._mostrar_lista_clientes(
                self._controlador_reportes.clientes_activos())

        elif opcion == "Clientes suspendidos":
            self._mostrar_lista_clientes(
                self._controlador_reportes.clientes_suspendidos())

        elif opcion == "Repartidores sin amonestaciones":
            repartidores = self._controlador_reportes.repartidores_sin_amonestaciones()
            if not repartidores:
                st.info("No hay repartidores sin amonestaciones")
            for repartidor in repartidores:
                st.write(str(repartidor))

        elif opcion == "Listado de restaurantes":
            restaurantes = self._controlador_reportes.listado_restaurantes()
            if not restaurantes:
                st.info("No hay restaurantes registrados")
            for restaurante in restaurantes:
                st.write(str(restaurante))

        elif opcion == "Restaurante con mas pedidos":
            restaurante = self._controlador_reportes.restaurante_mayor_pedidos()
            st.write(str(restaurante) if restaurante else "Sin pedidos registrados")

        elif opcion == "Restaurante con menos pedidos":
            restaurante = self._controlador_reportes.restaurante_menor_pedidos()
            st.write(str(restaurante) if restaurante else "Sin restaurantes registrados")

        elif opcion == "Monto total por restaurante":
            montos = self._controlador_reportes.monto_total_por_restaurante()
            if not montos:
                st.info("No hay ventas registradas")
            for nombre, monto in montos.items():
                st.write(f"{nombre}: {monto:,.2f}")

        elif opcion == "Monto total general":
            st.write(f"{self._controlador_reportes.monto_total_general():,.2f}")

        elif opcion == "Quejas por repartidor":
            quejas = self._controlador_reportes.quejas_por_repartidor()
            if not any(quejas.values()):
                st.info("No hay quejas registradas")
            for nombre, lista_quejas in quejas.items():
                with st.expander(nombre):
                    if lista_quejas:
                        for queja in lista_quejas:
                            st.write(queja)
                    else:
                        st.write("Sin quejas")

        elif opcion == "Pedidos por cliente":
            pedidos = self._controlador_reportes.pedidos_por_cliente()
            if not pedidos:
                st.info("No hay pedidos registrados")
            for nombre, lista_pedidos in pedidos.items():
                with st.expander(nombre):
                    for pedido in lista_pedidos:
                        st.write(str(pedido))

        elif opcion == "Cliente con mas pedidos":
            resultado = self._controlador_reportes.cliente_mayor_pedidos()
            if resultado:
                nombre, cantidad = resultado
                st.write(f"{nombre}: {cantidad} pedido(s)")
            else:
                st.info("No hay pedidos registrados")

        elif opcion == "Hora pico":
            resultado = self._controlador_reportes.hora_pico()
            if resultado:
                hora, cantidad = resultado
                st.write(f"Hora {hora}:00 - {cantidad} pedido(s)")
            else:
                st.info("No hay pedidos registrados")

    @staticmethod
    def _mostrar_lista_clientes(clientes: list):
        if not clientes:
            st.info("No hay clientes en este estado")
        for cliente in clientes:
            st.write(str(cliente))