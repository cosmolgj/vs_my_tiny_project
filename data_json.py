import json
import urllib.request

'''
url = 'https://www.naver.com'
json_url = urllib.request.urlopen(url)
byte_data = json_url.read()
text_data = byte_data.decode('utf-8')

print(text_data)
'''

url = 'https://python.bakyeono.net/data/movies.json'
text_data = urllib.request.urlopen(url).read().decode('utf-8')
movies = json.loads(text_data)

print(len(movies))
print(movies[2])