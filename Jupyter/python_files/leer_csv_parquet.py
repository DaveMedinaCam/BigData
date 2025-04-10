from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("LeerEscribir").getOrCreate()

# Leer CSV
df_csv = spark.read.csv("data/archivo_grande.csv", header=True, inferSchema=True)
df_csv.printSchema()

# Guardar como Parquet
df_csv.write.parquet("data/output_parquet/", mode="overwrite")

# Leer Parquet
df_parquet = spark.read.parquet("data/output_parquet/")
df_parquet.show(5)