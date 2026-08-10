import streamlit as st


class VistaLogin:

    def __init__(self, controlador_clientes):
        self._controlador_clientes = controlador_clientes

    def mostrar(self):
        st.title("CletaEats")
        st.subheader("Inicio de sesion")

        tab_login, tab_registro = st.tabs(["Iniciar sesion", "Registrarme"])

        with tab_login:
            self._mostrar_formulario_login()

        with tab_registro:
            self._mostrar_formulario_registro()

    def _mostrar_formulario_login(self):
        with st.form("form_login"):
            cedula = st.text_input("Cedula", key="login_cedula")
            enviar = st.form_submit_button("Ingresar")

        if enviar:
            if not cedula:
                st.warning("Debe ingresar su cedula")
                return

            cliente, error = self._controlador_clientes.iniciar_sesion(cedula)
            if error:
                st.error(error)
            else:
                st.session_state["cliente_actual"] = cliente
                st.success(f"Bienvenido, {cliente.nombre}")
                st.rerun()

    def _mostrar_formulario_registro(self):
        with st.form("form_registro_cliente"):
            cedula = st.text_input("Cedula")
            nombre = st.text_input("Nombre completo")
            direccion = st.text_input("Direccion exacta")
            telefono = st.text_input("Numero de celular")
            correo = st.text_input("Correo electronico")
            numero_tarjeta = st.text_input("Numero de tarjeta")
            enviar = st.form_submit_button("Registrarme")

        if enviar:
            if not all([cedula, nombre, direccion, telefono, correo,
                        numero_tarjeta]):
                st.warning("Todos los campos son obligatorios")
                return

            cliente, error = self._controlador_clientes.registrar_cliente(
                cedula, nombre, direccion, telefono, correo, numero_tarjeta)
            if error:
                st.error(error)
            else:
                st.session_state["cliente_actual"] = cliente
                st.success(f"Cliente {cliente.nombre} registrado correctamente")
                st.rerun()