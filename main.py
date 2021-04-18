from bs4 import BeautifulSoup
import csv
import requests

#Ingreso del parámetro de búsqueda
cadena = input("Ingresa la cadena que deseas buscar: ")
#Ingreso del idioma de búsqueda
idioma = input("Ingresa ES para español, EN para inglés: ")
#Reemplazo de espacios blancos por el signo +
nueva_cadena = cadena.replace(" ", "+")


#Crear nuevo archivo
file = open('resultados.csv','w')
writer = csv.writer(file)


#Escribir las cabeceras del archivo
writer.writerow(['titulo','vinculo','resumen'])

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
    titulo = item.select('h3')[0].get_text()
    print(titulo)
    #vinculo del articulo
    vinculo = item.select('a')[0]['href']
    print(vinculo)
    #Resumen
    resumen = item.select('.gs_rs')[0].get_text()
    print(resumen)
    print('-------------------')
    writer.writerow([titulo.encode('utf-8'),vinculo.encode('utf-8'),resumen.encode('utf-8')])

file.close()