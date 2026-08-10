from collections import Counter


class GeneradorReportes:

    def __init__(self, gestor_clientes, gestor_restaurantes, gestor_repartidores, gestor_pedidos):
        self._gestor_clientes = gestor_clientes
        self._gestor_restaurantes = gestor_restaurantes
        self._gestor_repartidores = gestor_repartidores
        self._gestor_pedidos = gestor_pedidos
        print("[GeneradorReportes] Constructor: generador creado")

    def __del__(self):
        print("[GeneradorReportes] Destructor: generador eliminado")

    def listado_clientes_activos(self) -> list:
        return self._gestor_clientes.listar_activos()

    def listado_clientes_suspendidos(self) -> list:
        return self._gestor_clientes.listar_suspendidos()

    def listado_repartidores_sin_amonestaciones(self) -> list:
        return self._gestor_repartidores.listar_sin_amonestaciones()

    def listado_restaurantes(self) -> list:
        return self._gestor_restaurantes.listar()

    def restaurante_mayor_pedidos(self):
        pedidos = self._gestor_pedidos.listar()
        if not pedidos:
            return None
        conteo = Counter(p.restaurante.cedula_juridica for p in pedidos)
        cedula_top = conteo.most_common(1)[0][0]
        return self._gestor_restaurantes.buscar_por_cedula(cedula_top)

    def restaurante_menor_pedidos(self):
        restaurantes = self._gestor_restaurantes.listar()
        if not restaurantes:
            return None
        pedidos = self._gestor_pedidos.listar()
        conteo = Counter(p.restaurante.cedula_juridica for p in pedidos)
        return min(restaurantes, key=lambda r: conteo.get(r.cedula_juridica, 0))

    def monto_total_por_restaurante(self) -> dict:
        totales = {}
        for p in self._gestor_pedidos.listar():
            subtotal = sum(combo.precio for combo in p.combos)
            totales[p.restaurante.nombre] = totales.get(p.restaurante.nombre, 0) + subtotal
        return totales

    def monto_total_general(self) -> float:
        return sum(self.monto_total_por_restaurante().values())

    def quejas_por_repartidor(self) -> dict:
        return {r.nombre: r.listar_quejas() for r in self._gestor_repartidores.listar()}

    def pedidos_por_cliente(self) -> dict:
        resultado = {}
        for p in self._gestor_pedidos.listar():
            resultado.setdefault(p.cliente.nombre, []).append(p)
        return resultado

    def cliente_mayor_pedidos(self):
        pedidos_por_cliente = self.pedidos_por_cliente()
        if not pedidos_por_cliente:
            return None
        nombre_top = max(pedidos_por_cliente, key=lambda n: len(pedidos_por_cliente[n]))
        return nombre_top, len(pedidos_por_cliente[nombre_top])

    def hora_pico(self):
        pedidos = self._gestor_pedidos.listar()
        if not pedidos:
            return None
        horas = Counter(p.hora_inicio.hour for p in pedidos)
        return horas.most_common(1)[0]