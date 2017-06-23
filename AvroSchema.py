import os
os.environ['SPARK_HOME']= '/usr/lib/spark'
import avro.schema
from avro.io import DatumWriter
from avro.datafile import DataFileReader, DataFileWriter
#from pyspark.sql import SQLContext , Row
from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext , Row

#####Important### Install avro codex using linux shell
# $SPARK_HOME/bin/pyspark --packages com.databricks:spark-avro_2.11:3.2.0
conf = (SparkConf().setMaster("local").setAppName("anoterApp").set("spark.executor.memory", "1g"))
sc=SparkContext(conf= conf)
sqlc = SQLContext(sc)

schema_string ='''{"namespace": "example.avro",
 "type": "record",
 "name": "KeyValue",
 "fields": [
     {"name": "key", "type": "string"},
     {"name": "value",  "type": ["int", "null"]}
 ]
}'''

schema = avro.schema.parse(schema_string)

wrt = DataFileWriter(open("kv.avro", "w"), DatumWriter(), schema)
wrt.append({"key": "foo", "value": -1})
wrt.append({"key": "bar", "value": 1})

df = sqlc.read.format("com.databricks.spark.avro").load("kv.avro")
print df.show()