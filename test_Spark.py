from pyspark.sql import SparkSession
from pyspark.sql.functions import split, regexp_extract, regexp_replace, col
from pyspark.sql.types import StructField, StructType, StringType, IntegerType,ArrayType
import sys
import time

spark = SparkSession \
    .builder \
    .appName("Pyspark Tokenize") \
    .getOrCreate()

data = [('Category A', 100, "This is category A"),
        ('Category B', 120, "This is category B"),
        ('Category C', 150, "This is category C")]

# Create a schema for the dataframe
schema = StructType([
    StructField('Category', StringType(), True),
    StructField('Count', IntegerType(), True),
    StructField('Description', StringType(), True)
])

# Convert list to RDD
rdd = spark.sparkContext.parallelize(data)

# Create data frame
df = spark.createDataFrame(rdd,schema)
print(df.schema)
df.show()
