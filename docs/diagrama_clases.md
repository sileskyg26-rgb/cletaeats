# Diagrama de Clases — CletaEats

Diagrama UML del modelo de dominio (paquete `Modelo/`), con atributos,
métodos principales y relaciones entre clases (herencia, composición,
agregación y asociación con multiplicidad).

```mermaid
classDiagram
    direction TB

    class Usuario {
        <<abstract>>
        -cedula: str
        -nombre: str
        -direccion: str
        -telefono: str
        -correo: str
        +registrar()*
        +__str__() str
    }

    class Cliente {
        -id: int
        -numero_tarjeta: str
        -estado: str
        -pedidos: List~Pedido~
        +esta_activo() bool
        +agregar_pedido(pedido)
        +listar_pedidos() list
        +registrar()
    }

    class Repartidor {
        +COSTO_KM_HABIL: int = 1000
        +COSTO_KM_FERIADO: int = 1500
        +MAX_AMONESTACIONES: int = 4
        -id: int
        -numero_tarjeta: str
        -estado: str
        -distancia_pedido: float
        -km_recorridos_diarios: float
        -numero_amonestaciones: int
        +calcular_costo_transporte(es_feriado) float
        +esta_disponible() bool
        +agregar_amonestacion()
        +agregar_queja(descripcion, cedula_cliente)
        +debe_salir_de_la_empresa() bool
        +registrar()
    }

    class Queja {
        -descripcion: str
        -cedula_cliente: str
        -fecha: datetime
    }

    class ListaQuejas {
        -quejas: List~Queja~
        +agregar_queja(queja)
        +cantidad() int
        +listar() list
    }

    class Restaurante {
        -nombre: str
        -cedula_juridica: str
        -direccion: str
        -tipo_comida: str
    }

    class MenuRestaurante {
        -combos: List~Combo~
        +agregar_combo(combo)
        +obtener_combo(numero) Combo
        +listar_combos() list
    }

    class Combo {
        +PRECIO_BASE: int = 4000
        +INCREMENTO: int = 1000
        -numero: int
        -descripcion: str
        +precio: float
    }

    class Pedido {
        +ESTADOS_VALIDOS: tuple
        -id: int
        -combos: List~Combo~
        -hora_inicio: datetime
        -hora_entrega: datetime
        -estado: str
    }

    class Factura {
        +IVA: float = 0.13
        -km_recorridos: float
        -es_feriado: bool
        +calcular_subtotal() float
        +calcular_transporte() float
        +calcular_iva() float
        +calcular_total() float
    }

    class GestorBase {
        <<abstract>>
        -lista: list
        +agregar(elemento)*
        +listar() list*
        +buscar_por_cedula(cedula)*
        +cantidad() int
    }

    class GestorClientes {
        +listar_activos() list
        +listar_suspendidos() list
    }

    class GestorRestaurantes
    class GestorRepartidores {
        +listar_sin_amonestaciones() list
        +primer_disponible() Repartidor
    }
    class GestorPedidos {
        +crear_pedido(cliente, restaurante, gestorRep, combos) Pedido
        +buscar_por_id(id) Pedido
    }

    class GeneradorReportes {
        +restaurante_mayor_pedidos() Restaurante
        +restaurante_menor_pedidos() Restaurante
        +monto_total_por_restaurante() dict
        +monto_total_general() float
        +quejas_por_repartidor() dict
        +pedidos_por_cliente() dict
        +cliente_mayor_pedidos() tuple
        +hora_pico() tuple
    }

    class ManejadorArchivo {
        <<abstract>>
        +guardar(lista)*
        +cargar() list*
    }

    class ArchivoTexto {
        -ruta_archivo: str
        +guardar(lista)
        +cargar() list
    }

    Usuario <|-- Cliente
    Usuario <|-- Repartidor
    GestorBase <|-- GestorClientes
    GestorBase <|-- GestorRestaurantes
    GestorBase <|-- GestorRepartidores
    GestorBase <|-- GestorPedidos
    ManejadorArchivo <|-- ArchivoTexto

    Repartidor "1" *-- "1" ListaQuejas : contiene
    ListaQuejas "1" o-- "*" Queja : registra

    Restaurante "1" *-- "1" MenuRestaurante : tiene
    MenuRestaurante "1" o-- "*" Combo : ofrece

    Pedido "*" --> "1" Cliente : realizado por
    Pedido "*" --> "1" Restaurante : hecho a
    Pedido "*" --> "1" Repartidor : entregado por
    Pedido "1" o-- "1..*" Combo : incluye

    Factura "1" --> "1" Pedido : factura

    GeneradorReportes --> GestorClientes : consulta
    GeneradorReportes --> GestorRestaurantes : consulta
    GeneradorReportes --> GestorRepartidores : consulta
    GeneradorReportes --> GestorPedidos : consulta
```

## Notas de diseño

- **Herencia:** `Usuario` es una clase abstracta (`ABC`) que centraliza los
  campos comunes de `Cliente` y `Repartidor` (cédula, nombre, dirección,
  teléfono, correo) y obliga a implementar `registrar()`. `GestorBase` sigue
  el mismo patrón para los cuatro gestores, y `ManejadorArchivo` define el
  contrato de persistencia que implementa `ArchivoTexto`.
- **Composición:** `Restaurante` es dueño de su `MenuRestaurante`, y
  `Repartidor` es dueño de su `ListaQuejas` — si el contenedor desaparece,
  las partes no tienen sentido fuera de él.
- **Agregación:** `MenuRestaurante` agrega `Combo`s y `ListaQuejas` agrega
  `Queja`s — colecciones de objetos con identidad propia.
- **Asociación:** `Pedido` referencia a `Cliente`, `Restaurante` y
  `Repartidor` (múltiples pedidos por cada uno), y `Factura` se asocia 1 a 1
  con el `Pedido` que factura.
