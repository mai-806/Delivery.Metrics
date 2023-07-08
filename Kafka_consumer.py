from kafka import KafkaConsumer

def get_data_from_kafka(topic):

    consumer = KafkaConsumer(topic, bootstrap_servers='localhost:9092')

    for message in consumer:
        return message.value.decode('utf-8')

topic = 'quickstart-events1'
data = get_data_from_kafka(topic)
print(data)