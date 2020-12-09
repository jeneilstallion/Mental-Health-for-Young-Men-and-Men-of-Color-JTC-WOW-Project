from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.nami.org/About-Mental-Illness').text

soup = BeautifulSoup(source, 'lxml')

# print(soup.prettify())

# this line is looping into all class "links-region" tag
for topic in soup.find_all('div', class_='links-region'):
	info = topic.ul.find_all('li')
	# print(info)
	for link in info:
		if link.a == None:
			print('No href')
		else:
			title = link.a.get('href')
			print(title)
	

	

 
