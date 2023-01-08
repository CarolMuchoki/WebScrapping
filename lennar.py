from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as req

my_url = 'https://www.lennar.com/find-a-home?homeCoords=62.7057%2C-19.3727%2C-27.6226%2C-147.5173&commCoords=62.7057%2C-19.3727%2C-27.6226%2C-147.5173&tab=1'
uClient = req(my_url)
page_html = uClient.read()
uClient.close()
page_soup = bs(page_html, 'html.parser')
containers = page_soup.findAll('div', id='main')
print(len(containers))
