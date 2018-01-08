import requests 
from bs4 import BeautifulSoup


def find_titles(soup):

    titles = soup.find_all('h2', {'class': 'entry-title'})

    for title in titles:
        title_text = title.contents[0].get_text()
        title_url = title.contents[0]['href']

        print(title_text)
        print(title_url)
        print()


if __name__ == "__main__":

    url = 'http://eliascanetti.org/bg/category/novini/' # initial page

    while True:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        find_titles(soup)

        next_page = soup.select('a.pagination-next')

        if next_page:
            url = next_page[0]['href']
        else:
            break
