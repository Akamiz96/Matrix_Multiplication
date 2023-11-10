/************************************************************************
 * Autor: J. Corredor
 * Modificado por: Alejandro Castro Martinez
 * Fecha: Octubre 2023
 * Computación de Alto Rendimiento
 * Maestría en Ingenieria de Sistemas y Computación
 * Tema: Programa de Multiplicación de Matrices usando hilos OpenMP
 * - Algoritmo filasXfilas
 *************************************************************************/

/* -------------------------------------------------------------------------------------------
+                                   Incluir librerias                                        +
---------------------------------------------------------------------------------------------- */
#include <stdlib.h>
#include <stdio.h>
#include <omp.h>
#include "sample.h"

#ifndef MIN
// Definición de la macro MIN si no está previamente definida
#define MIN(x, y) ((x) < (y) ? (x) : (y))
#endif

// Tamaño predeterminado para el arreglo MEM_CHUNK
#define DATA_SZ (1024 * 1024 * 64 * 3)

// Declaración de un arreglo estático MEM_CHUNK con el tamaño especificado
static double MEM_CHUNK[DATA_SZ];

/* ==========================================================================================
+                             Funcion Inicializar Matriz                                    +
============================================================================================= */
void Matrix_Init_col(int SZ, double *a, double *b, double *c)
{
    int j, k;
    // Inicialización de las matrices a, b y c en formato de columna
    for (j = 0; j < SZ; j++)
    {
        // Asignación de valores según la fórmula dada
        a[j + k * SZ] = 2.0 * (j + k);
        b[j + k * SZ] = 3.2 * (j - k);
        c[j + k * SZ] = 0.0;
    }
}

/* ==========================================================================================
+                                   Funcion Princial                                        +
============================================================================================= */
int main(int argc, char **argv)
{
    // Declaración de la variable para el tamaño de la matriz
    int N;

    // Verificación de la presencia mínima de argumentos en la línea de comandos
    if (argc < 2)
    {
        // Mensaje de uso correcto y retorno de código de error
        printf("MM1c MatrixSize [Sample arguments ...]\n");
        return -1;
    }

    // Obtención del tamaño de la matriz desde los argumentos
    N = (int)atof(argv[1]);

    argc--; // Reducción del número de argumentos
    argv++; // Ajuste de la lista de argumentos

    // Verificación del tamaño de la matriz contra un límite predefinido
    if (N > 1024 * 10)
    {
        // Mensaje de matriz no válida y retorno de código de error
        printf("Unvalid MatrixSize\n");
        return -1;
    }

    // Inicializa la biblioteca de muestreo
    Sample_Init(argc, argv);

// Comienza una sección paralela
#pragma omp parallel
    {
        // Declaración de variables locales
        int NTHR, THR, SZ;
        int i, j, k;
        double *a, *b, *c;

        // Establece el tamaño SZ a partir de N
        SZ = N;
        // Instala el muestreador para el hilo
        THR = Sample_PAR_install();
        // Obtiene el número de hilos
        NTHR = omp_get_num_threads();

        // Asigna un puntero a la memoria compartida para la matriz A
        a = MEM_CHUNK;
        // Asigna un puntero a la memoria compartida para la matriz B
        b = a + SZ * SZ;
        // Asigna un puntero a la memoria compartida para la matriz de resultado C
        c = b + SZ * SZ;

// Solo el hilo maestro ejecuta este bloque
#pragma omp master
        // Inicializa las matrices a, b y c
        Matrix_Init_col(SZ, a, b, c);
        // Inicia el temporizador de muestreo para el hilo
        Sample_Start(THR);

// Inicia un bucle paralelo
#pragma omp for
        // Bucle para recorrer las filas de la matriz A
        for (i = 0; i < SZ; i++)
        {
            double *pA;
            // Establece un puntero a la fila i de la matriz A
            pA = a + (i * SZ);
            // Bucle para recorrer las filas de la matriz B
            for (j = 0; j < SZ; j++)
            {
                double *pB, S;
                // Establece un puntero a la columna j de la matriz B
                pB = b + (j * SZ);
                // Bucle para realizar la multiplicación y la suma
                for (k = 0; k < SZ; k++, pB++)
                {
                    // Realiza la multiplicación y acumula el resultado en la matriz C
                    c[i * SZ + k] += (*pA * *pB);
                }
                // Avanza al siguiente elemento en la fila de la matriz A
                pA++;
            }
        }
        // Detiene el temporizador de muestreo para el hilo actual
        Sample_Stop(THR);
    }
    // Finaliza el muestreo
    Sample_End();
}
