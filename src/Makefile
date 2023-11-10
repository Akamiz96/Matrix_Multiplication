# Especificación de los compiladores
GCC = gcc
#MPI = mpicc

# Opciones de compilación para optimización y OpenMP
oT = -fopenmp -O3 

# Opciones de enlace y bibliotecas
CFLAGS = -lm 

# Archivos fuente
oL= Otime.c

# Directorio de destino para los binarios
BINDIR = ../BIN/

# Programas a borrar en el comando clean
PROGS = $(BINDIR)MM1c $(BINDIR)MM1f

# Regla para limpiar los binarios generados
all: MM1c MM1f

# Regla para limpiar los binarios generados
clean:
	$(RM) $(PROGS)

# Reglas individuales para construir cada programa
MM1c:
	$(GCC) $(oT) $(oL) $@.c -o $(BINDIR)$@ $(CFLAGS)

#MM1c_MPI:
#$(MPI) $(oT) $(oL) $@.c -o $(BINDIR)$@ $(CFLAGS)

MM1f:
	$(GCC) $(oT) $(oL) $@.c -o $(BINDIR)$@ $(CFLAGS)

#MM1f_MPI:
#$(MPI) $(oT) $(oL) $@.c -o $(BINDIR)$@ $(CFLAGS)
