r las listas de valores para los parámetros
VectorSize=("100" "200" "400" "600" "800" "1000" "1500" "2000" "3000" "4000" "5000" "6000" "7000" "8000")
cores=("1" "2" "4" "8" "10" "14" "16" "20")

# Directorio donde se generarán los archivos de sumisión
output_dir="submit_files"

# Crear el directorio si no existe
mkdir -p "$output_dir"

# Número de ejecuciones por combinación
num_executions=30

# Iterar sobre las combinaciones de parámetros
for vs in "${VectorSize[@]}"; do
    for c in "${cores[@]}"; do
        # Nombre del archivo de sumisión
        submit_file="$output_dir/submit_${vs}_${c}.sub"

        # Crear el archivo de sumisión
        cat <<EOF > "$submit_file"
executable = ../../../BIN/MM1c
universe = vanilla
output = output/salida_${vs}_${c}_\$(Process).txt
error = error/error_${vs}_${c}_\$(Process).txt
log = log/log_${vs}_${c}_\$(Process).txt
should_transfer_files = YES
when_to_transfer_output = ON_EXIT
notification = never

arguments = $vs $c 0
queue $num_executions
EOF

        echo "Archivo de sumisión creado: $submit_file"
    done
done
