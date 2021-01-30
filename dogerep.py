from bs4 import BeautifulSoup
import requests
from decouple import config

url = config('URL')
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')
# title = soup.find('title')
# print(title)
print(soup.prettify())
