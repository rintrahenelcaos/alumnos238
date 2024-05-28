from tkinter import *
from tkinter import Label
from tkinter import Button
from tkinter import messagebox


theproc=""

class VentanaServer:
    def __init__(self, window):
        self.root = window
        self.root.title("Alumnos 238 - Acceso al Servidor")

            
        self.titulo = Label(self.root, text="Usted está en el control de Servidor", height=1, width=60)
        self.titulo.grid(row=0, column=0, columnspan=7, padx=1, pady=1, sticky="w")

        self.boton_salida=Button(self.root,text="Salir")
        self.boton_salida.grid(row=1,column=5, columnspan=4,pady=10)

        self.boton_prender=Button(self.root, text="Iniciar Servidor")
        self.boton_prender.grid(row=1, column=3)

        self.boton_apagar=Button(self.root, text="Apagar Servidor")
        self.boton_apagar.grid(row=1, column=1)

    def salida(self):  
        """Ventana emergente de consulta sobre salida"""
        self.terminar=messagebox.askquestion("Salir", "¿Esta seguro de que quiere salir?")
    

    
if __name__ == "__main__":
    main = Tk()
    aplicacion = VentanaServer(main)
    
    main.mainloop()
    

 