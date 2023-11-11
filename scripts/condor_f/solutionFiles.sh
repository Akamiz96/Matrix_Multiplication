#!/bin/bash
#Directorio donde se encuentran los archivos de salida
output_dir="output"

# Directorio donde se guardarán las soluciones
solutions_dir="Soluciones"

# Crear el directorio de soluciones si no existe
mkdir -p "$solutions_dir"

# Iterar sobre las combinaciones de parámetros
for vs in "100" "200" "400" "600" "800" "1000" "1500" "2000" "3000" "4000" "5000" "6000" "7000" "8000"; do
    for c in "1" "2" "4" "8" "10" "14" "16" "20"; do
        # Nombre base del archivo de solución
        solution_file="${solutions_dir}/solucion_${vs}_${c}.txt"
        
        # Combinar los resultados de las 30 ejecuciones en un solo archivo de solución
        cat "$output_dir/salida_${vs}_${c}"_* >> "$solution_file"
        
        echo "Solución creada: $solution_file"
    done
done

