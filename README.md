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
- [Perl](https://www.perl.org/) instalado en su sistema.
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


## Ejecución de los experimentos 

En respuesta a la necesidad de realizar múltiples ejecuciones de diversos programas, se ha desarrollado un conjunto de scripts en el lenguaje de programación Perl. Este enfoque se ha adoptado para gestionar eficientemente la ejecución repetida de pruebas asociadas con algoritmos específicos de multiplicación de matrices.

Se han diseñado tres scripts distintos para abordar la diversidad de programas en cuestión. El primero, denominado **[lanzadorMM1c.pl](./scripts/execution/lanzadorMM1c.pl)**, se dedica exclusivamente a la ejecución de pruebas para el programa de multiplicación de matrices mediante el método tradicional de filas por columnas.

En paralelo, el segundo script, **[lanzadorMM1f.pl](./scripts/execution/lanzadorMM1f.pl)**, se especializa en ejecutar pruebas para el programa de multiplicación de matrices mediante el método de filas por filas. Por último, el tercer script, denominado **[lanzadorMM1.pl](./scripts/execution/lanzadorMM1.pl)**, engloba y coordina la ejecución de pruebas para ambos algoritmos.

Las pruebas emprendidas por estos scripts abarcan diversas combinaciones de matrices de tamaño, incluyendo dimensiones como *"100"*, *"200"*, *"400"*, *"600"*, *"800"*, *"1000"*, *"1500"*, *"2000"*, *"3000"*, *"4000"*, *"5000"*, *"6000"*, *"7000"* y *"8000"*. Además, se han considerado diferentes cantidades de procesadores para evaluar el rendimiento de los algoritmos, con opciones que van desde un solo procesador (*"1"*) hasta configuraciones más avanzadas, como *"2"*, *"4"*, *"8"*, *"10"*, *"14"*, *"16"* y *"20"*. 

En caso de que se requiera ajustar los parámetros, tanto el tamaño de las matrices a multiplicar como la cantidad de procesadores a emplear, se puede realizar dicha modificación de manera precisa y eficiente mediante la manipulación de las listas presentadas en la ilustración que sigue a continuación:


![Code that can be modified in Perl](/images/code_perl_modify.png)

En el fragmento de código proporcionado, se identifican tres listas, cada una desempeñando un papel específico en el proceso:

- Ejecutables:
  - Esta lista contiene los nombres de los programas ejecutables que servirán como base para la ejecución de las pruebas. Cada elemento de esta lista representa un programa específico destinado a realizar la multiplicación de matrices.
- Cores:
  - La lista denominada "Cores" almacena la cantidad de procesadores que se emplearán en cada una de las pruebas. Cada elemento de esta lista representa una configuración particular de núcleos de procesador utilizados durante la ejecución de las pruebas.
- VectorSize:
  - La lista "VectorSize" detalla el tamaño de las matrices cuadradas que serán sometidas a la operación de multiplicación. Cada valor en esta lista representa las dimensiones de las matrices, estableciendo la base para las variadas combinaciones de tamaños que serán objeto de prueba. 

Los scripts mencionados están ubicados en la ruta [./Matrix_Multiplication/scripts/execution/](./scripts/execution/). Para su ejecución, se requiere encontrarse en dicha carpeta, y además, es imperativo que exista la carpeta [./Matrix_Multiplication/Soluciones/](./Soluciones/).

Esta última carpeta actúa como el destino para almacenar las soluciones generadas por cada ejecución de los programas, representando así un componente esencial del proceso de experimentación.

En caso de requerir la creación de la carpeta [./Matrix_Multiplication/Soluciones/](./Soluciones/) se puede ejecutar el siguiente comando en la raíz del proyecto: 

```bash
mkdir Soluciones
```

## Resultados

Los resultados de los experimentos se almacenan en la carpeta results/. Puede utilizar herramientas de análisis de datos como Python y matplotlib para visualizar los resultados.

## Contribuciones

Si desea contribuir a este proyecto, no dude en abrir problemas, enviar solicitudes de extracción o sugerir mejoras.

## Licencia

Este proyecto se distribuye bajo la licencia MIT. Consulte el archivo LICENSE para obtener más detalles.

## Autor 

Ing. Alejandro Castro Martínez 
