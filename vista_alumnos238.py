"""######################################################
### Trabajo realizado por: MAZZEO, Leonardo Mario ####
######################################################

vista_alumnos238 es el módulo visual de la aplicación. Es llamado solo por control alumnos para mantener la arquitectura MVC.
"""
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import re


listado_cursos = []

class Lanzador_Vista:

    def __init__(self,master):
        self.master = master
        self.master.title("Alumnos 238 - Acceso a la Base de Datos")

        self.titulo = Label(self.master, text="Ingrese sus datos", bg="DarkOrchid3", fg="thistle1", height=1, width=60)
        self.titulo.grid(row=0, column=0, columnspan=4, padx=1, pady=1, sticky="w")


class Marco_base:

    """
    Clase que define el objeto encargado de los aspectos visuales de la aplicación.
    """

    lista_valores = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    lista_letras = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    

    def __init__(self, master):
        
        self.master = master
        self.master.title("Alumnos 238")
        self.master.geometry("1040x500")  

        """
        Se inician las Variables de entrada desde el GUI y vinculo con control. Además se define la estructura de la vista
        """

        self.identif=()
        self.enapellido = StringVar()
        self.ennombre = StringVar()
        self.encurso = StringVar()
        self.entp1 = IntVar()
        self.entp2 = IntVar()
        self.entp3 = IntVar()
        self.enexamen = IntVar()
        self.ennota = IntVar()
        self.fapellido = StringVar()
        self.fcurso = StringVar()
        self.listado_cursos = []
        self.noticia=StringVar()
        self.noticia.set("Estado: ")


        """
        MARCOS Y TITULOS
        usados para ordenar la vista de la aplicación.
        """
        
        self.fijador=Label(self.master, width=1)
        self.fijador.grid(row=1,column=0)

        self.titulo_editar = Label(
            self.master, text="Editar", relief=GROOVE, width=60, padx=0
        )
        self.titulo_editar.grid(row=1, column=1, columnspan=3)

        self.titulo_filtrar = Label(
            self.master, text="Filtrar datos", relief=GROOVE, width=60, padx=0
        )
        self.titulo_filtrar.grid(row=1, column=4, columnspan=3)

        marco_editar = ttk.Frame(self.master)
        marco_editar.grid(row=10, column=1, columnspan=3)
        
        marco_planilla=ttk.Frame(self.master)
        marco_planilla.grid(column=1, row=0, columnspan=7)

        """ 
        EDICION
        Definidos para la modificación de los datos de la base de datos.
        """
        """BOTONES"""
        

        self.boton_editar = Button(marco_editar, text="Agregar entrada")
        self.boton_editar.pack(side=LEFT, expand=TRUE, fill=BOTH)

        self.boton_elimnar = Button(marco_editar, text="Eliminar entrada")
        self.boton_elimnar.pack(side=LEFT, expand=TRUE, fill=BOTH)

        self.boton_modificar = Button(marco_editar, text="Modificar entrada")
        self.boton_modificar.pack(side=LEFT, expand=TRUE, fill=BOTH)

        """CAMPOS DE ENTRADA"""

        self.apellido_entrada = Label(self.master, text="Apellido")
        self.apellido_entrada.grid(row=2, column=2, sticky=W)

        self.entry_apellido = Entry(self.master, textvariable=self.enapellido)
        self.entry_apellido.grid(row=2, column=3)

        self.nombre_entrada = Label(self.master, text="Nombre")
        self.nombre_entrada.grid(row=3, column=2, sticky=W)

        self.entry_nombre = Entry(self.master, textvariable=self.ennombre)
        self.entry_nombre.grid(row=3, column=3)

        self.curso_entrada = Label(self.master, text="Curso")
        self.curso_entrada.grid(row=4, column=2, sticky=W)

        self.entry_curso = Entry(self.master, textvariable=self.encurso)
        self.entry_curso.grid(row=4, column=3)

        self.tp1_entrada = Label(self.master, text="TP1")
        self.tp1_entrada.grid(row=5, column=2, sticky=W)

        self.combo_tp1 = ttk.Combobox(self.master, textvariable=self.entp1, width=5)
        self.combo_tp1.grid(row=5, column=3)
        self.combo_tp1["values"] = self.lista_valores
        self.combo_tp1["state"] = "readonly"

        self.tp2_entrada = Label(self.master, text="TP2")
        self.tp2_entrada.grid(row=6, column=2, sticky=W)

        self.combo_tp2 = ttk.Combobox(self.master, textvariable=self.entp2, width=5)
        self.combo_tp2.grid(row=6, column=3)
        self.combo_tp2["values"] = self.lista_valores
        self.combo_tp2["state"] = "readonly"

        self.tp3_entrada = Label(self.master, text="TP3")
        self.tp3_entrada.grid(row=7, column=2, sticky=W)

        self.combo_tp3 = ttk.Combobox(self.master, textvariable=self.entp3, width=5)
        self.combo_tp3.grid(row=7, column=3)
        self.combo_tp3["values"] = self.lista_valores
        self.combo_tp3["state"] = "readonly"

        self.examen_entrada = Label(self.master, text="Examen")
        self.examen_entrada.grid(row=8, column=2, sticky=W)

        self.combo_examen = ttk.Combobox(
            self.master, textvariable=self.enexamen, width=5
        )
        self.combo_examen.grid(row=8, column=3)
        self.combo_examen["values"] = self.lista_valores
        self.combo_examen["state"] = "readonly"

        """
        FILTROS
        Usados para modificar la información que se muestra en la planilla.
        """
        """ BOTONES"""

        self.boton_fapellido = Button(self.master, text="Aplicar")

        self.boton_fapellido.grid(row=2, column=6)

        self.boton_filtrocurso = Button(self.master,text="Aplicar",)
        self.boton_filtrocurso.grid(row=3, column=6)

        self.boton_todaslasentradas = Button(self.master, text="Eliminar los filtros")
        self.boton_todaslasentradas.grid(row=5, column=5)

        """CAMPOS DE ENTRADA"""

        self.fapellido_entrada = Label(self.master, text="Filtro por Apellido", padx=0)
        self.fapellido_entrada.grid(row=2, column=4)

        self.selector_apellido = ttk.Combobox(
            self.master, width=5, textvariable=self.fapellido
        )
        self.selector_apellido["values"] = self.lista_letras
        self.selector_apellido["state"] = "readonly"
        self.selector_apellido.grid(row=2, column=5)

        self.fcurso_entrada = Label(self.master, text="Filtro por curso", padx=0)
        self.fcurso_entrada.grid(row=3, column=4)

        self.selector_curso = ttk.Combobox(
            self.master, width=5, textvariable=self.fcurso
        )
        self.selector_curso["values"] = self.listado_cursos
        self.selector_curso["state"] = "readonly"
        self.selector_curso.grid(row=3, column=5)

        """
        NOTIFICACIONES
        Texto que informa el último acto realizado.
        """

        self.notificaciones=Label(master, textvariable=self.noticia) 
        self.notificaciones.grid(row=11, column=1,columnspan=6 ,sticky=W, pady=10)

        """
        BOTON DE SALIDA
        permite cerrar la aplicación.
        """

        self.boton_salida=Button(master, text="Salir")
        self.boton_salida.grid(row=8, column=5)


        """
        PLANILLA
        Muestra la base de datos y permite su elección.
        """

        self.planilla = ttk.Treeview(marco_planilla)
        self.planilla["columns"] = (
            "apellido",
            "nombre",
            "curso",
            "tp1",
            "tp2",
            "tp3",
            "examen",
            "promedio",
        )
        self.planilla.column("#0", width=50, minwidth=40, anchor=W)
        self.planilla.column("apellido", width=295, minwidth=80, anchor=W)
        self.planilla.column("nombre", width=295, minwidth=80, anchor=W)
        self.planilla.column("curso", width=60, minwidth=60, anchor=CENTER)
        self.planilla.column("tp1", width=60, minwidth=60, anchor=CENTER)
        self.planilla.column("tp2", width=60, minwidth=60, anchor=CENTER)
        self.planilla.column("tp3", width=60, minwidth=60, anchor=CENTER)
        self.planilla.column("examen", width=60, minwidth=60, anchor=CENTER)
        self.planilla.column("promedio", width=60, minwidth=60, anchor=CENTER)

        self.planilla.pack(side=LEFT, expand=TRUE, fill=BOTH)
        self.planilla.heading("#0", text="ID")
        self.planilla.heading("apellido", text="APELLIDO")
        self.planilla.heading("nombre", text="NOMBRE")
        self.planilla.heading("curso", text="CURSO")
        self.planilla.heading("tp1", text="TP1")
        self.planilla.heading("tp2", text="TP2")
        self.planilla.heading("tp3", text="TP3")
        self.planilla.heading("examen", text="EXAMEN")
        self.planilla.heading("promedio", text="NOTA")

        self.scroller=Scrollbar(marco_planilla)
        self.scroller.configure(command=self.planilla)
        self.scroller.pack(side=RIGHT,expand=TRUE,fill=Y)

        self.planilla.configure(yscrollcommand=self.scroller.set)

        

        



    def limpiador_ingresos(self):
        """Método para limpiar los datos ingresados en los campos de entrada de edición."""
        self.enapellido.set("")
        self.ennombre.set("")
        self.encurso.set("")
        self.entp1.set(0)
        self.entp2.set(0)
        self.entp3.set(0)
        self.enexamen.set(0)

    def limpia_planilla(self): 
        """Método que limpia la planilla para permitir su actualización."""

        for x in self.planilla.get_children():
            self.planilla.delete(x)
        
    
    def seleccionada(self,event):   
        """
        Método que permite seleccionar entradas en la planilla para modificarlas en edición o eleminarlas. 
        Asegura que la entrada seleccionada en la planilla sea ingresada a los campos de edición

        parametro: event(Any) 
            definido a partir de la selección de una entrada en la planilla
            
        retorna: identif(tuple)
            consiste en una tupla conteniendo el número de índice de la entrada elegida"""
        
        entrada = self.planilla.focus()
                    
        self.enapellido.set(str(self.planilla.item(entrada)["values"][0]))
        self.ennombre.set(str(self.planilla.item(entrada)["values"][1]))
        self.encurso.set(str(self.planilla.item(entrada)["values"][2]))
        self.entp1.set(int(self.planilla.item(entrada)["values"][3]))
        self.entp2.set(int(self.planilla.item(entrada)["values"][4]))
        self.entp3.set(int(self.planilla.item(entrada)["values"][5]))
        self.enexamen.set(int(self.planilla.item(entrada)["values"][6]))

        self.identif = (self.planilla.item(entrada)["text"],)
        
        
        return self.identif
    
            
    def tomador_de_datos(self):  
        """
        Método para tomar los datos de la edición y enviarlos a la base de datos.

        retorno: lista_de_datos(list)
            lista con los datos editados para procesar en la base de datos

        """
        lista_de_datos=[]
        lista_de_datos.append(self.enapellido.get())
        lista_de_datos.append(self.ennombre.get())
        lista_de_datos.append(self.encurso.get())
        lista_de_datos.append(self.entp1.get())
        lista_de_datos.append(self.entp2.get())
        lista_de_datos.append(self.entp3.get())
        lista_de_datos.append(self.enexamen.get())
        
        return lista_de_datos
    
    def carga_planilla(self, datos):  
        """
        Método de ingreso de datos para mostrar en la planilla
        
        parametros: datos(Any)
            lista de lista con los datos a mostrar en la planilla
        """
    
        for ficha in datos:
            self.planilla.insert(
                "",
                "end",
                text=ficha[0],
                values=(
                    ficha[1],
                    ficha[2],
                    ficha[3],
                    ficha[4],
                    ficha[5],
                    ficha[6],
                    ficha[7],
                    ficha[8],
                ),tags="ent"
            )
        
    def salida(self):  
        """Ventana emergente de consulta sobre salida"""
        self.terminar=messagebox.askquestion("Salir", "¿Esta seguro de que quiere salir?")
            
    
    def error_apellido(self):
        """Control errores de edición en apellido y aviso"""
        condicionador = "[^a-zA-Z ]"
        error=False
        if re.search(condicionador, self.enapellido.get()):
            messagebox.showerror("Error", "El Apellido solo acepta letras y espacios")
            self.enapellido.set("")
            error=True
        else:
            
            temporal=self.enapellido.get()
            self.enapellido.set(temporal.title())
            
        return error

    
       
    def error_curso(self):  
        """Aviso de error al ingresar el curso"""
        error=False
        if self.encurso.get()=="":
            messagebox.showerror("Error", "Debe ingresarse un curso")
            self.encurso.set("")
            error=True
        return error


    def falta_eleccion(self):  
        """Aviso de error al no seleccionar una entrada"""
        messagebox.showerror("Error", "Debe seleccionar una entrada")
        

    def detector_errores(self):  
        """Control de errores de edición"""
        condicionador = "^[A-Z]"
        error=False
        if re.search(condicionador, self.enapellido.get()) and self.encurso.get() !="":
            pass

        elif self.encurso.get()=="":
            self.error_curso()
            self.noticia.set("Estado: Error, debe ingresarse un curso")
            error=True
            aviso="Estado: Error, debe ingresarse un curso"
            return aviso
        else:
            self.error_apellido()
            self.noticia.set("Estado: Error, el Apellido debe comenzar con MAYÚSCULA")
            error=True
            aviso="Estado: Error, el Apellido debe comenzar con MAYÚSCULA"
            return aviso
        
        return error
    
    def fallo_de_conexion(self,):
        
        messagebox.showerror("Error", "Fallo la conexión con el servidor")
                


    
    


