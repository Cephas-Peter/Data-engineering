# Bronze Layer - Ingest JSON from ADLS
from pyspark.sql.functions import col, to_date, lower
df_bronze = spark.read.parquet("abfss://retailcontainer@retaildatalake.dfs.core.windows.net/Bronze/Cephas-Peter/Data-engineering/05071f489a0f083eb6d19cefdf5f204ae869e0da/retail_transactions_bronze.parquet")
df_bronze.show(5)
