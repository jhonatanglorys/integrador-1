from bs4 import BeautifulSoup
import requests

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'}
url = 'https://scholar.google.com/scholar?hl=es&as_sdt=0%2C10&q=web+scraping&btnG='

response = requests.get(url, headers=headers)

soup= BeautifulSoup(response.content,'lxml')

for item in soup.select('[data-lid]'):
    print(item)
    print('-------------------')