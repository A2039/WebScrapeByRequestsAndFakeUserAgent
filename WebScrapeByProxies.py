import requests
import time
from fake_useragent import UserAgent

gfgurl = 'https://www.geeksforgeeks.org/getting-started-with-python-programming/?ref=lbp'

proxies_list = [
    {'ip': '00.000.00.134', 'port': '6540'},
    {'ip': '00.000.007.165', 'port': '6712'},
    #You can add more proxies, or only single proxies
]

proxy_user = 'YourUserID'
proxy_password = 'YourPassword'

ua = UserAgent()

def check_proxy(proxy):
    proxy_auth = f"{proxy_user}:{proxy_password}@{proxy['ip']}:{proxy['port']}"
    proxies = {
        'http': f'http://{proxy_auth}',
        'https': f'http://{proxy_auth}',
    }

    try:
        response = requests.get("https://httpbin.org/ip", proxies=proxies, timeout=10)
        if response.status_code == 200:
            print(f"Proxy {proxy['ip']}:{proxy['port']} is valid: {response.text}")
            return True
        else:
            print(f"Proxy {proxy['ip']}:{proxy['port']} failed with status code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Proxy {proxy['ip']}:{proxy['port']} failed: {e}")
    return False

for proxy in proxies_list:
    if check_proxy(proxy):
        proxy_auth = f"{proxy_user}:{proxy_password}@{proxy['ip']}:{proxy['port']}"
        proxies = {
            'http': f'http://{proxy_auth}',
            'https': f'http://{proxy_auth}',
        }

        headers = {
            'User-Agent': ua.random,
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Referer': 'https://www.google.com',
            'DNT': '1',
        }

        try:
            print(f"Testing proxy: {proxy['ip']}:{proxy['port']}")
            response = requests.get(gfgurl, headers=headers, proxies=proxies, timeout=10)
            if response.status_code == 200:
                print(f"Success with proxy {proxy['ip']}:{proxy['port']}")
                with open("gfgurlfile.html", "w", encoding='utf-8') as file:
                    file.write(response.text)
                break
            else:
                print(f"Error: Received status code {response.status_code} with proxy {proxy['ip']}:{proxy['port']}")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred with proxy {proxy['ip']}:{proxy['port']} -> {e}")
    time.sleep(3)  # Delay between retries
