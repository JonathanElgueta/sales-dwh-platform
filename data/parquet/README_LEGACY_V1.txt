SALES DWH - LEGACY V1 LAYER

Autor: Jonathan Elgueta Elgueta
Versión actual proyecto: V2.0.0

Esta carpeta corresponde a la capa legacy de almacenamiento V1.

La arquitectura oficial V2 utiliza:

data/warehouse/

como storage principal.

La carpeta parquet se mantiene temporalmente para:

- rollback
- recovery
- validaciones históricas
- auditoría

NO utilizar esta carpeta para nuevos desarrollos.