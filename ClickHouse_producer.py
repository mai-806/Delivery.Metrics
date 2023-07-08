from clickhouse_driver import Client
import datetime

def send_to_clickhouse(data):

	client = Client(host='localhost', port=9000, user='default', password='213790')


	client.execute('CREATE TABLE IF NOT EXISTS two_table (column1 Int32, column2 String) ENGINE = MergeTree() ORDER BY (column1)')

	formatted_data = [(item['column1'], item['column2']) for item in data]

	client.execute('INSERT INTO two_table (column1, column2) VALUES', formatted_data)

data = [{'column1': 1, 'column2': 'row1'},
	{'column1': 5, 'column2': 'row23'},
	{'column1': 34, 'column2': 'row23'}]

send_to_clickhouse(data)
