# -*- coding: utf-8 -*-
"""VentaVideojuegos.ipynb

En este notebook se busca identificar qué región del mundo cuenta con el mercado más grande de videojuegos (cuánto dinero han gastado los consumidores en videojuegos), y qué tipo de videojuegos se debería desarrollar para que tenga el mayor impacto en dicha región.
"""

#Se importan las librerias que se van a utilizar
import pandas as pd
import matplotlib.pyplot as plt

#Se importa el csv y se crea un df
df = pd.read_csv('/content/vgsales.csv')
df.head()

#Se eliminan los registros que tengan valores NaN en la columna de Years y se convierte a integer
df = df.dropna(subset=['Year'])
df['Year'] = df['Year'].astype(int)

#Se crea una lista que contenga solo los últimos 10 años registrados en el df
años_recientes = sorted(df['Year'].unique(), reverse=True)[:10]
años_recientes

#Se crea nuevo df con los ultimos 10 años
df_recientes = df[df['Year'].isin(años_recientes)]
df_recientes.sum()

#Se identifica la región que haya reportado la mayor cantidad de ventas
sum_reg = df_recientes[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']].sum()
sum_reg

#Se crea un df que contenga los 10 juegos más vendidos en NA en los últimos 10 años
bestSel_NA = df_recientes.sort_values('NA_Sales', ascending=False).head(10)

"""Se ha identificado que Norte América es el territorio en donde hay mayor gasto de capital por parte de los consumidores."""

#Gráfica de barras de los juegos más vendidos
bestSel_NA.plot(kind='barh', x='Name', y='NA_Sales', color='green', figsize=(10, 6))
plt.title('Juegos más vendidos en Norte América')
plt.xlabel('Ventas')
plt.ylabel('Juegos')
plt.show()

#Se agrupan por género y plataforma las ventas en NA
na_gen = df_recientes.groupby('Genre')['NA_Sales'].sum().sort_values(ascending=False)
na_plat = df_recientes.groupby('Platform')['NA_Sales'].sum().sort_values(ascending=False)

#Gráfica de barras de la venta por genero
na_gen.plot(kind='bar', figsize=(10, 6))
plt.title('Ventas por género en Norte América')
plt.xlabel('Género')
plt.ylabel('Ventas')
plt.tight_layout()
plt.show()

#Gráfica de barras de la venta por plataforma
na_plat.plot(kind='bar', color = 'green', figsize=(10, 6))
plt.title('Ventas por plataforma en Norte América')
plt.xlabel('Plataforma')
plt.ylabel('Ventas')
plt.tight_layout()
plt.show()

"""De la lista de juegos más vendidos, la mitad son del **género shooter y acción**, esto lo podemos corroborar la gráfica de ventas por género, con esta información ya nos podemos enfocar en qué tipo de videojuego deberíamos enfocarnos en hacer.
Con las ventas por plataforma, podemos notar que la consola Xbox 360 cuenta con el primer lugar, seguido del Ps3 y Wii. Estas 3 consolas fueron revolucionarias por sus tecnologías en jugabilidad cooperativa (local y en línea), por lo que ahora sabemos que **el videojuego de acción/shooter debe tener modos de juego que insiten a la cooperación entre jugadores.**
"""