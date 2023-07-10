from clickhouse_driver import Client
import datetime

client = Client(host='localhost', port=9000, user='default', password='213790')

client.execute('CREATE TABLE IF NOT EXISTS b_table (timestamp String, metric_name String, value Int32) ENGINE = MergeTree() ORDER BY (timestamp)')

data = [('2023-07-01 10:00:00', 'metric1', 12),
        ('2023-07-01 12:00:00', 'metric2', 14),
        ('2023-07-02 8:00:00', 'metric3', 84),
        ('2023-07-02 10:00:00', 'metric4', 12)]

client.execute('INSERT INTO b_table (timestamp, metric_name, value) VALUES', data)
