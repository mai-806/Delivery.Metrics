from kafka import KafkaProducer

def send_to_kafka(data, topic):

    producer = KafkaProducer(bootstrap_servers='localhost:9092')

    data_bytes = data.encode('utf-8')

    producer.send(topic, value=data_bytes)

    producer.close()

data = "Пример текстовой информации"
topic = "quickstart-events1"

send_to_kafka(data, topic)