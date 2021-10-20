
from urllib.request import urlopen
from bs4 import BeautifulSoup

# html = urlopen("http://www.kyobobook.co.kr/bestSellerNew/bestseller.laf")
html = urlopen("http://www.kyobobook.co.kr/bestSellerNew/steadyseller.laf")
# html = urlopen("https://www.aladin.co.kr/usedstore/wbrowse.aspx?offcode=Gangnam&cid=351&start=offmain")
# html = urlopen("https://www.aladin.co.kr/search/wsearchresult.aspx?SearchTarget=UsedStore&KeyWord=%ED%95%9C%EB%B9%9B&KeyRecentPublish=0&OutStock=0&ViewType=Detail&SortOrder=5&CustReviewCount=0&CustReviewRank=0&KeyFullWord=%ED%95%9C%EB%B9%9B&KeyLastWord=%ED%95%9C%EB%B9%9B&CategorySearch=&chkKeyTitle=&chkKeyAuthor=&chkKeyPublisher=&ViewRowCount=25")
bsObject = BeautifulSoup(html, "html.parser")

#print(bsObject)

book_page_urls = []
for cover in bsObject.find_all('div', {'class':'detail'}):
    link = cover.select('a')[0].get('href')
    book_page_urls.append(link)

for index, book_page_url in enumerate(book_page_urls):
    html = urlopen(book_page_url)
    bsObject = BeautifulSoup(html, "html.parser")
    title = bsObject.find('meta', {'property':'og:title'}).get('content')
    author = bsObject.select('span.name a')[0].text
    image = bsObject.find('meta', {'property':'og:url'}).get('content')
    url = bsObject.find('meta', {'property':'og:url'}).get('content')
    Price = bsObject.find('meta', {'property':'og:price'}).get('content')

    print(index+1, title, author, image, url, Price)

