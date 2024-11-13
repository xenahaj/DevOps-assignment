import requests
import sys
import time
import logging

# Configure logging with timestamp and level
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

def check_server(url, expected_status, retries=5, delay=2):
    #Check if server returns expected status code with retries
    for attempt in range(1, retries + 1):
        try:
            response = requests.get(url, timeout=5)
            logging.info(f"Attempt {attempt}: Checked {url} - Status Code {response.status_code}")
            if response.status_code == expected_status:
                logging.info(f"{url} returned expected status code {expected_status}.")
                return True
            else:
                logging.warning(f"{url} did not return expected status code {expected_status}. Received {response.status_code} instead.")
                return False
        except requests.exceptions.RequestException as e:
            logging.warning(f"Attempt {attempt}: Error connecting to {url}: {e}")
            if attempt < retries:
                time.sleep(delay)
    return False

def main():
    # Define servers to test with expected status codes
    servers = [
        {"url": "http://nginx:8080", "expected_status": 200},
        {"url": "http://nginx:8081", "expected_status": 503}
    ]
    all_passed = True
    for server in servers:
        if not check_server(server["url"], server["expected_status"]):
            all_passed = False
    if not all_passed:
        sys.exit(1)
    else:
        logging.info("All servers responded with expected status codes.")

if __name__ == "__main__":
    main()
