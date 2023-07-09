from clickhouse_driver import Client
import pandas as pd

def get_logs_from_clickhouse(filters):

    client = Client(host='localhost', port=9000, user='default', password='213790')

    conditions = []
    for key, value in filters.items():
        condition = f"{key} = '{value}'"
        conditions.append(condition)
    where_clause = " AND ".join(conditions)

    query = f"SELECT * FROM a_table WHERE {where_clause}"
    result = client.execute(query)

    df = pd.DataFrame(result, columns=[col[0] for col in client.execute('DESCRIBE a_table')])

    return df.values.tolist()


filters = {
    'source': 'web',
    'level': 'error'
}

logs = get_logs_from_clickhouse(filters)
for log in logs:
    print(log)
