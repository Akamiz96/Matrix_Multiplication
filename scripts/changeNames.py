import os

# Directorio donde se encuentran los archivos
directorio = '..//results//OpenMP_Filas_Condor'

# Lista los archivos en el directorio
archivos = os.listdir(directorio)

for archivo in archivos:
    # Comprueba que el archivo tiene el formato deseado
    if archivo.startswith('solucion_') and archivo.endswith('.txt'):
        # Divide el nombre del archivo en sus partes
        partes = archivo.split('_')
        
        # Extrae los valores X e Y
        X = partes[1]
        Y = partes[2].split('.')[0]  # Elimina la extensión .txt
        
        # Crea el nuevo nombre de archivo
        nuevo_nombre = f'MM1f-condor-Size{X}-core{Y}'
        
        # Renombra el archivo
        os.rename(os.path.join(directorio, archivo), os.path.join(directorio, nuevo_nombre))
