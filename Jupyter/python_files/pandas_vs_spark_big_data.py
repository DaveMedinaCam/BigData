# pandas vs spark en big data
import pandas as pd
from pyspark.sql import SparkSession

# Spark Session
spark = SparkSession.builder.appName("PandasVSpark").getOrCreate()

# Simulamos un gran DataFrame
data = {'id': list(range(1, 100001)), 'valor': list(range(100001, 200001))}
pdf = pd.DataFrame(data)
sdf = spark.createDataFrame(pdf)

# Operación simple con pandas
print("Pandas media:", pdf['valor'].mean())

# Operación equivalente con Spark
sdf.selectExpr("avg(valor)").show()