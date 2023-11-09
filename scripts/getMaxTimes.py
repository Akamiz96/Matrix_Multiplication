import os
import sys

# Directorio raíz que contiene las carpetas con los archivos
root_directory = '..//results'
# Carpeta donde se guardarán los archivos de consolidación
output_directory = '..//consolidated'  
# Asegúrate de que la carpeta de consolidación exista
os.makedirs(output_directory, exist_ok=True)

# Define una función para procesar un archivo y escribir los resultados en un archivo de consolidación
def process_and_write_to_file(file_path, output_file):
    # Lee el archivo y determina el mayor tiempo para cada bloque
    with open(file_path, 'r') as file:
        current_sequence = None
        max_time = -1
        sequence_number = 0
        print(f"Experimento;Tiempo")
        for line in file:
            if line.strip():
                parts = line.strip().split(':')
                if len(parts) == 2:
                    sequence, time = int(parts[0]), int(parts[1])
                    if sequence == 0:
                        if current_sequence is not None:
                            output_file.write(f"{sequence_number};{max_time}\n")
                        current_sequence = sequence
                        sequence_number += 1
                        max_time = time
                    else:
                        max_time = max(max_time, time)
    
        # Imprime el mayor tiempo del último bloque si es necesario
        if current_sequence is not None:
            output_file.write(f"{sequence_number};{max_time}\n")


# Recorre las carpetas y subcarpetas en busca de archivos
for root, _, files in os.walk(root_directory):
    for file_name in files:
        file_path = os.path.join(root, file_name)

        # Genera la ruta para la carpeta de salida en la carpeta "consolidated" manteniendo la estructura
        relative_path = os.path.relpath(file_path, root_directory).split('/')[0]
        output_folder = os.path.join(output_directory, relative_path)
        # Asegúrate de que la carpeta de salida exista
        os.makedirs(output_folder, exist_ok=True)

        # Genera el nombre del archivo de consolidación
        consolidated_file_name = os.path.join(output_folder, f"Consolidado_{file_name}")

        # Abre un archivo para escribir los resultados de la consolidación
        with open(consolidated_file_name, 'w') as output_file:
            # Redirige la salida estándar al archivo de consolidación
            sys.stdout = output_file

            # Procesa el archivo y escribe los resultados en el archivo de consolidación
            process_and_write_to_file(file_path, output_file)

        # Restaura la salida estándar
        sys.stdout = sys.__stdout__
        
