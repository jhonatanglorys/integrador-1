from bs4 import BeautifulSoup
import csv
import requests
import tkinter as tk
from tkinter import *


#Ingreso del idioma de búsqueda
idioma = "ES"

#Ingreso la cantidad que quiero de resultados (Multiplo de 10)
cantidadres = 10


#Metodo para realizar la busqueda
def buscarResultados(cadena, idioma, cantidadres):
    #Ingreso del parámetro de búsqueda
    subcadena = cadena.split(',')
    cadena = subcadena[0]

    #Reemplazo de espacios blancos por el signo +
    nueva_cadena = cadena.replace(" ", "+")


    #Crear nuevo archivo
    file = open('resultados.csv','w',encoding="ISO-8859-1")
    writer = csv.writer(file)


    #Escribir las cabeceras del archivo
    writer.writerow(['titulo','vinculo','resumen'])

    #Cabecera del navegador
    #headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'}
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36 Edg/89.0.774.77'}

    #URL de acceso a los resultados de busqueda
    url = 'https://scholar.google.com/scholar?hl='+idioma+'&q='+nueva_cadena

    #Respuesta obtenida
    response = requests.get(url, headers=headers)

    #creacion objeto BeaustifulSoup con los parametros requeridos para el webscraping
    soup= BeautifulSoup(response.content,'lxml')


    itbusqueda = cantidadres/10
    for i in range(0, int(itbusqueda)):
        start = i*10
        
        #URL de acceso a los resultados de busqueda
        url2 = 'https://scholar.google.com/scholar?hl='+idioma+'&q='+nueva_cadena+'&start='+str(start)
        
        #Respuesta obtenida
        response = requests.get(url2, headers=headers)

        #creacion objeto BeaustifulSoup con los parametros requeridos para el webscraping
        soup= BeautifulSoup(response.content,'lxml')

        for item in soup.select('[data-lid]'):
            #print(item)
            #Titulo del articulo
            titulo = str(item.select('h3')[0].get_text())

            tipodoc = titulo.find("[CITAS]")

            if tipodoc==-1:
                #vinculo del articulo
                vinculo = str(item.select('a')[0]['href'])
                print(vinculo)
                #Resumen
                resumen = str(item.select('.gs_rs')[0].get_text())
                print(resumen)
                print('-------------------')
                writer.writerow([str(titulo.encode('utf-8')),str(vinculo.encode('utf-8')),str(resumen.encode('utf-8'))]) 
            
        itbusqueda = int(itbusqueda) - 1
            
    file.close()











#Programa principal
root = tk.Tk()
root.title('Plan de búsqueda')
root.iconbitmap('./images/pajaro.ico')
root.geometry("850x300")

lbl = Label(root, text="Plan de búsqueda", font=('Times', '30', 'italic'))
lbl.pack()




def button_click():
    text = ''
    cadena = edescr.get(1.0,END)
    cadena2 = edistr.get(1.0,END)
    separador = ","
    vector = cadena.split(separador)
    vector2 = cadena2.split(separador)
    for ec in vector:
        for ec2 in vector2:
            text = text + ec.strip() + ' y ' + ec2.strip() +", "+ec.strip() + ' o ' + ec2.strip()+", "
    
    eexplog.insert(tk.END,text)  
       
      

    
    
#Frame principal
frame = tk.Frame(root, width=200, height=500)
frame.pack(fill=None, expand=False)

#Expresiones logicas de busqueda -6,7
eexplog= Text(frame, width=65, height=5)
eexplog.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

#Boton Buscar,Limpiar - 6,7
button_Buscar = Button(frame, text="Buscar", command=lambda: buscarResultados(eexplog.get(1.0,END),idioma,cantidadres),padx=50, pady=5, font=('Times', '15', 'italic'))
button_Buscar.grid(row=0, column=3)



root.mainloop()





















