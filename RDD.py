# from collections import namedtuple
# from datetime import datetime
#
# fields = ('date', 'airlines', 'flightnum', 'origin', 'dest', 'dep', 'dep_delay', 'arv', 'arv_delay', 'airtime', 'distance')
# Flights = namedtuple('Flights', fields,verbose=True )
#
# DATE_FMT = "%Y-%m-%d"
# TIME_FMT = "%H%M"
# def parse(row):
#     row[0] = datetime.strptime(row[0], DATE_FMT).date()
#     row[5] = datetime.strptime(row[5], TIME_FMT).time()
#     row[6] = float(row[6])
#     row[7] = datetime.strptime(row[7], TIME_FMT).time()
#     row[8] = float(row[8])
#     row[9] = float(row[9])
#     row[10] = float(row[10])
#     return Flights(*row[:11])
#


####### common spark properties to set  #################
#  setMaster, setAppname,
#  set(<properties name>, values)
#  properties name : spark.app.name, spark.driver.core,spark.driver.maxResultSize, spark.driver.memory, spark.executor.memory
#  spark.extraListeners, spark.local.dir,spark.logConf, spark.master
##########################################################################################################################################

import os
os.environ['SPARK_HOME']= '/usr/lib/spark'
from pyspark import SparkContext, SparkConf
conf = (SparkConf()
         .setMaster("local")
         .setAppName("My app")
         .set("spark.executor.memory", "1g"))
sc = SparkContext(conf = conf)

arr = sc.parallelize([1,2,3,4,5,6,7])

airport = sc.textFile('hdfs://quickstart.cloudera:8020/user/cloudera/spark_assignment/airports.csv')
print airport.take(10)








