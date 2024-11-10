import requests
import sys

def check_server(url):
    try:
        response = requests.get(url, timeout=5)
        print(f"Checked {url}: Status Code {response.status_code}")
        if response.status_code == 200:
            print(f"Content: {response.text}")
        return response.status_code < 400
    except requests.exceptions.Timeout:
        print(f"Error: Timeout when connecting to {url}")
        return False
    except requests.exceptions.ConnectionError:
        print(f"Error: Connection error when connecting to {url}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred when connecting to {url}: {e}")
        return False

if __name__ == "__main__":
    servers = ["http://nginx:8080", "http://nginx:8081"]
    all_passed = True
    for server in servers:
        if not check_server(server):
            all_passed = False
    if not all_passed:
        sys.exit(1)
