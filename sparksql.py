import os
os.environ['SPARK_HOME']= '/usr/lib/spark'
from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext , Row

conf = (SparkConf().setMaster("local").setAppName("MyApp").set("spark.executor.memory", "1g"))
sc=SparkContext(conf= conf)

sqlc = SQLContext(sc)

tweetpath = 'hdfs://quickstart.cloudera:8020/user/cloudera/spark_sql/cache-1000000.json'
twittertable = sqlc.read.json(tweetpath)
twittertable.registerTempTable("twittertable")
print sqlc.sql("select text, user.screen_name from twittertable where user.screen_name = 'realDonaldTrump' limit 10").collect()


