from flask import Flask, request, jsonify
from ClickHouse_consumer_metrics1 import get_metrics_from_clickhouse

app = Flask(__name__)

@app.route('/v1/get-metrics', methods=['POST'])
def get_metrics_handler():
    data = request.get_json()
    metrics = get_metrics_from_clickhouse(data)
    response = jsonify(metrics)
    return response

if __name__ == '__main__':
    app.run()
