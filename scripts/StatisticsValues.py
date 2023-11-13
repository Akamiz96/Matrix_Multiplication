import os
import re
import pandas as pd

# Ruta de la carpeta principal que contiene todas las carpetas
carpeta_principal = '../consolidated'

# Ruta de la carpeta donde se guardarán los resultados
ruta_resultados = '../tables'

# Crear la carpeta si no existe
if not os.path.exists(ruta_resultados):
    os.makedirs(ruta_resultados)

# Lista de carpetas dentro de la carpeta principal
carpetas = [nombre for nombre in os.listdir(carpeta_principal) if os.path.isdir(os.path.join(carpeta_principal, nombre))]

# Iterar sobre cada carpeta
for carpeta in carpetas:

    carpeta_relativa = os.path.join(carpeta_principal, carpeta)

    # Listar todos los archivos en la carpeta
    archivos = [archivo for archivo in os.listdir(carpeta_relativa) if os.path.isfile(os.path.join(carpeta_relativa, archivo))]

    # Almacenar resultados en una lista para imprimir al final
    resultados_totales = []

    # Iterar sobre cada archivo y calcular el valor promedio y la desviación estándar
    for archivo in archivos:
        ruta_archivo = os.path.join(carpeta_relativa, archivo)
        df = pd.read_csv(ruta_archivo, delimiter=';') 

        # Extraer X e Y del nombre del archivo
        # X = Tamaño de las matrices a multiplicar 
        # Y = Procesadores 
        match = re.match(r'Consolidado_MM1[cf]-condor?-Size(\d+)-core(\d+)', archivo) or \
                re.match(r'Consolidado_MM1[cf]-Size(\d+)-core(\d+)', archivo)
        if match:
            x = int(match.group(1))
            y = int(match.group(2))
        else:
            print(f"No se pudo extraer el tamaño de las matrices y la cantidad de procesadores de {archivo}")
            continue

        
        # Calcular el valor promedio y la desviación estándar
        valor_promedio = round(df['Tiempo'].mean(), 2)
        desviacion_estandar = round(df['Tiempo'].std(), 2)

        # Almacenar resultados en la lista
        resultados_totales.append({
            'Tamano': x,
            'Procesadores': y,
            'Tiempo Promedio': valor_promedio,
            'Desviación Estándar': desviacion_estandar
        })

    # Crear el camino del archivo de salida
    ruta_salida = os.path.join(ruta_resultados, f'{carpeta}.csv')  # Nombre de archivo basado en el nombre de la carpeta

    # Crear el DataFrame con los resultados totales
    df_resultados = pd.DataFrame(resultados_totales)

    # Calcular el speedup para cada tamaño
    tamanos_unicos = df_resultados['Tamano'].unique()

    for tamano in tamanos_unicos:
        # Filtrar el DataFrame para un tamaño específico
        df_tamano = df_resultados[df_resultados['Tamano'] == tamano]

        # Encontrar la fila con 1 procesador (ejecución en serie)
        serie_row = df_tamano[df_tamano['Procesadores'] == 1]

        # Calcular el speedup para cada fila del DataFrame
        for index, row in df_tamano.iterrows():
            speedup = serie_row['Tiempo Promedio'].values[0] / row['Tiempo Promedio']
            df_resultados.at[index, 'Speedup'] = round(speedup,2)

    # Ordenar el DataFrame por tamaño y procesadores
    df_resultados = df_resultados.sort_values(by=['Tamano', 'Procesadores'])

    # Agregar la columna 'Speedup' al DataFrame original y guardar en el archivo CSV
    df_resultados.to_csv(ruta_salida, sep=';', index=False, columns=['Tamano', 'Procesadores', 'Tiempo Promedio', 'Desviación Estándar', 'Speedup'])

    print(f"Los resultados se han guardado en {ruta_salida}")
    print(df_resultados)
