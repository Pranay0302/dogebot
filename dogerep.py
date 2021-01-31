import requests
import time, os
from decouple import config

url = config("URL")


def get_curr():
    res = requests.get(url, allow_redirects=True)
    print(res.status_code)
    r = res.json()
    data = r["dogeinr"]["last"]
    os.system(f'echo `date "+%T"` {data} >> list')


def repeat_interval():
    get_curr()
    time.sleep(10)
    repeat_interval()


repeat_interval()