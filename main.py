from bs4 import BeautifulSoup
import requests

#Cabecera del navegador
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'}
#URL de acceso a los resultados de busqueda
url = 'https://scholar.google.com/scholar?hl=es&as_sdt=0%2C10&q=web+scraping&btnG='

#Respuesta obtenida
response = requests.get(url, headers=headers)

#creacion objeto BeaustifulSoup con los parametros requeridos para el webscraping
soup= BeautifulSoup(response.content,'lxml')

for item in soup.select('[data-lid]'):
    #print(item)
    #Titulo del articulo
    print(item.select('h3')[0].get_text())
    #vinculo del articulo
    print(item.select('a')[0]['href'])
    #Resumen
    print(item.select('.gs_rs')[0].get_text())
    print('-------------------')