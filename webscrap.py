import bs4
from urllib.request import urlopen

res = urlopen('https://automatetheboringstuff.com/chapter11/')

exampleSoup = bs4.BeautifulSoup(res.read())
elements = exampleSoup.select('h2.title3')

for ele in elements:
    print(ele)

print('ivo')