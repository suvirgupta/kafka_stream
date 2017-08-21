import os
os.environ['SPARK_HOME']= '/usr/lib/spark'



from pyspark.streaming.kafka import  KafkaUtils
from pyspark import SparkContext, SparkConf
from pyspark.streaming import StreamingContext

if __name__ == "__main__":
    conf = (SparkConf().setMaster("local[*]").setAppName("spar_stream").set("spark.executor.memory","4g").set("spark.driver.memory","5g"))
    sc = SparkContext(conf = conf)
    ssc = StreamingContext(sc, 10)
    kafkastream = KafkaUtils.createDirectStream(ssc, ['rna'],{"metadata.broker.list":'localhost:9093'})
    kafkastream.pprint()
    # print count.pprint()
    # kafkastream.saveAsTextFile("/user/cloudera/twitter"3
    # flatMap(lambda x: x.split('\n')).map(lambda x: x.split(','))
    ssc.start()
    ssc.awaitTermination()
