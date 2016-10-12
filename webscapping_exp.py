import re,  os
from urllib.request import urlopen
from bs4 import BeautifulSoup
import mechanicalsoup

my_address = "https://realpython.com/practice/dionysus.html"

html_page = urlopen(my_address)
html_text = html_page.read().decode('utf-8')

name = "Name:"
fav = "Favorite Color:"

print (html_text[html_text.find(name)+len(name):html_text.find('</h2>')].strip())
print (html_text[html_text.find(fav)+len(fav):html_text.find('</center>')].strip())

for tag in ["Name:*" , "Favorite Color:*"]:
	search = re.search(tag+".*?[\n<]", html_text).group().strip()
	print (search)
	tag_sub = re.sub(tag,"", search).strip(" \n<")
	print (tag_sub)


base_address = "https://realpython.com/practice"
my_address = base_address+"/profiles.html"
html_page = urlopen(my_address)
html_text = html_page.read().decode('utf-8')
my_soup = BeautifulSoup(html_text, 'html.parser')


for hrf in my_soup.find_all("a"):
	print (hrf['href'])
	profile = hrf.get('href')
	my_address = base_address+"/"+profile
	print (my_address)
	html_page = urlopen(my_address)
	html_text = html_page.read()
	soup = BeautifulSoup(html_text, 'html.parser')
	print (soup.get_text())
	
my_browser = mechanicalsoup.Browser()
page = my_browser.get("https://realpython.com/practice/login.php")
html_text = page.soup

form = html_text.select('form')[0]
form.select("input")[0]["value"] = 'zeus'
form.select("input")[1]["value"] = 'Thunderude'

profile_page = my_browser.submit(form, page.url)
print (profile_page.soup.text)

if profile_page.soup.title.text == 'All Profiles':
	print ("redirected to ALL profiles", profile_page.soup)
else:
	print (profile_page.soup)