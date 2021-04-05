import tkinter as tk
from tkinter import * 

root = tk.Tk()
root.title('Plan de búsqueda')
root.iconbitmap('../pajaro.ico')
root.geometry("600x400")

#Logo
lbllogo = Label(root, text="Plan de busqueda",  padx=30, pady=20)
lbllogo.grid(row=0, column=0)

#Pregunta investigada
lblpreguntainv = Label(root, text="Pregunta investigada", padx=30, pady=20)
lblpreguntainv.grid(row=0, column=1)

#Realizar otro plan de busqueda
button_Retornar = Button(root, text="Realizar otro plan \n de busqueda", padx=30, pady=20)
button_Retornar.grid(row=0, column=2)

#Elementos a buscar
lblele = Label(root, text="Elementos a buscar \n - Articulo \n - Revista \n - Conferencia \n ...")
lblele.grid(row=1, column=0)


#Descriptores
lbldescr = Label(root, text="Descriptores \n  Lorem ipsum dolor sit amet,\n consectetur adipiscing elit,\n sed do eiusmod tempor incididunt \n ut labore et dolore magna aliqua.")
lbldescr.grid(row=2, column=0)


#Distractores
lbldistr = Label(root, text="Descriptores \n  Lorem ipsum dolor sit amet,\n consectetur adipiscing elit,\n sed do eiusmod tempor incididunt \n ut labore et dolore magna aliqua.")
lbldistr.grid(row=3, column=0)

#Frame resultados
frame = tk.Frame(root, width=350, height=400)
frame.grid(row=1, column=1, columnspan=2, rowspan=3)

#Resultados
lbltr1 = Label(frame, text="\nTitulo articulo 1", font=('Times', '16', 'italic'))
lbltr1.pack(anchor=W)
lblar1 = Label(frame, text="Author: P rodman - Libro - Fecha publicación")
lblar1.pack(anchor=W)
lbldes1 = Label(frame, text="Descripción: \n")
lbldes1.pack(anchor=W)

lbltr2 = Label(frame, text="Titulo articulo 2" , font=('Times', '16', 'italic'))
lbltr2.pack(anchor=W)
lblar2 = Label(frame, text="Author: P rodman - Libro - Fecha publicación")
lblar2.pack(anchor=W)
lbldes2 = Label(frame, text="Descripción: \n")
lbldes2.pack(anchor=W)

lbltr3 = Label(frame, text="Titulo articulo 3" , font=('Times', '16', 'italic'))
lbltr3.pack(anchor=W)
lblar3 = Label(frame, text="Author: P rodman - Libro - Fecha publicación")
lblar3.pack(anchor=W)
lbldes3 = Label(frame, text="Descripción: \n")
lbldes3.pack(anchor=W)

root.mainloop()