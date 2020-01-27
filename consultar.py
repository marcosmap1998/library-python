from tkinter import Toplevel, ttk, W, CENTER
import sqlite3

class consulta:

    def ventana_consulta(self):
        self.ventana = Toplevel()
        self.ventana.title('Consulta de ejemplares')

        #TABLA DE DATOS
        self.tree = ttk.Treeview(self.ventana, columns=2, height=10)
        self.tree.grid(row=0, column=0)
        self.tree.heading('#0', text='ISSN', anchor=CENTER)
        self.tree.heading('#1', text='Título', anchor=CENTER)
        '''self.tree.pack()
        self.tree.heading('#0', text='ISSN', anchor=W)
        self.tree.heading('#1', text='Título', anchor=W)
        self.tree.heading(2, text='Autor', anchor=W)
        self.tree.heading(3, text='Tema', anchor=W)
        self.tree.heading(4, text='Editorial', anchor=W)
        self.tree.heading(5, text='Lugar', anchor=W)
        self.tree.heading(6, text='Año', anchor=W)'''

        self.get_data()

    def run_query(self, query, parameters=()):
        conector = sqlite3.connect('database_library')
        cursor = conector.cursor()
        result = cursor.execute(query, parameters)
        conector.commit()
        return result

    def get_data(self):
        query = 'SELECT issn, titulo FROM libros_db'
        db_rows = self.run_query(query)
        for row in db_rows:
            self.tree.insert('',0,text=row[0], values=row[1])


        