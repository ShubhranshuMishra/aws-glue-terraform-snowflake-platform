import sys

from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.context import SparkContext
from pyspark.sql import functions as F


sc = SparkContext()
glue_context = GlueContext(sc)
spark = glue_context.spark_session
job = Job(glue_context)
job.init("partner_sales_etl", {})

input_path = "s3://partner-sales-platform-input/raw/partner_sales.csv"
output_path = "s3://partner-sales-platform-input/curated/partner_sales/"

df = (
    spark.read.option("header", True)
    .csv(input_path)
    .withColumn("sale_amount", F.col("sale_amount").cast("double"))
    .withColumn("sale_date", F.to_date("sale_date"))
    .withColumn("ingestion_date", F.current_date())
)

curated_df = (
    df.groupBy("partner_id", "country", "sale_date")
    .agg(F.sum("sale_amount").alias("daily_sales_amount"))
    .withColumn(
        "sales_band",
        F.when(F.col("daily_sales_amount") >= 15000, F.lit("HIGH"))
        .when(F.col("daily_sales_amount") >= 8000, F.lit("MEDIUM"))
        .otherwise(F.lit("LOW")),
    )
    .withColumn("load_timestamp", F.current_timestamp())
)

curated_df.write.mode("overwrite").parquet(output_path)

job.commit()
