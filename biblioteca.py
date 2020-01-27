from tkinter import *
from tkinter import ttk

#Importamos nuestros módulos
from bbdd import *
from registrar import *
from actualizar import *
from eliminar import *
from consultar import *

root = Tk()
root.title('Biblioteca')
root.geometry('585x325')

#MENU para manejar la aplicación
menu = Menu(root)

#Menu para la bd y salir de la aplicacion
menu_bbdd = Menu(menu, tearoff=0)
menu_bbdd.add_command(label='Conectar', command=conecta)
menu_bbdd.add_command(label='Desconectar', command=desconecta)
menu_bbdd.add_separator()
menu_bbdd.add_command(label='Salir', command=lambda: salir(root))
menu.add_cascade(label='BBDD', menu=menu_bbdd)

#Menu para consultar la bd
new_wind = consulta()
menu_consulta = Menu(menu, tearoff=0)
menu_consulta.add_command(label='Consultar BD', command=lambda: new_wind.ventana_consulta())
menu.add_cascade(label='Consultar', menu=menu_consulta)

#Mostramos el menu en pantalla
root.config(menu=menu)

#Variables de texto para controlar las entradas
issn = StringVar()
titulo = StringVar()
autor = StringVar()
tema = StringVar()
editorial = StringVar()
lugar = StringVar()
anio = StringVar()

#CREAMOS LAS PESTAÑAS DE NAVEGACIÓN DE NUESTRA APP
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand='yes')
pest1 = Frame(notebook)
#pest2 = Frame(notebook)
pest3 = Frame(notebook)
pest4 = Frame(notebook)
notebook.add(pest1, text='Registrar')
#notebook.add(pest2, text='Información')
notebook.add(pest3, text='Actualizar')
notebook.add(pest4, text='Eliminar')

#Agregamos las etiquetas y entradas de texto

# ----------------------------------------------- REGISTRO --------------------------------------------------------
issn_label = Label(pest1, text='ISSN:')
issn_label.grid(row=0, column=0, padx=80, pady=5, sticky='w', columnspan=2)
titulo_label = Label(pest1, text='Título del libro:')
titulo_label.grid(row=1, column=0, sticky='w', padx=80, pady=5, columnspan=2)
autor_label = Label(pest1, text='Autor:')
autor_label.grid(row=2, column=0, sticky='w', padx=80, pady=5, columnspan=2)
tema_label = Label(pest1, text='Género/Tema:')
tema_label.grid(row=3, column=0, sticky='w', padx=80, pady=5, columnspan=2)
edit_label = Label(pest1, text='Editorial:')
edit_label.grid(row=4, column=0, sticky='w', padx=80, pady=5, columnspan=2)
lugar_label = Label(pest1, text='Lugar:')
lugar_label.grid(row=5, column=0, sticky='w', padx=80, pady=5, columnspan=2)
anio_label = Label(pest1, text='Año:')
anio_label.grid(row=6, column=0, sticky='w', padx=80, pady=5, columnspan=2)

issn_text = Entry(pest1, width=30, textvariable=issn)
issn_text.grid(row=0, column=1, columnspan=2)
issn_text.focus()
titulo_text = Entry(pest1, width=30, textvariable=titulo)
titulo_text.grid(row=1, column=1, columnspan=2)
autor_text = Entry(pest1, width=30, textvariable=autor)
autor_text.grid(row=2, column=1, columnspan=2)
tema_text = Entry(pest1, width=30, textvariable=tema)
tema_text.grid(row=3, column=1, columnspan=2)
edit_text = Entry(pest1, width=30, textvariable=editorial)
edit_text.grid(row=4, column=1, columnspan=2)
lugar_text = Entry(pest1, width=30, textvariable=lugar)
lugar_text.grid(row=5, column=1, columnspan=2)
anio_text = Entry(pest1, width=30, textvariable=anio)
anio_text.grid(row=6, column=1, columnspan=2)

btn_borra = Button(pest1, text='Borrar campos', width=20, command=lambda: borrar_campos(issn, titulo, autor, tema, 
editorial, lugar, anio))
btn_borra.grid(row=7, column=0, padx=80, pady=10, sticky=E)
btn_registrar = Button(pest1, text='Dar de alta', width=20, command=lambda: registra(issn, titulo, autor, tema, 
editorial, lugar, anio))
btn_registrar.grid(row=7, column=1, pady=10, sticky=E)

# ----------------------------------------------- CONSULTAR --------------------------------------------------------

'''tree = ttk.Treeview(pest2, height=15, columns=7)
tree.grid(row=0, column=0, columnspan=7)
tree.heading(0, text='ISSN', anchor=W)
tree.heading(1, text='Título', anchor=W)
tree.heading(2, text='Autor', anchor=W)
tree.heading(3, text='Género', anchor=W)
tree.heading(4, text='Editorial', anchor=W)
tree.heading(5, text='Lugar', anchor=W)
tree.heading(6, text='Año', anchor=W)'''

# ----------------------------------------------- ACTUALIZAR --------------------------------------------------------
issn_label = Label(pest3, text='ISSN:')
issn_label.grid(row=0, column=0, padx=80, pady=5, sticky='w', columnspan=2)
titulo_label = Label(pest3, text='Título del libro:')
titulo_label.grid(row=1, column=0, sticky='w', padx=80, pady=5, columnspan=2)
autor_label = Label(pest3, text='Autor:')
autor_label.grid(row=2, column=0, sticky='w', padx=80, pady=5, columnspan=2)
tema_label = Label(pest3, text='Género/Tema:')
tema_label.grid(row=3, column=0, sticky='w', padx=80, pady=5, columnspan=2)
edit_label = Label(pest3, text='Editorial:')
edit_label.grid(row=4, column=0, sticky='w', padx=80, pady=5, columnspan=2)
lugar_label = Label(pest3, text='Lugar:')
lugar_label.grid(row=5, column=0, sticky='w', padx=80, pady=5, columnspan=2)
anio_label = Label(pest3, text='Año:')
anio_label.grid(row=6, column=0, sticky='w', padx=80, pady=5, columnspan=2)

issn_text = Entry(pest3, width=30, textvariable=issn)
issn_text.grid(row=0, column=1, columnspan=2)
issn_text.focus()
titulo_text = Entry(pest3, width=30, textvariable=titulo)
titulo_text.grid(row=1, column=1, columnspan=2)
autor_text = Entry(pest3, width=30, textvariable=autor)
autor_text.grid(row=2, column=1, columnspan=2)
tema_text = Entry(pest3, width=30, textvariable=tema)
tema_text.grid(row=3, column=1, columnspan=2)
edit_text = Entry(pest3, width=30, textvariable=editorial)
edit_text.grid(row=4, column=1, columnspan=2)
lugar_text = Entry(pest3, width=30, textvariable=lugar)
lugar_text.grid(row=5, column=1, columnspan=2)
anio_text = Entry(pest3, width=30, textvariable=anio)
anio_text.grid(row=6, column=1, columnspan=2)

btn_busca = Button(pest3, text='Buscar ISSN', width=20, command=lambda: busca(issn, titulo, autor, tema, editorial, lugar, 
anio))
btn_busca.grid(row=7, column=0, padx=80, pady=10, sticky=E)
btn_actua = Button(pest3, text='Dar de alta', width=20, command=lambda: actualiza(issn, titulo, autor, tema, 
editorial, lugar, anio))
btn_actua.grid(row=7, column=1, pady=10, sticky=E)
btn_borra = Button(pest3, text='Borrar campos', width=20, command=lambda: borrar_campos(issn, titulo, autor, tema, 
editorial, lugar, anio))
btn_borra.grid(row=8, column=0, padx=80, pady=5, sticky=E)

# ----------------------------------------------- ELIMINAR --------------------------------------------------------
issn_label = Label(pest4, text='ISSN:')
issn_label.grid(row=0, column=0, padx=80, pady=10, sticky='w', columnspan=2)
issn_text = Entry(pest4, width=30, textvariable=issn)
issn_text.grid(row=0, column=1, columnspan=2)
issn_text.focus()

btn_eliminar = Button(pest4, text='Eliminar datos', width=20, command=lambda: elimina(issn))
btn_eliminar.grid(row=1, column=0, padx=60, pady=5, sticky=E)

root.mainloop()
