from bs4 import BeautifulSoup
import requests

# r = requests.get('https://www.nami.org/Home')

# print(r)


# from selenium import webdriver

# PATH = "/Users/hernancarvente/Desktop/Chromedriver"
# driver = webdriver.Chrome(PATH)

# driver.get("https://www.nami.org/home")

# with open('/Users/hernancarvente/Desktop/web-projects/test-site/index.html') as html_file:
# 	soup = BeautifulSoup(html_file, 'lxml')

# print(soup.prettify())

# for article in soup.find_all('div', class_='article'):
# 	headline = article.h2.a.text
# 	print(headline)

# 	summary = article.p.text
# 	print(summary)

# 	print()

source = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source, 'lxml')

# for description in soup.find_all('div', class_='entry-content'):
# 	text_article = description.p.text
# 	print(text_article)

# 	print()

# this line of code is looping into all the 'article' tags in the website
for articles in soup.find_all('article'):
	# this line is looking for the titles in each article using the appropriate tags
	text_title = articles.h2.a.text
	# this line prints the title
	print(text_title)
	# this line is creating an if statement that is looking for the 'iframe' in each article 
	if articles.iframe == None:
		# print something to make it fun.
		print("No iframe here buddy")
	# creating an else statement for instances when no iframe is available
	else:
		#this line is pulling the source link from the 'src' attribute in the iframe tag 		
		video_link = articles.iframe.get('src')
		# printing the 'src' attribute link
		print(video_link)

	print()

 
# print(soup.prettify())


