from kafka import KafkaConsumer
from clickhouse_driver import Client
import time
import json


def get_data_from_kafka(topic):
    consumer = KafkaConsumer(topic, bootstrap_servers='localhost:9092')
    for message in messages:
            data = json.loads(message.value.decode('utf-8'))
            send_to_clickhouse(data)

def send_to_clickhouse(data):
    client = Client(host='localhost', port=9000, user='default', password='213790')
    client.execute('CREATE TABLE IF NOT EXISTS on_table (column1 Int32, column2 String) ENGINE = MergeTree() ORDER BY (column1)')
    formatted_data = [(data['column1'], data['column2']) for item in data]
    client.execute('INSERT INTO on_table (column1, column2) VALUES', formatted_data)

topic = 'quickstart-events1'

while True:
    get_data_from_kafka(topic)
    time.sleep(5)
