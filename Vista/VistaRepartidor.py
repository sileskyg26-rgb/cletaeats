import streamlit as st

class VistaRepartidor:

    def __init__(self, controlador_repartidores):
        self._controlador_repartidores = controlador_repartidores

    def mostrar(self):
        st.header("Repartidores")

        tab_listado, tab_registro, tab_queja = st.tabs(
            ["Ver repartidores", "Registrar repartidor", "Registrar queja"])

        with tab_listado:
            self._mostrar_listado()

        with tab_registro:
            self._mostrar_formulario_registro()

        with tab_queja:
            self._mostrar_formulario_queja()

    def _mostrar_listado(self):
        repartidores = self._controlador_repartidores.listar_repartidores()

        if not repartidores:
            st.info("Aun no hay repartidores registrados")
            return

        mostrar_solo_sin_amonestaciones = st.checkbox(
            "Mostrar solo repartidores sin amonestaciones")

        if mostrar_solo_sin_amonestaciones:
            repartidores = self._controlador_repartidores.listar_sin_amonestaciones()
            if not repartidores:
                st.info("No hay repartidores sin amonestaciones")
                return

        for repartidor in repartidores:
            st.write(str(repartidor))

    def _mostrar_formulario_registro(self):
        with st.form("form_registro_repartidor"):
            cedula = st.text_input("Cedula")
            nombre = st.text_input("Nombre completo")
            direccion = st.text_input("Direccion exacta")
            telefono = st.text_input("Numero de celular")
            correo = st.text_input("Correo electronico")
            numero_tarjeta = st.text_input("Numero de tarjeta")
            enviar = st.form_submit_button("Registrar")

        if enviar:
            if not all([cedula, nombre, direccion, telefono, correo,
                        numero_tarjeta]):
                st.warning("Todos los campos son obligatorios")
                return

            repartidor, error = self._controlador_repartidores.registrar_repartidor(
                cedula, nombre, direccion, telefono, correo, numero_tarjeta)
            if error:
                st.error(error)
            else:
                st.success(f"Repartidor {repartidor.nombre} registrado correctamente")
                st.rerun()

    def _mostrar_formulario_queja(self):
        repartidores = self._controlador_repartidores.listar_repartidores()

        if not repartidores:
            st.info("Aun no hay repartidores registrados")
            return

        nombres = [f"{r.nombre} ({r.cedula})" for r in repartidores]

        with st.form("form_queja"):
            indice = st.selectbox(
                "Repartidor", range(len(repartidores)),
                format_func=lambda i: nombres[i])
            descripcion = st.text_area("Descripcion de la queja")
            enviar = st.form_submit_button("Registrar queja")

        if enviar:
            if not descripcion:
                st.warning("Debe describir la queja")
                return

            cliente = st.session_state.get("cliente_actual")
            cedula_cliente = cliente.cedula if cliente else ""
            repartidor = repartidores[indice]

            exito, error = self._controlador_repartidores.registrar_queja(
                repartidor.cedula, descripcion, cedula_cliente)
            if error:
                st.error(error)
            else:
                st.success("Queja registrada")
                st.rerun()