import pandas as pd

# Leer los datos desde el archivo
df = pd.read_csv('..//consolidated//OpenMP_Columnas//Consolidado_MM1c-Size100-core1', delimiter=';')

# Calcular el valor promedio y la desviación estándar
valor_promedio = df['Tiempo'].mean()
desviacion_estandar = df['Tiempo'].std()

print('Valor Promedio:', valor_promedio)
print('Desviación Estándar:', desviacion_estandar)