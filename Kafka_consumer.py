from kafka import KafkaConsumer 

def get_data_from_kafka(topic):
    
    consumer = KafkaConsumer(topic, bootstrap_servers='localhost:9092') 
    while (True): 
        messages = consumer.poll(timeout_ms=1000)
        for tp, messages in messages.items(): 
            for message in messages: 
                print(message.value.decode('utf-8')) 

topic = 'quickstart-events1' 
get_data_from_kafka(topic)
