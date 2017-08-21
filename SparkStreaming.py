## Spark Streaming ###

import sys
## Develop Spark streaming context ##
# import os
# os.environ["SPARK_HOME"] = '/usr/lib/spark'
from pyspark import SparkConf, SparkContext
from pyspark.streaming import StreamingContext
## creating spark stream for word count
if __name__ == "__main__":
    conf = SparkConf().setMaster("local[2]").setAppName("SparkStreamingcount").set("spark.executor.memory","1g")
    sc = SparkContext(conf = conf)
    strc = StreamingContext(sc,1)

    strc.checkpoint("hdfs://quickstart.cloudera:8020/user/cloudera/sparkstream")

    lines = strc.socketTextStream(sys.argv[1],int(sys.argv[2]))
    count = lines.flatMap(lambda x: x.split(' ')).map(lambda x: (x,1)).reduceByKey(lambda x,y : x+y)

    count.pprint()
    strc.start()
    strc.awaitTermination()





