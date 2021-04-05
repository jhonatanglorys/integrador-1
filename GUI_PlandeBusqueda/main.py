import tkinter as tk
from tkinter import * 

root = tk.Tk()
root.title('Plan de búsqueda')
root.iconbitmap('../pajaro.ico')
root.geometry("850x600")

lbl = Label(root, text="Plan de búsqueda", font=('Times', '30', 'italic'))
lbl.pack()

#Frame principal
frame = tk.Frame(root, width=400, height=500)
frame.pack(fill=None, expand=False)

#Pregunta - 1
lblpregunta = Label(frame, text="Pregunta", font=('Times', '15', 'italic'))
lblpregunta.grid(row=0, column=0)
epregunta= Entry(frame, width=130)
epregunta.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

#Elementos a buscar - 2,3

frameele = tk.Frame(frame, width=30)
frameele.grid(row=3, column=0, padx=10, pady=10)

lblelbuscar = Label(frame, text="Elementos a buscar", font=('Times', '15', 'italic'))
lblelbuscar.grid(row=2, column=0, padx=10, pady=10)


TOPPINGS = [
    ("Articulo","Articulo"),
    ("Revista","Revista"),
    ("Conferencia","Conferencia"),
    ("...","..."),
]

atributos = StringVar()

for text, topping in TOPPINGS:
    Checkbutton(frameele, text=text, variable=atributos, onvalue=topping).pack()
    

#Contexto - 2,3
lblcontexto = Label(frame, text="contexto", font=('Times', '15', 'italic'))
lblcontexto.grid(row=2, column=1)
econtexto= Text(frame, width=65, height=5)
econtexto.grid(row=3, column=1, columnspan=2, padx=10, pady=10)

#Descriptores - 4,5
lbldescr = Label(frame, text="Descriptores", font=('Times', '15', 'italic'))
lbldescr.grid(row=4, column=0)
edescr= Text(frame, width=30, height=5)
edescr.grid(row=5, column=0, padx=10, pady=10)

#Distractores - 4,5
lbldistr = Label(frame, text="Distractores", font=('Times', '15', 'italic'))
lbldistr.grid(row=4, column=1)
edistr= Text(frame, width=30, height=5)
edistr.grid(row=5, column=1, padx=10, pady=10)

#Estrategia de busqueda - 4,5
lblestb = Label(frame, text="Estrategia de busqueda", font=('Times', '15', 'italic'))
lblestb.grid(row=4, column=2)
eestb= Text(frame, width=30, height=5)
eestb.grid(row=5, column=2, padx=10, pady=10)

#Expresiones logicas de busqueda -6,7
lblexplog = Label(frame, text="Expresiones logicas de busqueda", font=('Times', '13', 'italic'))
lblexplog.grid(row=6, column=0)
eexplog= Text(frame, width=65, height=5)
eexplog.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

#Boton Buscar,Limpiar - 6,7
button_Buscar = Button(frame, text="Buscar", padx=50, pady=5, font=('Times', '15', 'italic'))
button_Buscar.grid(row=6, column=2)
button_Limpiar = Button(frame, text="Limpiar", padx=50, pady=5, font=('Times', '15', 'italic'))
button_Limpiar.grid(row=7, column=2)


root.mainloop()