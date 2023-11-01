![Matrix Multiplication Image](/images/matrix_multiplication.jpg)

# Multiplicación de Matrices con OpenMP y MPI

Este repositorio contiene un proyecto para realizar experimentos de multiplicación de matrices utilizando el algoritmo tradicional de filas por columnas con implementaciones en paralelo utilizando OpenMP y MPI. 

El objetivo es medir y comparar el tiempo de ejecución para matrices cuadradas de diferentes tamaños.

## Estructura del Proyecto

- `src/`: Contiene el código fuente de las implementaciones en C/C++.
- `scripts/`: Scripts de compilación y ejecución de los experimentos.
- `results/`: Almacena los resultados de los experimentos.
- `docs/`: Documentación adicional, si es necesario.

## Requisitos

- [OpenMP](https://www.openmp.org/) instalado en su sistema.
- [MPI (Message Passing Interface)](https://www.open-mpi.org/) instalado en su sistema.

## Compilación

Puede compilar los programas de la siguiente manera:

```bash
cd scripts/
```

## Ejecución 

Para ejecutar los experimentos, utilice los scripts proporcionados en la carpeta scripts:

```bash
cd scripts/
./run_experiment.sh
```

Asegúrese de ajustar los parámetros de los experimentos según sus necesidades.

## Resultados

Los resultados de los experimentos se almacenan en la carpeta results/. Puede utilizar herramientas de análisis de datos como Python y matplotlib para visualizar los resultados.

## Contribuciones

Si desea contribuir a este proyecto, no dude en abrir problemas, enviar solicitudes de extracción o sugerir mejoras.

## Licencia

Este proyecto se distribuye bajo la licencia MIT. Consulte el archivo LICENSE para obtener más detalles.

## Autor 

Ing. Alejandro Castro Martínez 
