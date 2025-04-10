# archivo: analisis_datos.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configuramos estilo de gráficos
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

# Simulamos un DataFrame de ejemplo
np.random.seed(42)

data = {
    'edad': np.random.randint(18, 65, 100),
    'ingresos_mensuales': np.random.normal(3000, 750, 100),
    'horas_trabajadas': np.random.randint(30, 60, 100),
    'satisfecho': np.random.choice(['Sí', 'No'], 100)
}

df = pd.DataFrame(data)

# Mostramos las primeras filas
print("Primeras filas del DataFrame:")
display(df.head())

# Estadísticas descriptivas
print("\nEstadísticas descriptivas:")
display(df.describe())

# Conteo de valores categóricos
print("\nDistribución de satisfacción:")
display(df['satisfecho'].value_counts())

# Gráfica 1: Histograma de edades
plt.figure()
sns.histplot(df['edad'], bins=10, kde=True)
plt.title('Distribución de Edades')
plt.xlabel('Edad')
plt.ylabel('Frecuencia')
plt.show()

# Gráfica 2: Boxplot de ingresos por nivel de satisfacción
plt.figure()
sns.boxplot(x='satisfecho', y='ingresos_mensuales', data=df)
plt.title('Ingresos mensuales por satisfacción')
plt.show()

# Gráfica 3: Mapa de calor de correlaciones
plt.figure()
corr = df.drop(columns='satisfecho').corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlaciones entre variables numéricas')
plt.show()