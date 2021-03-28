# a glimpse at what's popular on Netflix Nigeria
# github @AminuAhmadh


import requests
from bs4 import BeautifulSoup as bs 


url = requests.get('https://www.netflix.com/ng/browse/genre/34399')
soup = bs(url.content, 'html.parser')
body = soup.find('main', {'class':'nm-collections-container with-blur'})
popularTitle = body.section.h2
print(popularTitle.string)
print()
some = body.find('div', {'class':'nm-content-horizontal-row'})
ul = some.find('ul', {'class':'nm-content-horizontal-row-item-container'})
li = ul.findAll('li', {'class': 'nm-content-horizontal-row-item'})
count = 0
for movie in li:
    titles = movie.find('span', {'class': 'nm-collections-title-name'})
    links = movie.find('a')['href']
    print(titles.get_text())
    print(f'Link to movie: {links}')
    print()
    count += 1
    if count == 10:
        break
print('Above are the list of the top 10 most popular movies on Netflix Nigeria Right Now')