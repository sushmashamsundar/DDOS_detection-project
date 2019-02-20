
# coding: utf-8

# In[ ]:


KAFKA_TOPIC = 'demo'
KAFKA_BROKERS = 'value_from_plain_text_endpoint' # see step 1

# python 2/3 compatibility
from __future__ import print_function  
import sys # used to exit
from kafka import KafkaConsumer
 
KAFKA_TOPIC = 'demo'
KAFKA_BROKERS = 'value_from_plain_text_endpoint' # see step 1
 
consumer = KafkaConsumer(topic, bootstrap_servers=['localhost:9092'])
 
try:
    for message in consumer:
        print(message.value)
except KeyboardInterrupt:
    sys.exit()

