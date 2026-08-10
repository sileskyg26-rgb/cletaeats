import streamlit as st

class VistaRestaurante:

    def __init__(self, controlador_restaurantes):
        self._controlador_restaurantes = controlador_restaurantes

    def mostrar(self):
        st.header("Restaurantes")

        tab_listado, tab_registro = st.tabs(
            ["Ver restaurantes", "Registrar restaurante"])

        with tab_listado:
            self._mostrar_listado()

        with tab_registro:
            self._mostrar_formulario_registro()

    def _mostrar_listado(self):
        restaurantes = self._controlador_restaurantes.listar_restaurantes()

        if not restaurantes:
            st.info("Aun no hay restaurantes registrados")
            return

        nombres = [f"{r.nombre} ({r.tipo_comida})" for r in restaurantes]
        indice = st.selectbox(
            "Seleccione un restaurante", range(len(restaurantes)),
            format_func=lambda i: nombres[i])
        restaurante = restaurantes[indice]

        st.write(f"Direccion: {restaurante.direccion}")
        st.write(f"Tipo de comida: {restaurante.tipo_comida}")

        st.subheader("Menu")
        combos, error = self._controlador_restaurantes.ver_menu(
            restaurante.cedula_juridica)
        if error:
            st.error(error)
        elif not combos:
            st.info("Este restaurante aun no tiene combos en su menu")
        else:
            for combo in combos:
                st.write(str(combo))

        self._mostrar_formulario_agregar_combo(restaurante.cedula_juridica)

    def _mostrar_formulario_agregar_combo(self, cedula_juridica: str):
        with st.expander("Agregar combo al menu"):
            with st.form(f"form_combo_{cedula_juridica}"):
                numero = st.number_input(
                    "Numero de combo (1-9)", min_value=1, max_value=9, step=1)
                descripcion = st.text_input("Descripcion del combo")
                enviar = st.form_submit_button("Agregar combo")

            if enviar:
                if not descripcion:
                    st.warning("Debe indicar una descripcion")
                    return
                exito, error = self._controlador_restaurantes.agregar_combo(
                    cedula_juridica, int(numero), descripcion)
                if error:
                    st.error(error)
                else:
                    st.success("Combo agregado correctamente")
                    st.rerun()

    def _mostrar_formulario_registro(self):
        with st.form("form_registro_restaurante"):
            nombre = st.text_input("Nombre del restaurante")
            cedula_juridica = st.text_input("Cedula juridica")
            direccion = st.text_input("Direccion")
            tipo_comida = st.text_input("Tipo de comida (rapida, china, saludable, etc)")
            enviar = st.form_submit_button("Registrar")

        if enviar:
            if not all([nombre, cedula_juridica, direccion, tipo_comida]):
                st.warning("Todos los campos son obligatorios")
                return
            restaurante, error = self._controlador_restaurantes.registrar_restaurante(
                nombre, cedula_juridica, direccion, tipo_comida)
            if error:
                st.error(error)
            else:
                st.success(f"Restaurante {restaurante.nombre} registrado correctamente")
                st.rerun()