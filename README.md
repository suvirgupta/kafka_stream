# kafka_stream
kafka-spark streaming

Project is to ingest the real time tweets to HDFS and Spark as RDDS.
RDDS are can be used for sentiment analysis on real time and to make twitter headt maps.

python library to extract tweets from the twitter handle is Tweepy.
Link: https://github.com/suvirgupta/kafka_stream/blob/master/kafka_spark_stream.py

Topics are extracted from the twitter feeds on producer port 9092

kafka server properties are set as given below
link: https://github.com/suvirgupta/kafka_stream/blob/master/info%20file

There are two ways a real time tweets can be feed to spark
Link: https://spark.apache.org/docs/1.6.1/streaming-kafka-integration.html

Approach 1: Receiver-based Approach link: https://github.com/suvirgupta/kafka_stream/blob/master/sparkstream.py
This approach uses a Receiver to receive the data. The Receiver is implemented using the Kafka high-level consumer API. 
As with all receivers, the data received from Kafka through a Receiver is stored in Spark executors, and then jobs launched
by Spark Streaming processes the data.

However, under default configuration, this approach can lose data under failures (see receiver reliability. 
To ensure zero-data loss, you have to additionally enable Write Ahead Logs in Spark Streaming (introduced in Spark 1.2). 
This synchronously saves all the received Kafka data into write ahead logs on a distributed file system (e.g HDFS), 
so that all the data can be recovered on failure.

second approach gives better connectivity on my cloudera 5.8 vm

Approach 2 : Approach 2: Direct Approach (No Receivers) Link: https://github.com/suvirgupta/kafka_stream/blob/master/sparkstream.py
This new receiver-less “direct” approach has been introduced in Spark 1.3 to ensure stronger end-to-end guarantees. 
Instead of using receivers to receive data, this approach periodically queries Kafka for the latest offsets in each 
topic+partition, and accordingly defines the offset ranges to process in each batch. When the jobs to process the data 
are launched, Kafka’s simple consumer API is used to read the defined ranges of offsets from Kafka 
(similar to read files from a file system). Note that this is an experimental feature introduced in Spark 1.3 for the 
Scala and Java API, in Spark 1.4 for the Python API.

