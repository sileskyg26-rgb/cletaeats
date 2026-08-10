from MenuPrincipal import MenuPrincipal

if __name__ == "__main__":
    app = MenuPrincipal()

    cliente = app.registrar_cliente(
        "64366333", "Lausen Barrantes", "Grecia, Alajuela",
        "8888-8888", "lausen@email.com", "1234-5678-9012-3456")

    restaurante = app.registrar_restaurante(
        "Pollos Heredia", "3-101-123456", "Heredia centro", "rápida",
        combos_info=[(1, "Combo sencillo"), (3, "Combo familiar")])

    repartidor = app.registrar_repartidor(
        "2-2222-2222", "Josué Rojas", "Heredia",
        "8777-7777", "josue@email.com", "9999-8888-7777-6666")

    print("\n--- MENÚ ---")
    for linea in app.ver_menu_restaurante("3-101-123456"):
        print(" ", linea)

    print("\n--- CREAR PEDIDO (combos 1 y 3) ---")
    pedido = app.hacer_pedido("1-1111-1111", "3-101-123456", [1, 3])
    print(pedido)

    print("\n--- ENTREGAR PEDIDO (5 km, día hábil) ---")
    factura = app.entregar_pedido(pedido, km_recorridos=5, es_feriado=False)
    print(factura)

    print("\n--- REGISTRAR UNA QUEJA ---")
    app.registrar_queja("2-2222-2222", "Llegó tarde al pedido")
    print("Amonestaciones del repartidor:", repartidor.numero_amonestaciones)
    print("Quejas registradas:", repartidor.listar_quejas())

    print("\n--- REPORTES ---")
    print("Clientes activos:", [c.nombre for c in app.reportes.listado_clientes_activos()])
    print("Monto total por restaurante:", app.reportes.monto_total_por_restaurante())
    print("Restaurante con más pedidos:", app.reportes.restaurante_mayor_pedidos())
    print("Quejas por repartidor:", app.reportes.quejas_por_repartidor())
    print("Hora pico:", app.reportes.hora_pico())

    print("\nTODO OK - integración completa sin errores")