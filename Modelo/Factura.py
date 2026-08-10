class Factura:
    IVA = 0.13
    def __init__(self, pedido, km_recorridos: float = 0.0, es_feriado: bool = False):
        self._pedido = pedido
        self._km_recorridos = km_recorridos
        self._es_feriado = es_feriado
        print(f"[Factura] Constructor: factura del pedido #{pedido.id} creada")

    def __del__(self):
        print("[Factura] Destructor: se eliminó la factura")

    @property
    def pedido(self):
        return self._pedido

    def calcular_subtotal(self) -> float:
        return sum(combo.precio for combo in self._pedido.combos)

    def calcular_transporte(self) -> float:
        repartidor = self._pedido.repartidor
        repartidor.distancia_pedido = self._km_recorridos
        return repartidor.calcular_costo_transporte(self._es_feriado)

    def calcular_iva(self) -> float:
        return self.calcular_subtotal() * IVA

    def calcular_total(self) -> float:
        return self.calcular_subtotal() + self.calcular_transporte() + self.calcular_iva()

    def __str__(self) -> str:
        pedido = self._pedido
        lineas = [f"===== FACTURA - Pedido #{pedido.id} ====="]
        lineas.append(f"Cliente: {pedido.cliente.nombre}")
        lineas.append(f"Restaurante: {pedido.restaurante.nombre}")
        for combo in pedido.combos:
            lineas.append(f"  {combo}")
        lineas.append(f"Sub-total: ₡{self.calcular_subtotal():,.2f}")
        lineas.append(f"Transporte: ₡{self.calcular_transporte():,.2f}")
        lineas.append(f"IVA (13%): ₡{self.calcular_iva():,.2f}")
        lineas.append(f"TOTAL: ₡{self.calcular_total():,.2f}")
        lineas.append(f"Repartidor: {pedido.repartidor.nombre}")
        lineas.append(f"Estado: {pedido.estado}")
        return "\n".join(lineas)