
# coding: utf-8

# In[ ]:


from kafka import KafkaProducer
import logfile_preprocessing as lf
KAFKA_TOPIC = 'demo'
KAFKA_BROKERS = 'value_from_plain_text_endpoint' # see step 1
 
producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
 
# Must send bytes
logs=lf.pre.log_file_preprocessing('apache-access-log.txt')
stats=logs['server_status']
# Send the messages
for m in stats:
    producer.send(KAFKA_TOPIC, m)

