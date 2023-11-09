GCC = gcc
MPI = mpicc
oT = -fopenmp -O3 

CFLAGS = -lm 

oL= Otime.c

BINDIR = ../../BIN/
PROGS = $(BINDIR)MM1c 

all: MM1c MM1c_MPI MM1f MM1f_MPI

clean:
	$(RM) $(PROGS)

MM1c:
	$(GCC) $(oT) $(oL) $@.c -o $(BINDIR)$@ $(CFLAGS)

MM1c_MPI:
	$(MPI) $(oT) $(oL) $@.c -o $(BINDIR)$@ $(CFLAGS)

MM1f:
	$(GCC) $(oT) $(oL) $@.c -o $(BINDIR)$@ $(CFLAGS)

MM1f_MPI:
	$(MPI) $(oT) $(oL) $@.c -o $(BINDIR)$@ $(CFLAGS)
