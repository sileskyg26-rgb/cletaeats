# Universidad Nacional
## Sección Regional Central-Occidente Alajuela
### EIF-400 Paradigmas de Programación — II Ciclo 2026

---

## Proyecto: CletaEats

**Integrantes:**

| Nombre | Cédula |
|---|---|
| Genesis Silesky Araya | 119470878 |
| Lausen Paniagua Arias | 208490835 |

**Fecha de entrega:** _(completar)_

---

## Descripción del trabajo

CletaEats es una aplicación de pedidos de comida a domicilio para la
provincia de Heredia, desarrollada en Python siguiendo el paradigma de
programación orientada a objetos y arquitectura Modelo-Vista-Controlador
(MVC), con interfaz web construida sobre Streamlit.

El sistema permite:

- **Registro e inicio de sesión de clientes** mediante su cédula, con
  estados de cuenta activo/suspendido.
- **Registro de restaurantes** (nombre, cédula jurídica, dirección, tipo
  de comida) y gestión de su menú de combos (numerados del 1 al 9, con
  precio calculado automáticamente desde ₡4.000 hasta ₡12.000).
- **Registro de repartidores**, con seguimiento de estado
  (disponible/ocupado), kilómetros recorridos, quejas recibidas y
  amonestaciones (con salida automática de la empresa al llegar a 4).
- **Creación de pedidos** de uno o varios combos de un mismo restaurante,
  con asignación automática del primer repartidor disponible.
- **Facturación** de cada pedido entregado, con sub-total, costo de
  transporte (según día hábil o feriado), IVA (13%) y monto total.
- **Persistencia en archivos de texto**, de modo que toda la información
  registrada (clientes, restaurantes, repartidores, combos, quejas y
  amonestaciones) se conserva entre ejecuciones del programa.
- **Módulo de reportes** para la empresa: listados de clientes por
  estado, repartidores sin amonestaciones, restaurantes con mayor/menor
  número de pedidos, montos vendidos por restaurante y totales, quejas
  por repartidor, pedidos por cliente, cliente con más pedidos y hora
  pico de pedidos.

La arquitectura del proyecto separa el dominio de negocio (`Modelo/`), la
lógica de coordinación y persistencia (`Controlador/`) y la interfaz de
usuario (`Vista/`), documentada en los diagramas de clases
(`diagrama_clases.md`) y de relaciones entre componentes
(`diagrama_relaciones.md`) incluidos en esta misma carpeta.
