#!/bin/bash
# Directorio donde se encuentran los archivos de sumisión
submit_dir="submit_files"

# Iterar sobre los archivos de sumisión y enviarlos a Condor
for submit_file in "$submit_dir"/*.sub; do
    condor_submit "$submit_file"
    echo "Archivo de sumisión enviado: $submit_file"
done

