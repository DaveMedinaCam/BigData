from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg

spark = SparkSession.builder.appName("AnalisisBigData").getOrCreate()

df = spark.read.csv("data/ventas.csv", header=True, inferSchema=True)

# Total por categoría
df.groupBy("categoria").sum("monto").show()

# Promedio por país
df.groupBy("pais").agg(avg("monto").alias("promedio_venta")).show()

# Filtrar grandes ventas
df.filter(col("monto") > 10000).show()