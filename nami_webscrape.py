from bs4 import BeautifulSoup
import requests

# source = requests.get('https://www.nami.org/Search?searchtext=Latino&searchmode=allwords&bygroup=&bytopic=&bytype=139-141-142-143-144-145-146-147-149-153').text


# soup = BeautifulSoup(source, 'lxml')

# print(soup.prettify())

# this line is looping into all class "links-region" tag
# for topic in soup.find_all('div', class_='links-region'):
# 	info = topic.ul.find_all('li')
# 	# print(info)
# 	for link in info:
# 		if link.a == None:
# 			print('No href')
# 		else:
# 			title = link.a.get('href')
# 			print(title)


# url = ['https://www.nami.org/Search?searchtext=Latino&searchmode=allwords&bygroup=&bytopic=&bytype=139-141-142-143-144-145-146-147-149-153']


# soup = BeautifulSoup(url)

keywords = ['Black', 'Latino', 'Latinx']

# 'toolkit', 'depression','wellness'

for number in range(1,10):
	for keyword in keywords:
		url = f'https://www.nami.org/Search?searchtext={keyword}&searchmode=allwords&bygroup=&bytopic=&bytype=139-141-142-143-144-145-146-147-149-153&page={number}'
		nami_info = requests.get(url).text

	# print(nami_info.text)

		soup = BeautifulSoup(nami_info, 'lxml')
		titles_list = []
		summary_list = []
		url_list = []

		for resource_title in soup.find_all('div', class_='search-resultsTitle'):
			title = resource_title.a.text
			titles_list.append(title)

			# print(title)

		for resource_summary in soup.find_all('div', class_='search-resultsSummary'):
			summary = resource_summary
			summary_list.append(summary)

			# print(summary)

		for resource_url in soup.find_all('div', class_='search-resultsRelURL'):
			link = resource_url.a.get('href')
			url_list.append(link)

		# loop through each index in the lists (they all have the same length so you can just pick one)
		# and print every item at that index in each of the lists since they will match up
		for l in range(len(titles_list)):
			print(titles_list[l], summary_list[l], url_list[l])

			# print(link)



		# print(soup.prettify())




# div class="search-resultsTitle

# div class="search-resultsSummary

# div class="search-resultsRelURL

# span class="search-resultsURL


	

 
