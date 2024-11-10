import requests
import sys
import time
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

def check_server(url, retries=5, delay=2):
    for attempt in range(1, retries + 1):
        try:
            response = requests.get(url, timeout=5)
            logging.info(f"Attempt {attempt}: Checked {url} - Status Code {response.status_code}")
            if response.status_code == 200:
                logging.debug(f"Content: {response.text}")
            return response.status_code < 400
        except requests.exceptions.RequestException as e:
            logging.warning(f"Attempt {attempt}: Error connecting to {url}: {e}")
            if attempt < retries:
                time.sleep(delay)
    return False

def main():
    servers = ["http://nginx:8080", "http://nginx:8081"]
    all_passed = True
    for server in servers:
        if not check_server(server):
            all_passed = False
    if not all_passed:
        sys.exit(1)

if __name__ == "__main__":
    main()
