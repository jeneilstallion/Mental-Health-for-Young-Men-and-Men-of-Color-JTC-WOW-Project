from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.nami.org/Home').text

soup = BeautifulSoup(source, 'lxml')

# print(soup.prettify())

for resource in soup.find_all('div', class_='dropdown-menu dropdown-menu-right dropdown-menu-lg-left show'):
	state = resource.a.data-text
	print(state)
