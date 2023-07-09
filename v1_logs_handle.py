from flask import Flask, request, jsonify
from ClickHouse_consumer_logs import get_logs_from_clickhouse

app = Flask(__name__)

@app.route('/v1/get-logs', methods=['POST'])
def get_logs_handler():
    data = request.get_json()
    logs = get_logs_from_clickhouse(data)
    response = jsonify(logs)
    return response

if __name__ == '__main__':
    app.run()
