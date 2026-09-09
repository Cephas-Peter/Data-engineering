from pyspark.sql.functions import col, count, sum, to_date, lower

df_daily_revenue = (
    df_silver.groupBy("event_date")
    .agg(sum("amount").alias("daily_revenue"), count("*").alias("total_purchases"))
)

df_daily_revenue.write.mode("overwrite").parquet("abfss://retailcontainer@retaildatalake.dfs.core.windows.net/gold/")
df_daily_revenue.show(5)
