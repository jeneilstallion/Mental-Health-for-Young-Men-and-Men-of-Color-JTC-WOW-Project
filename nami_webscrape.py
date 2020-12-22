# This line of code imports Beautiful Soup which allows for data to be pulled 
# from HTML files and allows for easy searching of the data using python code.
from bs4 import BeautifulSoup

# This line of code allows us to access the response data (content) from the 
# url link we are looking to search.
from requests

# This line of code allows us to export the parsed data from our searches
# in a spreadsheet.
import csv

# Below are keywords that we searched on the nami website. 
# For 'African American', the %20 signifies a space in the url line
keywords = ['Black','African%20American', 'Latino', 'Latinx','Latina',
			'Indigenous']

# The set() method below creates an empty set where unique search results
# are being placed once the line of code is run
unique_results = set()

# The lines of code below we are accessing a csv file where the unique results
# above will be housed once the for loop goes through all the search keywords
with open('nami_list.csv', newline='', mode='w') as csvfile:
	fieldnames = ['title', 'summary', 'link']
	nami_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	nami_writer.writeheader()

	# Each keyword brings up multiple result pages so the for loop below goes 
	# through every page of each keyword.
	for number in range(1,10):
		#The for loop below is requesting the nami search page and going 
		# through each of the keywords listed in the keywords list above. 		
		for keyword in keywords:
			# This line of code contains the url for the nami search page.
			# We changed the keywork and the page number using the for loops
			# above to go through all the results.
			url = f'https://www.nami.org/Search?searchtext={keyword}&searchmode=allwords&bygroup=&bytopic=&bytype=139-141-142-143-144-145-146-147-149-153&page={number}'
			# The line of code below requests the nami url in text format 
			# so that we can read and view the search contents in terminal 
			nami_info = requests.get(url).text
			# The line of code below takes the url request above and creates
			# a soup object to parse the data
			soup = BeautifulSoup(nami_info, 'lxml')
			
			# This is an empty list to place the title of each resource
			titles_list = []
			# This is an empty list to place the summary of each resource 
			summary_list = []
			# This is an empty list to palce the url of each resource
			url_list = []
			
			# The for loop below is finding all of the tags in the html code 
			# with the specific "class" for all the titles. 
			for resource_title in soup.find_all('div', class_='search-resultsTitle'):
				# This line defines titles with the specific anchor element
				# in the div tag where the title exists.
				title = resource_title.a.text
				# This line of code takes the title and adds it to the empty 
				# titles list above and uses the strip function to remove
				# all of the extra spacing.
				titles_list.append(title.strip())

			# The for loop below is finding all of the tags in the html code 
			# with the specific "class" for all the summaries.
			for resource_summary in soup.find_all('div', class_='search-resultsSummary'):
				# This line defines summary with the specific anchor element
				# in the div tag where the summary exists.
				summary = resource_summary.text
				# This line of code takes the summary and adds it to the empty 
				# summaries list above and uses the strip function to remove
				# all of the extra spacing.
				summary_list.append(summary.strip())

			# The for loop below is finding all of the tags in the html code 
			# with the specific "class" for all the url's.
			for resource_url in soup.find_all('div', class_='search-resultsRelURL'):
				# This line defines summary with the specific anchor element
				# in the div tag where the url exists.
				link = resource_url.a.get('href')
				# This line of code takes the url and adds it to the empty 
				# url's list above and uses the strip function to remove
				# all of the extra spacing.
				url_list.append(link.strip())

			# The line below loops through each index in the lists that were 
			# created. With each list being the same the same length.
			for l in range(len(titles_list)):
				# This line of code adds each individual title with the
				# corresponding summary and url into the unique results empty
				# set created above.		
				unique_results.add((titles_list[l], summary_list[l], url_list[l]))		

	#This for loop goes through each result in the unique results set
	for result in unique_results:
		# The line of code below adds each unique result to the CSV file we 
		# created to house the results of the webscraping	
		nami_writer.writerow({'title': result[0] , 'summary': result[1], 'link': result[2]})



	

 
