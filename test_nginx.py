import requests
import sys

def check_server(url):
    try:
        response = requests.get(url, timeout=5)
        print(f"Checked {url}: Status Code {response.status_code}")
        if response.status_code == 200:
            print(f"Content: {response.text}")
    except requests.exceptions.Timeout:
        print(f"Error: Timeout when connecting to {url}")
    except requests.exceptions.ConnectionError:
        print(f"Error: Connection error when connecting to {url}")
    except Exception as e:
        print(f"An unexpected error occurred when connecting to {url}: {e}")

if __name__ == "__main__":
    servers = ["http://nginx:8080", "http://nginx:8081"]
    for server in servers:
        check_server(server)
