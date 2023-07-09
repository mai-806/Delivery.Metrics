from clickhouse_driver import Client
import pandas as pd

def get_metrics_from_clickhouse(filters):

    client = Client(host='localhost', port=9000, user='default', password='213790')

    conditions = []
    for key, value in filters.items():
        condition = f"{key} = '{value}'"
        conditions.append(condition)
    where_clause = " AND ".join(conditions)

    query = f"SELECT * FROM b_table WHERE {where_clause}"
    result = client.execute(query)

    df = pd.DataFrame(result, columns=[col[0] for col in client.execute('DESCRIBE b_table')])

    return df.values.tolist()

filters = {
    'value': 12
}
metrics = get_metrics_from_clickhouse(filters)
for metric in metrics:
    print(metric)
