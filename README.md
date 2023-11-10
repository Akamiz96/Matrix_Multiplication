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
mkdir BIN
cd src/
make
```

La ejecución de los comandos mencionados resulta en la generación de ejecutables correspondientes a diversos programas desarrollados en C. 

Dichos archivos ejecutables serán almacenados en el directorio `BIN/`, situado en la raíz del proyecto, siguiendo la siguiente nomenclatura: 

- **MM1c**: Archivo ejecutable correspondiente al algoritmo tradicional de multiplicación de matrices de filas por columnas. 
- **MM1f**: Archivo ejecutable correspondiente al algoritmo nuevo de multiplicación de matrices de filas por filas.


## Ejecución individual de cada archivo ejecutable

Los archivos ejecutables generados demandan la especificación de ciertos parámetros para garantizar su ejecución adecuada:

- **Tamaño de las matrices a multiplicar**: Debe ser un número entero comprendido entre 0 y 10,240, representando el tamaño de las matrices cuadradas sujetas a la operación de multiplicación.
- **Cantidad de procesadores a utilizar**: Se espera un valor numérico entero que indique la cantidad de procesadores a emplear en el proceso de multiplicación. Este número está limitado por la capacidad de procesadores disponible en la máquina donde se ejecuta el programa.
- **Número 0**: Este parámetro, aunque carece de significado en el contexto de la operación, es esencial para la correcta ejecución del programa. Debe ser siempre el número 0 y se incorpora en la programación como requisito indispensable.


Al llevar a cabo una instancia de ejecución para ambos programas previamente compilados, el procedimiento se configura de la siguiente manera:

```bash
./MM1c 1000 10 0
```

Este comando activaría el programa que implementa el algoritmo tradicional de multiplicación de matrices. La ejecución se efectuaría sobre dos matrices cuadradas, cada una compuesta por 1,000 filas y 1,000 columnas, haciendo uso de 10 procesadores. 

La ejecución de este programa produce un resultado de fácil interpretación. Cada línea de salida está compuesta por dos valores delimitados por el carácter ":". El primer número indica el procesador utilizado, mientras que el siguiente indica el tiempo de utilización de dicho procesador en microsegundos.

A continuación, se presenta una ilustración que exhibe la salida del comando ejecutado en una de las máquinas de prueba.

![Test Execution Image](/images/TestExecutionImage.jpg)


## Ejecución de experimento 

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
