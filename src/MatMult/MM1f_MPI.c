/************************************************************************
* Autor: J. Corredor
* Fecha: Octubre 2023
* Computación de Alto Rendimiento
* Maestría en Inteligencia Artificial
* Tema: Programa de Multiplicación de Matrices usando MPI y OpenMP
* - Algoritmo Clásico filasXcolumnas
*************************************************************************/

#include <stdlib.h>
#include <stdio.h>
#include <mpi.h>
#include <omp.h>
#include "sample.h"

#ifndef MIN
#define MIN(x, y) ((x) < (y) ? (x) : (y))
#endif

#define DATA_SZ (1024 * 1024 * 64 * 3)

static double MEM_CHUNK[DATA_SZ];

void Matrix_Init_col(int SZ, double *a, double *b, double *c) {
    int j, k;
    for (j = 0; j < SZ; j++) {
        a[j + k * SZ] = 2.0 * (j + k);
        b[j + k * SZ] = 3.2 * (j - k);
        c[j + k * SZ] = 1.0;
    }
}

int main(int argc, char **argv) {
    int N;

    if (argc < 2) {
        printf("MM1c MatrixSize [Sample arguments ...]\n");
        return -1;
    }

    N = (int) atof(argv[1]);
    argc--;
    argv++;

    if (N > 1024 * 10) {
        printf("Invalid MatrixSize\n");
        return -1;
    }

    Sample_Init(argc, argv);

    MPI_Init(&argc, &argv);

    int rank, size;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    int local_N = N / size;
    int local_start = rank * local_N;
    int local_end = local_start + local_N;

    int SZ = N;
    double *a, *b, *c;
    a = MEM_CHUNK;
    b = a + SZ * SZ;
    c = b + SZ * SZ;

    if (rank == 0) {
        Matrix_Init_col(SZ, a, b, c);
    }

    double *local_a = a + local_start * SZ;
    double *local_b = b;
    double *local_c = c + local_start * SZ;

    Sample_Start(rank);

    #pragma omp parallel for
    for (int i = local_start; i < local_end; i++) {
        for (int j = 0; j < SZ; j++) {
            double *pA;
            pA = local_a + (i - local_start) * SZ;
            for (int k = 0; k < SZ; k++, pA++, local_b++) {
                local_c[(i - local_start) * SZ + j] += (*pA * *local_b);
            }
            local_b -= SZ; // Reset local_b for the next row of 'a'.
        }
    }

    Sample_Stop(rank);

    // Perform an Allreduce to gather results from all processes.
    MPI_Allreduce(local_c, c + local_start * SZ, local_N * SZ, MPI_DOUBLE, MPI_SUM, MPI_COMM_WORLD);

    if (rank == 0) {
        Sample_End();
    }

    MPI_Finalize();
}
