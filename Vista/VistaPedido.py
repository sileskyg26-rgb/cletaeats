import streamlit as st

class VistaPedido:

    def __init__(self, controlador_pedidos, controlador_restaurantes):
        self._controlador_pedidos = controlador_pedidos
        self._controlador_restaurantes = controlador_restaurantes

    def mostrar_formulario_pedido(self):
        st.header("Hacer pedido")

        cliente = st.session_state.get("cliente_actual")
        restaurantes = self._controlador_restaurantes.listar_restaurantes()

        if not restaurantes:
            st.info("Aun no hay restaurantes registrados")
            return

        nombres = [f"{r.nombre} ({r.tipo_comida})" for r in restaurantes]
        indice = st.selectbox(
            "Restaurante", range(len(restaurantes)),
            format_func=lambda i: nombres[i])
        restaurante = restaurantes[indice]

        combos, error = self._controlador_restaurantes.ver_menu(
            restaurante.cedula_juridica)
        if error:
            st.error(error)
            return
        if not combos:
            st.info("Este restaurante aun no tiene combos en su menu")
            return

        seleccionados = st.multiselect(
            "Combos deseados", combos, format_func=lambda c: str(c))

        if st.button("Confirmar pedido"):
            if not seleccionados:
                st.warning("Debe seleccionar al menos un combo")
                return

            numeros_combos = [combo.numero for combo in seleccionados]
            pedido, error = self._controlador_pedidos.hacer_pedido(
                cliente.cedula, restaurante.cedula_juridica, numeros_combos)

            if error:
                st.error(error)
            else:
                st.success(f"Pedido #{pedido.id} creado correctamente")
                st.write(pedido)

    def mostrar_pedidos_cliente(self):
        st.header("Mis pedidos")

        cliente = st.session_state.get("cliente_actual")
        pedidos = self._controlador_pedidos.listar_pedidos_cliente(cliente.cedula)

        if not pedidos:
            st.info("Todavia no ha realizado ningun pedido")
            return

        for pedido in pedidos:
            with st.expander(f"Pedido #{pedido.id} - Estado: {pedido.estado}"):
                st.write(f"Restaurante: {pedido.restaurante.nombre}")
                st.write(f"Repartidor: {pedido.repartidor.nombre}")
                for combo in pedido.combos:
                    st.write(combo)

                if pedido.estado != "entregado":
                    self._mostrar_formulario_entrega(pedido.id)

    def _mostrar_formulario_entrega(self, id_pedido: int):
        with st.form(f"form_entrega_{id_pedido}"):
            km_recorridos = st.number_input(
                "Kilometros recorridos", min_value=0.0, step=0.5)
            es_feriado = st.checkbox("Es dia feriado")
            enviar = st.form_submit_button("Marcar como entregado")

        if enviar:
            factura, error = self._controlador_pedidos.entregar_pedido(
                id_pedido, km_recorridos, es_feriado)
            if error:
                st.error(error)
            else:
                st.success("Pedido entregado, factura generada")
                st.text(str(factura))
                st.rerun()