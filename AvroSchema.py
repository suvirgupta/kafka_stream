

### commands to be excecuted in console

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
# crete spark context and sql context to run sql operation onthe spark in distributed format
conf = (SparkConf().setMaster("local").setAppName("anoterApp1").set("spark.executor.memory", "1g"))
sc=SparkContext(conf= conf)
sqlc = SQLContext(sc)
sqlc.setConf("spark.sql.avro.compression.codec","snappy")
# schema_string ='''{"namespace": "example.avro",
#  "type": "record",
#  "name": "KeyValue",
#  "fields": [
#      {name :'auctionid', 'type' : 'int'}
#      {name :'bid', 'type' : 'int'}
#      {name :'bidtime', 'type': 'string'}df = sqlc.read.format("com.databricks.spark.avro").load("/user/cloudera/ebay_sk")
#      {name: 'bidder', 'type' : 'string'}
#      {name :'bidderrate', 'type' : 'int'}
#      {name : 'openbid', 'type': 'int'}
#      {name : 'price', 'type' : 'int'}
#  ]
# }'''
#
#
#
# schema = avro.schema.parse(schema_string)
#
# wrt = DataFileWriter(open("kv.avro", "w"), DatumWriter(), schema)
# wrt.append({"key": "foo", "value": -1})
# wrt.append({"key": "bar", "value": 1})

## convert from avro to dataframe
df1 = sqlc.read.format("com.databricks.spark.avro").load("/user/cloudera/ebay/ebay")
## register table to implement sql operations
df1.registerTempTable("ebay")
sqlc.sql("select count(*) from ebay group by auctionid").show()

## show() shows the table in the formated form vs collect() shows collection of the rows
# function library in pyspark has to be imported in oreder to use aggregate function
## reading through api
import pyspark.sql.functions as func
df1.groupby(df1.auctionid).count().agg(func.max("count"),func.min("count"), func.avg("count")).show()


