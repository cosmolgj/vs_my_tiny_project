import requests
from bs4 import BeautifulSoup

#res = requests.get('https://news.v.daum.net/v/20170615203441266')
#res = requests.get('http://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20180117')

res = requests.get('https://search.naver.com/search.naver?query=%EA%B5%AD%EB%A6%BD%EA%B3%B5%EC%9B%90&where=news&ie=utf8&sm=nws_hty')

#print(res.content)

soup = BeautifulSoup(res.content, 'html.parser')

#print(soup.prettify())

titles = soup.find_all('a', {'class':'news_tit'})
for title in titles:
    print(title.get_text())

'''
contents = soup.find_all('a', attrs = {'class', 'news_info'})
for content in contents:
    print(content)
'''
'''
contents = soup.find_all('div', 'tit5')
for content in contents:
    print(content.get_text())
'''
'''
contents = soup.find_all('p', attrs= {'dmcf-ptype':'general'})


for content in contents:
    print(content.get_text())
'''

#print(soup.get_text())