# Databricks notebook source
dbutils.fs.mount(
  source = "wasbs://bronze@storage.blob.core.windows.net",
  mount_point = "/mnt/bronze",
  extra_configs = {"fs.azure.account.key.stroage.blob.core.windows.net":"key"})

# COMMAND ----------

df1 = spark.read.parquet("/mnt/bronze/customer.parquet", header=True, inferSchema=True)
display(df1.limit(20))

# COMMAND ----------

df2 = spark.read.parquet("/mnt/bronze/sales.parquet", header=True, inferSchema=True)
display(df2)

# COMMAND ----------

from pyspark.sql.types import IntegerType 

df1 = df1.withColumn('age', df1['age'].cast(IntegerType()))
df1.show(5)

# COMMAND ----------

from pyspark.sql.functions import col

df2.select(col('invoice_date').isNull()).count()

# COMMAND ----------

from pyspark.sql.types import IntegerType , TimestampType
from pyspark.sql.functions import col, to_timestamp, date_format, to_date, trim

df2 = df2.withColumn('quantity', df2['quantity'].cast(IntegerType()))
df2 = df2.withColumn('price', df2['price'].cast(IntegerType()))
df2 = df2.withColumn('invoice_date', to_date(trim(col('invoice_date')), 'dd-MM-yyyy'))
df2

# COMMAND ----------

df2.show(5)

# COMMAND ----------

dbutils.fs.mount(
  source = "wasbs://gold@storage.blob.core.windows.net",
  mount_point = "/mnt/gold",
  extra_configs = {"fs.azure.account.key.stroage1h.blob.core.windows.net":"key"})

# COMMAND ----------

name=[]
for i in dbutils.fs.ls('/mnt/bronze/'):
    names = name.append(i.name.split('.')[0])

df1.write.format('delta').mode('overwrite').save(f'/mnt/gold/{name[0]}')
df2.write.format('delta').mode('overwrite').save(f'/mnt/gold/{name[1]}')


