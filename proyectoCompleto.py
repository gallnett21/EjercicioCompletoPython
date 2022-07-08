from tkinter import *
import sqlite3

#Crea lo básico de la interfaz gráfica
root=Tk()
root.title("Proyecto Completo")

#Creación del frame
frame=Frame(root)
frame.pack()

#crea la conexión a la base de datos
miConexion=sqlite3.connect("ProyectoCompleto")
miCursor=miConexion.cursor()

root.mainloop()