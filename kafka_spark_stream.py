import tweepy
import threading, logging, time
from kafka.client import SimpleClient
from kafka.consumer import SimpleConsumer
from kafka.producer import SimpleProducer
import string


######################################################################
# Authentication details. To  obtain these visit dev.twitter.com
######################################################################

consumer_key = 'BnmwonLefknDZ3jTaJzKJdQa3'  # eWkgf0izE2qtN8Ftk5yrVpaaJ
consumer_secret = 'ZgY5zWER3z4YoASXNdgDAUGcUKosBm6BFbKpVpCdyCVJJSThzV'  # BYYnkSEDx463mGzIxjSifxfXN6V1ggpfJaGBKlhRpUMuQ02lBE
access_token = '819272523246399490-2lWcTACsY4EEbBTI4f1AwYYGF9fAiOE'  # 1355650081-Mq5jok7mbcrIbTpqZPcMHgWjcymqSrG1kVaut40
access_token_secret = 'UgxScNWNmIRsujTbsbehAeBOOKg8vmUidsMLvCzWLEJdE'  # QovqxQnw0hSPrKwFIYLWct3Zv4MeGMash66IaOoFyXNWs

mytopic = 'rna'


######################################################################
# Create a handler for the streaming data that stays open...
######################################################################

class StdOutListener(tweepy.StreamListener):
    # Handler
    ''' Handles data received from the stream. '''

    ######################################################################
    # For each status event
    ######################################################################

    def on_status(self, status):

        # Prints the text of the tweet
        print '%d,%d,%d,%s,%s' % (status.user.followers_count, status.user.friends_count,status.user.statuses_count, status.user.id_str, status.user.screen_name)
        #print '%s' %(status.user.screen_name)
        # Schema changed to add the tweet text
        # print '%d,%d,%d,%s,%s' % (
        # status.user.followers_count, status.user.friends_count, status.user.statuses_count, status.text,
        # status.user.screen_name)
        message = status.text + ',' + status.user.screen_name
        msg = filter(lambda x: x in string.printable, message)
        try:
            producer.send_messages(mytopic, str(msg))
        except Exception, e:
            return True

        return True

    ######################################################################
    # Supress Failure to keep demo running... In a production situation
    # Handle with seperate handler
    ######################################################################

    def on_error(self, status_code):

        print('Got an error with status code: ' + str(status_code))
        return True  # To continue listening

    def on_timeout(self):

        print('Timeout...')
        return True  # To continue listening


######################################################################
# Main Loop Init
######################################################################


if __name__ == '__main__':
    listener = StdOutListener()

    # sign oath cert

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

    auth.set_access_token(access_token, access_token_secret)

    # uncomment to use api in stream for data send/retrieve algorythms
    # api = tweepy.API(auth)

    stream = tweepy.Stream(auth, listener)

    ######################################################################
    # Sample dilivers a stream of 1% (random selection) of all tweets
    ######################################################################
    client = SimpleClient("localhost:9093")
    producer = SimpleProducer(client)


    stream.sample()

    # kafkastream =  KafkaUtils.(ssc, 'localhost:2181', {'rna':1})
    # kafkastream.map(lambda x : x.split('\n')).pprint()
    #print kafkastream.map(lambda x : x.split('\n')).pprint()
    ######################################################################
    # Custom Filter rules pull all traffic for those filters in real time.
    # Bellow are some examples add or remove as needed...
    ######################################################################
    # A Good demo stream of reasonable amount
    # stream.filter(track=['actian', 'BigData', 'Hadoop', 'Predictive', 'Quantum', 'bigdata', 'Analytics', 'IoT'])
    # Hadoop Summit following
    # stream.filter(track=['actian', 'hadoop', 'hadoopsummit'])