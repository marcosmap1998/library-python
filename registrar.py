from tkinter import messagebox
import sqlite3

#Función para borrar los campos
def borrar_campos(y1,y2,y3,y4,y5,y6,y7):
    y1.set('')
    y2.set('')
    y3.set('')
    y4.set('')
    y5.set('')
    y6.set('')
    y7.set('')

#Funcion para dar de alta los datos en nuestra BD
def registra(y1,y2,y3,y4,y5,y6,y7):
    conector = sqlite3.connect('database_library')
    cursor = conector.cursor()

    try:
        if y1.get()=='' or y2.get()=='' or y3.get()=='' or y4.get()=='' or y5.get()=='' or y6.get()=='' or y7.get()=='':
            messagebox.showinfo('Registrar', 'Todos los campos deben estar llenos')
        else:
            cursor.execute("INSERT INTO libros_db VALUES ('" + y1.get() + 
            "','" + y2.get() + 
            "','" + y3.get() +
            "','" + y4.get() +
            "','" + y5.get() +
            "','" + y6.get() +
            "','" + y7.get() + "')")
            conector.commit()
            messagebox.showinfo('Registrar', 'Los datos han sido guardados con éxito')
            y1.set('')
            y2.set('')
            y3.set('')
            y4.set('')
            y5.set('')
            y6.set('')
            y7.set('')

    except sqlite3.OperationalError:
        messagebox.showerror('Registrar', 'Los datos no se han podido guardar')
    finally:
        conector.close()
