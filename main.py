from bs4 import BeautifulSoup
import requests

#Ingreso del parámetro de búsqueda
cadena = input("Ingresa la cadena que deseas buscar: ")
#Ingreso del idioma de búsqueda
idioma = input("Ingresa ES para español, EN para inglés: ")
#Reemplazo de espacios blancos por el signo +
nueva_cadena = cadena.replace(" ", "+")


#Cabecera del navegador
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'}
#URL de acceso a los resultados de busqueda
url = 'https://scholar.google.com/scholar?hl='+idioma+'&q='+nueva_cadena

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