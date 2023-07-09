import requests
from kafka import KafkaProducer
import json
import time

def get_logs_and_metrics(logs_url, metrics_url):
    logs_response = requests.get(logs_url)
    logs_data = logs_response.json()

    metrics_response = requests.get(metrics_url)
    metrics_data = metrics_response.json()

    return logs_data, metrics_data

def kafka_producer(topic, data):
    producer = KafkaProducer(
        bootstrap_servers='localhost:9092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    producer.send(topic, value=data)
    producer.flush()

def From_handles_to_Kafka(logs_url, metrics_url, topic):
    while True:
        logs_data, metrics_data = get_logs_and_metrics(logs_url, metrics_url)
        kafka_producer(topic, {'column1': logs_data, 'column2': metrics_data})
        time.sleep(5)

logs_url = "url_logs"
metrics_url = "url_metrics"
topic = "quickstart-events1"
From_handles_to_Kafka(logs_url, metrics_url, topic)