import os
os.environ['SPARK_HOME']= '/usr/lib/spark'
os.environ["PYSPARK_PYTHON"]= "/home/cloudera/anaconda2/bin/python"
os.environ["PYSPARK_DRIVER_PYTHON"]= "/home/cloudera/anaconda2/bin/python"
os.environ["SPARK_YARN_USER_ENV"]= "/home/cloudera/anaconda2/bin/python"


from pyspark.streaming.kafka import  KafkaUtils
from pyspark import SparkContext, SparkConf
from pyspark.streaming import StreamingContext

if __name__ == "__main__":
    conf = (SparkConf().setMaster("local[*]").setAppName("spar_stream").set("spark.executor.memory","4g").set("spark.driver.memory","5g"))
    sc = SparkContext(conf = conf)
    ssc = StreamingContext(sc, 10)
    kafkastream = KafkaUtils.createStream(ssc, 'localhost:2181', 'spark-streaming', {'rna': 1})
    kafkastream.pprint()
    # flatMap(lambda x: x.split('\n')).map(lambda x: x.split(','))
    ssc.start()
    ssc.awaitTermination()
