import os
import re
import pandas as pd
import matplotlib.pyplot as plt

def obtener_texto_desde_nombre(nombre_archivo):
    # Utiliza expresiones regulares para extraer el texto después de "OpenMP_"
    match = re.search(r'OpenMP_(.+)_([^_]+)\.csv', nombre_archivo)
    if match:
        return match.group(2)
    else:
        return 'Desconocido'

def obtener_algoritmo_desde_nombre(nombre_archivo):
    # Utiliza expresiones regulares para extraer el texto después de "OpenMP_"
    match = re.search(r'OpenMP_(.+)_([^_]+)\.csv', nombre_archivo)
    if match:
        return match.group(1)
    else:
        return 'Desconocido'

def generar_grafico_speedup_comparativo(archivos_csv, carpeta_destino, nombre_imagen, tam):
    plt.figure(figsize=(10, 6))

    for archivo in archivos_csv:
        # Lee el archivo CSV
        df = pd.read_csv(os.path.join(carpeta_tablas, archivo), delimiter=';')

        # Filtra los datos para evitar errores si la columna 'Speedup' no existe
        if 'Speedup' not in df.columns:
            print(f"Advertencia: El archivo {archivo} no tiene la columna 'Speedup'. Se omitirá en la gráfica.")
            continue

        # Filtra los datos para el tamaño de tam
        df_filtrado = df[(df['Tamano'] == tam) & (df['Procesadores'] <= 16)]

        # Si no hay datos después de aplicar los filtros, omitir el archivo
        if df_filtrado.empty:
            print(f"Advertencia: No hay datos para el archivo {archivo} con Tamaño {tam}. Se omitirá en la gráfica.")
            continue

        # Obtén el ambiente desde el nombre del archivo
        ambiente = obtener_texto_desde_nombre(archivo) + "-" + obtener_algoritmo_desde_nombre(archivo)

        # Gráfica de líneas para Speedup
        plt.plot(df_filtrado['Procesadores'], df_filtrado['Speedup'], label=f'{ambiente}',linestyle='-', marker='o', markersize=5)

    plt.xlabel('Cantidad de Procesadores')
    plt.ylabel('Speedup')
    plt.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)
    plt.title(f'Comparación de Speedup en Ambientes de Windows y Ubuntu (Tamaño: {tam})')
    plt.legend()

    # Crear la carpeta de destino si no existe
    os.makedirs(carpeta_destino, exist_ok=True)

    # Guardar la gráfica como una imagen con un nombre único en la carpeta de destino
    ruta_imagen = os.path.join(carpeta_destino, nombre_imagen)
    plt.savefig(ruta_imagen, bbox_inches='tight')

    # Limpiar la figura para la próxima iteración
    plt.clf()

# Carpeta que contiene los archivos CSV
carpeta_tablas = '../../tables/'

# Carpeta de destino para la imagen de comparación de Speedup
carpeta_destino = 'imagenes_comparacion_speedup_lineas/'

# Lista de archivos CSV
#archivos_csv = ['OpenMP_Columnas_Ubuntu.csv', 'OpenMP_Columnas_Windows.csv', 'OpenMP_Filas_Ubuntu.csv', 'OpenMP_Filas_Windows.csv']
archivos_csv = ['OpenMP_Columnas_Condor.csv', 'OpenMP_Filas_Condor.csv']
# Tamano que se desea filtrar
tam = 4000

# Generar y guardar la gráfica comparativa de Speedup en líneas
nombre_imagen = f'grafica_comparativa_speedup_lineas_Condor_{tam}.png'
generar_grafico_speedup_comparativo(archivos_csv, carpeta_destino, nombre_imagen, tam)
