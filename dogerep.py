import requests
import time, os,sys

url = "https://api.wazirx.com/api/v2/tickers"


def get_curr():
    i=10
    res = requests.get(url, allow_redirects=True)
    r = res.json()
    data = r["dogeinr"]["last"]
    os.system(f'echo `date "+%T"` {data} >> list.txt')
    while True:
        i=i-1
        sys.stdout.write(f'\rCurrent rate in inr : ₹{data}  {i}s till refresh  ')
        time.sleep(1)
        sys.stdout.flush()
        if i==0:
            break
    
def repeat_interval():
    get_curr()
    repeat_interval()

