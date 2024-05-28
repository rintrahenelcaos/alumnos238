from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import re

class Lanzador_Vista:

    def __init__(self,master):
        self.masterlanzador = master
        self.masterlanzador.title("Alumnos 238 - Lanzador")

        self.avisobloqueo=StringVar()
        
        self.titulo = Label(self.masterlanzador, text="Seleccione como quiere trabajar",  height=1, width=60)
        self.titulo.grid(row=0, column=0, columnspan=5, padx=1, pady=1, sticky="w")

        self.boton_local = Button(self.masterlanzador, text="Local")
        self.boton_local.grid(row=1, column=0)

        self.boton_cliente = Button(self.masterlanzador, text="Cliente")
        self.boton_cliente.grid(row=1, column=2)

        self.boton_servidor = Button(self.masterlanzador, text="Servidor")
        self.boton_servidor.grid(row=1, column=4)

        self.boton_salida=Button(self.masterlanzador, text="Salir")
        self.boton_salida.grid(row=2, column=1, columnspan=3, pady=20)

    def fallo_de_conexion(self,):
        from tkinter import messagebox
        messagebox.showerror("Error", "Fallo la conexión con el Server")

    def salida(self,):
        self.terminar=messagebox.askquestion("Salir", "¿Esta seguro de que quiere salir?")   

if __name__ == "__main__":
    main = Tk()
    aplicacion = Lanzador_Vista(main)
    
    main.mainloop()
    