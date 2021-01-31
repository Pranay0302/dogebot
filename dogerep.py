import requests
import time, os

url = "https://api.wazirx.com/api/v2/tickers"


def get_curr():
    res = requests.get(url, allow_redirects=True)
    print(res.status_code)
    r = res.json()
    data = r["dogeinr"]["last"]
    os.system(f'echo `date "+%T"` {data} >> list.txt')


def repeat_interval():
    get_curr()
    time.sleep(10)
    repeat_interval()

