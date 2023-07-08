import requests

def get_logs_and_metrics(logs_url, metrics_url):

    logs_response = requests.get(logs_url)
    logs_data = logs_response.json()

    metrics_response = requests.get(metrics_url)
    metrics_data = metrics_response.json()

    print("Logs data:", logs_data)
    print("Metrics data:", metrics_data)

get_logs_and_metrics("url_logs", "url_metrics")