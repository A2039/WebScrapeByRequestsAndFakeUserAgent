import requests
import time

economictimes = 'https://economictimes.indiatimes.com/markets/ipo'

# sleep for mimic human behavior
time.sleep(2)
try:
    r = requests.get(economictimes, timeout=10)
    if r.status_code == 200:
        with open("economictimes.html", "w", encoding='utf-8') as file:
            file.write(r.text)
    else:
        print(f"Error: {r.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
