# Diagrama de Relaciones — Arquitectura CletaEats

Diagrama de relaciones entre los componentes del sistema (arquitectura
MVC): qué capa depende de cuál, y qué clase concreta de cada capa se
apoya en cuál del nivel inferior.

```mermaid
flowchart TB
    subgraph Vista["Vista (Streamlit)"]
        App["App"]
        VLogin["VistaLogin"]
        VMenu["VistaMenuPrincipal"]
        VRest["VistaRestaurante"]
        VRep["VistaRepartidor"]
        VPed["VistaPedido"]
        VRepo["VistaReportes"]
    end

    subgraph Controlador["Controlador"]
        CPrincipal["ControladorPrincipal"]
        CCli["ControladorClientes"]
        CRest["ControladorRestaurantes"]
        CRep["ControladorRepartidores"]
        CPed["ControladorPedidos"]
        CRepo["ControladorReportes"]
    end

    subgraph Modelo["Modelo (dominio + persistencia)"]
        Gestores["GestorClientes / GestorRestaurantes /\nGestorRepartidores / GestorPedidos"]
        Entidades["Cliente / Restaurante / Repartidor /\nCombo / Pedido / Factura / Queja"]
        Reportes["GeneradorReportes"]
        Persistencia["ArchivoTexto (ManejadorArchivo)"]
    end

    Datos[("datos/*.txt")]

    App --> VLogin
    App --> VMenu
    VMenu --> VRest
    VMenu --> VRep
    VMenu --> VPed
    VMenu --> VRepo

    VLogin --> CCli
    VRest --> CRest
    VRep --> CRep
    VPed --> CPed
    VRepo --> CRepo

    App --> CPrincipal
    CPrincipal --> Gestores
    CPrincipal --> Persistencia
    CPrincipal --> Reportes

    CCli --> Gestores
    CRest --> Gestores
    CRep --> Gestores
    CPed --> Gestores
    CRepo --> Reportes

    CCli -.->|guardar_todo| CPrincipal
    CRest -.->|guardar_todo| CPrincipal
    CRep -.->|guardar_todo| CPrincipal
    CPed -.->|guardar_todo| CPrincipal

    Gestores --> Entidades
    Reportes --> Gestores
    Persistencia --> Datos
```

## Cómo leerlo

- **Vista → Controlador:** cada vista de Streamlit solo conoce el
  controlador específico que necesita (p. ej. `VistaPedido` solo habla con
  `ControladorPedidos` y `ControladorRestaurantes`), nunca accede al Modelo
  directamente.
- **Controlador → Modelo:** cada controlador delega toda la lógica de
  negocio (validaciones, reglas de asignación de repartidor, cálculo de
  factura) en los Gestores y entidades del Modelo — el Controlador solo
  coordina y traduce errores a mensajes para la Vista.
- **Persistencia:** `ControladorPrincipal` es el único punto que sabe de
  archivos. Los demás controladores le avisan (`guardar_todo()`) cada vez
  que una operación modifica clientes, restaurantes o repartidores, para
  que el cambio quede en `datos/*.txt` y sobreviva a un reinicio.
