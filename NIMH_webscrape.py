from bs4 import BeautifulSoup
import requests
import csv

url = 'https://www.nimh.nih.gov/health/find-help/index.shtml#part_150431'

response = requests.get(url)
# print(response.status_code)
#Print staus code (200) valid page
# print(response.headers)
#print headers of page
source = response.content
# print(source)

soup = BeautifulSoup(source, 'lxml')
#create soup object to parse
links = soup.find_all('a')
# print(links)
div_tag = soup.find_all('div')
# print(div_tag)
match = soup.find_all('p')
# print(match)

resouces = soup.find_all('$0', )


for divs in div_tag:
	for links in divs.find_all('a'[0]):
		match = soup.a.text
		# print(links)


soup = BeautifulSoup(response.text, 'html.parser')
nimh_domain = 'https://www.nimh.gov'

def get_link_info(title):
	data = []
	for link in soup.find('section', {"data-cms-title": title}).findAll('a'):
		url = ''
		if 'http://' in link['href']:
			url = link['href']
		elif 'https://' in link['href']:
			url = link['href']
		else: 
			url = f"{nimh_domain}{link['href']}"
		print(link.text)
		parent = link.find_parent('p')
		print(parent.text)
		for child in soup.p.children:
			print(child)
			for e in soup.findAll('br'):
				e.extract()
				for div in soup.findAll("div", id='tagline'): 
					div.decompose()
		link_info = {'Link': url , 'Desription':link.text , 'Number':link.text, 'Summary':link.text}
		data.append(link_info)
	return data

def get_healthcare_info(title):
	healthcare_data = []
	for link in soup.find('section', {"data-cms-title": title}).findAll('a'):
		url = ''
		if 'http://' in link['href']:
			url = link['href']
		elif 'https://' in link['href']:
			url = link['href']
		else: 
			url = f"{nimh_domain}{link['href']}"
		print(link.text)
		link_info = {'Link': url , 'Desription':link.text , 'Number':link.text, 'Summary':link.text}
		healthcare_data.append(link_info)
	return healthcare_data
		

# def get_link_description(summary):
# 	link_summ = []
# 	for summ in soup.find('section', {""})

# title_tag = soup.title
# print(title_tag)

# links = soup.findAll('strong')
# print(links)
# parent = soup.find_parent('p')
# print(parent)
# for link in soup.find('a', class_="box_section mobile-collapse").findAll('a'):
#       print(f"{nimh_domain}{link['href']}")

# for link in soup.find('section', {"data-cms-title": "Get Immediate Help in a Crisis"}).findAll('a'):
#       print(f"{nimh_domain}{link['href']}")
#       print(link.text)


# for link in soup.find('section', {"data-cms-title": "Find a Health Care Provider or Treatment"}).findAll('a'):
#       print(f"{nimh_domain}{link['href']}")

get_link_info('Get Immediate Help in a Crisis')
# get_healthcare_info('Get Immediate Help in a Crisis')




# print('')

# get_link_info('Get Immediate Help in a Crisis')

# Headers = ['Link', 'Desription', 'Number', 'Summary']

# dict_data = get_link_info('Get Immediate Help in a Crisis',)
# healthcare_data = get_healthcare_info('Find a Health Care Provider or Treatment')

# NIMH_data = dict_data + healthcare_data 

# csv_file = "NIMH_data_new.csv"
# try:
#     with open(csv_file, 'w') as csvfile:
#         writer = csv.DictWriter(csvfile, fieldnames=Headers)
#         writer.writeheader()
#         for data in NIMH_data:
#             writer.writerow(data)
#     print('csv complete')

# except IOError:
#     print("I/O error")

# print(urls)

# print(a_tag)

# soup.find('div', {'class': 'field-content'})

# for number in range(1,10):
# 	for keyword in keywords:
# 		url = f'https://www.nimh.nih.gov/health/find-help/index.shtml#part_150431'
# 		nami_info = requests.get(url).text

# for resource_title in soup.find_all('div', class_='titleblock__title'):
# 			title = resource_title.a.text
# 			titles_list.append(title)

			# print(title)

		# for resource_summary in soup.find_all('div', class_='search-resultsSummary'):
		# 	summary = resource_summary
		# 	summary_list.append(summary)

		# 	# print(summary)

		# for resource_url in soup.find_all('div', class_='search-resultsRelURL'):
		# 	link = resource_url.a.get('href')
		# 	url_list.append(link)




	