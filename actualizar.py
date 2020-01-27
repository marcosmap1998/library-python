from tkinter import messagebox
import sqlite3

#Funcion para buscar el issn
def busca(y1,y2,y3,y4,y5,y6,y7):
    conector = sqlite3.connect('database_library')
    cursor = conector.cursor()

    try:
        cursor.execute("SELECT * FROM libros_db WHERE issn = '" + y1.get() + "'")
        conector.commit()
        registros = cursor.fetchall()

        for registro in registros:
            #y1.set(registro[0])
            y2.set(registro[1])
            y3.set(registro[2])
            y4.set(registro[3])
            y5.set(registro[4])
            y6.set(registro[5])
            y7.set(registro[6])

    except sqlite3.OperationalError:
        messagebox('Actualizar', 'No se han podido buscar los datos')
    finally:
        conector.close()

#Función para editar la info de la bd
def actualiza(y1,y2,y3,y4,y5,y6,y7):
    conector = sqlite3.connect('database_library')
    cursor = conector.cursor()

    try:
        if y1.get()=='' or y2.get()=='' or y3.get()=='' or y4.get()=='' or y5.get()=='' or y6.get()=='' or y7.get()=='':
            messagebox.showinfo('Registrar', 'Todos los campos deben estar llenos')
        else:
            cursor.execute("UPDATE libros_db SET issn = '" + y1.get() + 
            "', titulo = '" + y2.get() +
            "', autor = '" + y3.get() +
            "', tema = '" + y4.get() +
            "', editorial = '" + y5.get() +
            "', lugar = '" + y6.get() +
            "', anio = '" + y7.get() + "' WHERE issn = '" + y1.get() + "'")
            conector.commit()
            messagebox.showinfo('Actualizar', 'El registro ha sido actualizado')
            y1.set('')
            y2.set('')
            y3.set('')
            y4.set('')
            y5.set('')
            y6.set('')
            y7.set('')
    except sqlite3.OperationalError:
        messagebox.showerror('Actualizar', 'No se han podido actualizar los datos')
    finally:
        conector.close()
