import os
import re
import pandas as pd
import matplotlib.pyplot as plt

def obtener_texto_desde_nombre(nombre_archivo):
    # Utiliza expresiones regulares para extraer el texto después de "OpenMP_"
    match = re.search(r'OpenMP_(.+)', nombre_archivo)
    if match:
        return match.group(1)
    else:
        return 'Desconocido'

def obtener_texto_subtitulo(nombre_archivo):
    # Utiliza expresiones regulares para extraer el texto después de "OpenMP_"
    match = re.search(r'OpenMP_(.+)_([^_]+)\.csv', nombre_archivo)
    if match:
        return match.group(2)
    else:
        return 'Desconocido'

def generar_grafico_y_guardar_imagen(archivo_csv, tamanos, carpeta_destino, nombre_imagen):
    # Lee el archivo CSV
    df = pd.read_csv(archivo_csv, delimiter=';')

    # Filtra los datos por tamaño de archivo
    df_filtrado = df[df['Tamano'].isin(tamanos)]

    # Gráfica de Tiempo Promedio vs. Procesadores para cada tamaño
    for tamano in tamanos:
        data_tamano = df_filtrado[df_filtrado['Tamano'] == tamano]
        data_tamano = data_tamano.sort_values('Procesadores')  # Ordenar por número de procesadores
        plt.scatter(data_tamano['Procesadores'], data_tamano['Tiempo Promedio'], label=f'Tamaño {tamano}')
        plt.plot(data_tamano['Procesadores'], data_tamano['Tiempo Promedio'], linestyle='-', marker='o', markersize=5)

    plt.xlabel('Número de Procesadores')
    plt.ylabel('Tiempo Promedio (µs)')

    # Obtener el rango de los datos para centrar el título y el subtítulo
    x_range = plt.xlim()
    y_range = plt.ylim()

    # Título y subtítulo más concisos
    plt.title('Rendimiento vs. Procesadores', y=1.05, fontsize=16)
    plt.suptitle(f'Ambiente de pruebas: {obtener_texto_subtitulo(archivo_csv)}', y=0.85, fontsize=12)

    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

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

# Carpeta de destino para las imágenes
carpeta_destino = 'imagenes_resultantes/'

# Lista de archivos en la carpeta
archivos_csv = [archivo for archivo in os.listdir(carpeta_tablas) if archivo.endswith('.csv')]

# Tamaños a considerar en la gráfica
tamanos_grafica = [100, 400, 1000, 2000, 3000, 4000, 6000, 8000]

# Generar y guardar gráficos para cada archivo
for archivo in archivos_csv:
    nombre_imagen = f'Rendimiento vs. Procesadores_{obtener_texto_desde_nombre(archivo[:-4])}.png'  # Generar un nombre único para cada imagen
    ruta_completa = os.path.join(carpeta_tablas, archivo)
    generar_grafico_y_guardar_imagen(ruta_completa, tamanos_grafica, carpeta_destino, nombre_imagen)
