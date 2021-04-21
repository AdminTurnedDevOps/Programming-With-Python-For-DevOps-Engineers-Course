import requests
from bs4 import BeautifulSoup

page = requests.get('https://michaellevan.net')

soup = BeautifulSoup(page.content, 'html.parser')

page_title = soup.title.text
page_head = soup.head


first_h1 = soup.select('h1')[0].text
second_h1 = soup.select('h1')[1].text

print(first_h1)
print(second_h1)