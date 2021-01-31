import requests
from decouple import config

url = config('URL')
res = requests.get(url)

print(res.status_code)
r = res.json()
data = r['dogeinr']
print(data)
