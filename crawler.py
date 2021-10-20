from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.naver.com")
# html = urlopen("https://www.python.org/about")
# html = urlopen("https://book.naver.com/bestsell/bestseller_list.nhn")
#bsObject = BeautifulSoup(html, "html.parser")

# print(bsObject.head.find("meta", {"name":"description"}))

# print(bsObject.head.find("meta", {"name":"description"}).get('content'))

#print(bsObject)
'''
for link in bsObject.find_all('a'):
    print(link.text.strip(), link.get('href'))

'''

data = html.read()

with open("webpage.html", 'wb') as f:
    f.write(data)


#print(html.read())