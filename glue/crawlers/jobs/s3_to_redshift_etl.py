from data_quality_checks import check_row_count, check_null_values
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import sys

def main():
    spark = SparkSession.builder \
        .appName("S3ToRedshiftETL") \
        .getOrCreate()

    # Read raw data from S3
    raw_df = spark.read \
        .option("header", "true") \
        .option("inferSchema", "true") \
        .csv("s3://raw-sales-data-bucket/sales/")

    # Basic transformations
    transformed_df = raw_df \
        .filter(col("amount").isNotNull()) \
        .withColumn("amount", col("amount").cast("double"))

    # Data quality check
    if transformed_df.count() == 0:
        raise Exception("ETL failed: No valid records after transformation")

    check_row_count(transformed_df)
    check_null_values(transformed_df, "amount")

    # Write to Redshift
    transformed_df.write \
        .format("jdbc") \
        .option("url", "jdbc:redshift://redshift-cluster-endpoint:5439/dev") \
        .option("dbtable", "analytics.sales") \
        .option("user", "REDSHIFT_USERNAME") \
        .option("password", "REDSHIFT_PASSWORD") \
        .option("driver", "com.amazon.redshift.jdbc.Driver") \
        .mode("append") \
        .save()

    spark.stop()

if __name__ == "__main__":
    main()
