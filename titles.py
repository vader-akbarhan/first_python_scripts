import requests 
from bs4 import BeautifulSoup

url = 'http://eliascanetti.org/bg/category/novini/'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, "lxml")
titles = soup.find_all('h2', {'class': 'entry-title'})

for list_of_tags in titles: 
    for inner_tag in list_of_tags.contents[0]:
        print(inner_tag, end="\n\n")