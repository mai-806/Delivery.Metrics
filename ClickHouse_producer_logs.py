from clickhouse_driver import Client
import datetime

client = Client(host='localhost', port=9000, user='default', password='213790')

client.execute('CREATE TABLE IF NOT EXISTS a_table (timestamp String, level String, message String, source String) ENGINE = MergeTree() ORDER BY (timestamp)')

data = [('2023-07-01 10:00:00', 'error', 'Error message 1', 'web'),
        ('2023-07-01 12:00:00', 'info', 'Info message 1', 'api'),
        ('2023-07-02 8:00:00', 'error', 'Error message 2', 'web'),
        ('2023-07-02 10:00:00', 'warning', 'Warning message 1', 'web')]

client.execute('INSERT INTO a_table (timestamp, level, message, source) VALUES', data)
