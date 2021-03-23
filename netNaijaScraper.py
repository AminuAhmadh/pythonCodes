# scrapping one of Nigeria's most popular website
# just type a topic (a movie, series, song, celebrity etc.) and you'll find some info about it.
# E.g. prison break, 2021 movies, justin bieber etc.
# if nothing is returned, then no search result


import requests
from bs4 import BeautifulSoup


website = 'https://www.thenetnaija.com/search?t='
search = input('Enter search term: ')
seperator = search.replace(' ', '+')
url = website + seperator
html_tag = requests.get(url)
soup = BeautifulSoup(html_tag.content, features='html.parser')
search_result = soup.find('div', attrs={'id': 'search-results'})
search_result_list = search_result.find('main', attrs={'class': 'search-results-list'})
search_info = search_result_list.find_all('article', attrs={'class': 'result'})
for sinfo in search_info:
    info = sinfo.find_all('div', attrs={'class': 'result-info'})
    for inf in info:
        titles = inf.find('h3', attrs={'class': 'result-title'})
        desc = inf.find('p', attrs={'class': 'result-desc'})
        link = inf.find('a')
        actual_link = link['href']
        print(titles.get_text())
        print(desc.get_text())
        print(f'More info: {actual_link}')
        print()

