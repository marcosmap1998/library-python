from tkinter import messagebox
import sqlite3

#Función que nos hace conectar con nuestra BD
def conecta():
    conector = sqlite3.connect('database_library')
    cursor = conector.cursor()

    try:
        cursor.execute('''CREATE TABLE libros_db (
            issn VARCHAR(8) PRIMARY KEY,
            titulo VARCHAR(30) NOT NULL,
            autor VARCHAR(50) NOT NULL,
            tema VARCHAR(15) NOT NULL,
            editorial VARCHAR(15) NOT NULL,
            lugar VARCHAR(20),
            anio VARCHAR(4)
        )''')
        conector.commit()
        messagebox.showinfo('BBDD', 'La base de datos ha sido creada')
    except sqlite3.OperationalError:
        messagebox.showwarning('BBDD', 'La base de datos ya a sido conectada')

#Funcion para cerrar la bd
def desconecta():
    conector = sqlite3.connect('database_library')
    conector.close()
    messagebox.showinfo('BBDD', 'La base de datos ha sido desconectada')

#Funcion para salir de la app
def salir(raiz):
    resp = messagebox.askquestion('Salir', '¿Estás seguro que deseas salir de la aplicación?')

    if resp == 'yes':
        raiz.destroy()