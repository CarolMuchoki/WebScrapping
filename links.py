import requests
from bs4 import BeautifulSoup

r= requests.get('https://www.cloudflare.com/en-gb/?utm_source=challenge&utm_campaign=m')
soup= BeautifulSoup(r.content, 'html.parser')
for link in soup.find_all('a'):
    print(link.get('href'))
