from tkinter import messagebox
import sqlite3

def elimina(y1):
    conector = sqlite3.connect('database_library')
    cursor = conector.cursor()

    try:
        resp = messagebox.askquestion('Eliminar registro', '¿Estás seguro de querer eliminar esta información?'+
        '\nNo se podrá recuperar')
        if resp == 'yes':
            cursor.execute("DELETE FROM libros_db WHERE issn = '" + y1.get() + "'")
            conector.commit()
            messagebox.showinfo('Eliminar registro', 'Información eliminada')
            y1.set('')
        
    except sqlite3.OperationalError:
        messagebox.showerror('Eliminar registro', 'No se pudo eliminar la información')
