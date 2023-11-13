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

def generar_grafico_y_guardar_imagen(archivos_csv, tamanos, carpeta_destino, nombre_imagen):
    plt.figure(figsize=(10, 6))

    for archivo in archivos_csv:
        # Lee el archivo CSV
        df = pd.read_csv(os.path.join(carpeta_tablas, archivo), delimiter=';')

        # Filtra los datos por tamaño de archivo
        df_filtrado = df[df['Tamano'].isin(tamanos)]

        # Gráfica de Tiempo Promedio vs. Procesadores para cada tamaño
        for tamano in tamanos:
            data_tamano = df_filtrado[df_filtrado['Tamano'] == tamano]
            data_tamano = data_tamano.sort_values('Procesadores')  # Ordenar por número de procesadores
            plt.scatter(data_tamano['Procesadores'], data_tamano['Tiempo Promedio'], label=f'{obtener_algoritmo_desde_nombre(archivo)} - Tamaño {tamano}')
            plt.plot(data_tamano['Procesadores'], data_tamano['Tiempo Promedio'], linestyle='-', marker='o', markersize=5)

    plt.xlabel('Número de Procesadores')
    plt.ylabel('Tiempo Promedio (µs)')

    # Obtener el rango de los datos para centrar el título y el subtítulo
    x_range = plt.xlim()
    y_range = plt.ylim()

    # Título y subtítulo más concisos
    plt.title('Comparación de Rendimiento vs. Procesadores', fontsize=16)

    plt.legend()

    # Ajustes adicionales para mejorar la apariencia
    plt.xscale('log')  # Utilizar escala logarítmica para el eje x
    plt.yscale('log')  # Utilizar escala logarítmica para el eje y
    plt.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)
    plt.tight_layout()

    # Crear la carpeta de destino si no existe
    os.makedirs(carpeta_destino, exist_ok=True)

    # Guardar la gráfica como una imagen con un nombre único en la carpeta de destino
    ruta_imagen = os.path.join(carpeta_destino, nombre_imagen)
    plt.savefig(ruta_imagen)

    # Limpiar la figura para la próxima iteración
    plt.clf()

# Carpeta que contiene los archivos CSV
carpeta_tablas = '../../tables/'

# Carpeta de destino para la imagen comparativa
carpeta_destino = 'imagenes_comparativas/'

# Lista de archivos CSV
archivos_csv = ['OpenMP_Columnas_Windows.csv', 'OpenMP_Filas_Windows.csv']

# Tamaños a considerar en la gráfica
tamanos_grafica = [400]

# Generar y guardar la gráfica comparativa
nombre_imagen = 'grafica_comparativa_algo_windows_400.png'
generar_grafico_y_guardar_imagen(archivos_csv, tamanos_grafica, carpeta_destino, nombre_imagen)
