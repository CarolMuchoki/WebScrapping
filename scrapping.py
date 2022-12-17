import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')
print(r.url)

soup = BeautifulSoup(r.content, 'html.parser')

s = soup.find('div', id='main')
leftbar=s.find('ul', class_='leftBarList')
lines= leftbar.find_all('li')
for line in lines:
    print(line.text)