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

def generar_grafico_tiempo_promedio(archivos_csv, carpeta_destino, nombre_imagen, tam, proc):
    plt.figure(figsize=(12, 8))

    # Diccionario para almacenar los datos de cada algoritmo
    datos_por_algoritmo = {}

    for archivo in archivos_csv:
        # Lee el archivo CSV
        df = pd.read_csv(os.path.join(carpeta_tablas, archivo), delimiter=';')

        # Filtra los datos para evitar errores si la columna 'Tiempo Promedio' no existe
        if 'Tiempo Promedio' not in df.columns:
            print(f"Advertencia: El archivo {archivo} no tiene la columna 'Tiempo Promedio'. Se omitirá en la gráfica.")
            continue
        
        # Filtra los datos para el tamaño de tam y procesador proc
        df_filtrado = df[(df['Tamano'] == tam) & (df['Procesadores'] == proc)]

        # Si no hay datos después de aplicar los filtros, omitir el archivo
        if df_filtrado.empty:
            print(f"Advertencia: No hay datos para el archivo {archivo} con Tamaño 4000 y un solo procesador. Se omitirá en la gráfica.")
            continue

        # Obtén el tipo de algoritmo desde el nombre del archivo
        tipo_algoritmo = obtener_texto_desde_nombre(archivo)

        # Almacena los datos en el diccionario, agrupados por tipo de algoritmo
        if tipo_algoritmo not in datos_por_algoritmo:
            datos_por_algoritmo[tipo_algoritmo] = {'Algoritmos': [], 'Tiempo Promedio': []}

        # Añade los datos del archivo actual al diccionario
        datos_por_algoritmo[tipo_algoritmo]['Algoritmos'].append(obtener_texto_desde_nombre(archivo)+"-"+obtener_algoritmo_desde_nombre(archivo))
        datos_por_algoritmo[tipo_algoritmo]['Tiempo Promedio'].append(df_filtrado['Tiempo Promedio'].values[0])

    # Gráfica de barras del tiempo promedio para cada tipo de algoritmo
    for tipo_algoritmo, datos in datos_por_algoritmo.items():
        plt.bar(datos['Algoritmos'], datos['Tiempo Promedio'], label=f'{tipo_algoritmo}', alpha=0.7)

    plt.xlabel('Ambiente-Algoritmo')
    plt.ylabel('Tiempo Promedio (µs)')
    plt.title(f'Tiempo Promedio en Diferentes Ambientes de Prueba (Tamaño: {tam}, Procesadores: {proc})')
    plt.yscale('log')  # Utilizar escala logarítmica para el eje y
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

# Carpeta de destino para la imagen del tiempo promedio
carpeta_destino = 'imagenes_tiempo_promedio/'

# Lista de archivos CSV
archivos_csv = ['OpenMP_Columnas_Condor.csv', 'OpenMP_Columnas_Ubuntu.csv', 'OpenMP_Columnas_Windows.csv', 'OpenMP_Filas_Condor.csv', 'OpenMP_Filas_Ubuntu.csv', 'OpenMP_Filas_Windows.csv']

# Tamano que se desea filtrar 
tam = 1000

# Cantidad de procesadores que se desea filtrar
proc = 16

# Generar y guardar la gráfica del tiempo promedio
nombre_imagen = f'grafica_tiempo_promedio_{tam}_{proc}.png'
generar_grafico_tiempo_promedio(archivos_csv, carpeta_destino, nombre_imagen, tam, proc)
