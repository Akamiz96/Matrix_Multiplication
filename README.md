![Matrix Multiplication Image](/images/matrix_multiplication.jpg)

# Multiplicación de Matrices con OpenMP

Este repositorio contiene un proyecto para realizar experimentos de multiplicación de matrices utilizando el algoritmo tradicional de filas por columnas con implementaciones en paralelo utilizando OpenMP. 

El objetivo es medir y comparar el tiempo de ejecución para matrices cuadradas de diferentes tamaños.

## Estructura del Proyecto

- `src/`: Contiene el código fuente de las implementaciones en C.
- `scripts/`: Scripts de ejecución de los experimentos.
- `results/`: Almacena los resultados de los experimentos.
- `docs/`: Documentación adicional.

## Requisitos

- [build-essentials]() instalado en su sistema.
- [OpenMP](https://www.openmp.org/) instalado en su sistema.

## Compilación

Puede compilar los programas de la siguiente manera:

```bash
cd src/
make
```

La ejecución de los comandos mencionados resulta en la generación de ejecutables correspondientes a diversos programas desarrollados en C. 

Dichos archivos ejecutables serán almacenados en el directorio `BIN/`, situado en la raíz del proyecto.

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
