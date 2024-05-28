"""
######################################################
### Trabajo realizado por: MAZZEO, Leonardo Mario ####
######################################################

 control_alumnos238 es el modulo encargado de vincular los módulos de modelo y visual y controlar la aplicación  


"""

from tkinter import *
import threading
import os
import sys
from pathlib import Path
import subprocess
import sqlite3

import vista_alumnos238
import modelo_alumnos238
import observador_alumnos238
from cliente import Client
import vista_lanzador
from vista_server import VentanaServer

class Lanzador:

    
    def __init__(self, raizlanzador):
        """Clase encargada de lanzar las tres funcionalidades de la app"""
        self.raizlanzador=raizlanzador
        self.objeto_vista_lanzador = vista_lanzador.Lanzador_Vista(self.raizlanzador)

        self.objeto_vista_lanzador.boton_local.config(command=lambda: self.lanza_local())
        self.objeto_vista_lanzador.boton_cliente.config(command=lambda: self.lanza_cliente())
        self.objeto_vista_lanzador.boton_servidor.config(command=lambda: self.lanza_servidor())
        self.objeto_vista_lanzador.boton_salida.config(command=lambda:self.salidalanzador())

    def lanza_local(self,):
        """La app funciona sin conexión"""
        
        self.objeto_vista_lanzador.masterlanzador.destroy()
        self.aplicacion = Controlador()
        
    
    def lanza_servidor(self,):
        """permite inicializar el servidor"""
        
        self.objeto_vista_lanzador.masterlanzador.destroy()
        self.application = ControladorServer()
    
    def lanza_cliente(self,):
        """Lanza la app como cliente de un servidor. Se requiere que el servidor esté 
        funcionando previamente"""

        self.objeto_vista_lanzador.masterlanzador.destroy()
        self.aplicacion = Controlador(opcion="cliente")

    def salidalanzador(self,):
        """Sale de la app"""
        self.objeto_vista_lanzador.salida()
        if self.objeto_vista_lanzador.terminar=="yes":
            self.objeto_vista_lanzador.masterlanzador.destroy()


class Controlador:
    def __init__(self, opcion=""):

        """
        Se instancia Marco_base, que forma el vínculo con el módulo vista_alumnos238 
        y se vinculan las señales recibidas por los botones y planilla. Tiene dos modos,
        local y cliente. El último requiere la presencia del servidor para funcionar        
        
        """
        self.root_controlador=Tk()
        self.interruptor_planilla = True
        
        self.objeto_vista = vista_alumnos238.Marco_base(self.root_controlador)
        
        self.objeto_vista.boton_editar.config(command=lambda: self.control_carga())  
        self.objeto_vista.boton_elimnar.config(command=lambda: self.control_eliminar())  
        self.objeto_vista.boton_modificar.config(command=lambda: self.control_modificar())
        self.objeto_vista.boton_fapellido.config(command=lambda: self.control_filtro_apellido())  
        self.objeto_vista.boton_filtrocurso.config(command=lambda: self.control_filtro_curso())  
        self.objeto_vista.boton_todaslasentradas.config(command=lambda: self.control_sin_filtro())           
        self.objeto_vista.planilla.bind('<ButtonRelease-1>', self.objeto_vista.seleccionada)  
        self.objeto_vista.boton_salida.config(command=lambda:self.control_salida())
        self.control_coneccion()

        self.observadorpuro = observador_alumnos238.ConcreteObserverPuro(self.objeto_enganche)
        if opcion=="cliente":
            self.observadorcliente = observador_alumnos238.ConcreteObserverCliente(self.objeto_enganche)
            try :
                self.pruebaserver=Client("localhost", 9999)
                self.pruebaserver.enviar_msj("Mensaje de prueba, 1")

            except:
                self.objeto_vista.fallo_de_conexion()
                self.objeto_vista.master.destroy()
                raizlanza=Tk()
                regreso=Lanzador(raizlanza)
            

    def limpiaycarga(funcion):
        """Método de actualización de la planilla con prueba para evitar errores a la salida"""
        def paquete(self):
            aviso=funcion(self)
            
            try:    
                """Evita errores al cerrar el programa. """ 
                self.objeto_vista.limpia_planilla()
                
                self.objeto_vista.carga_planilla(self.objeto_enganche.enganche_planilla(self.interruptor_planilla))

            except:
                
                pass

            return aviso
        return paquete
    
        
    def comenta_estado(funcion):
        """Método de información sobre estado de las acciones desarrolladas a lo largo de la ejecución. Informa en la app y en consola a la vez"""
        def paquete(self):
            aviso=funcion(self)
            self.objeto_vista.noticia.set("Estado: "+aviso)

        return paquete
        

    @comenta_estado
    @limpiaycarga
    def control_coneccion(self) :
        """ Conección con la base de datos. """
            
        try:
            basedatos=sqlite3.connect("planillaalumnos1.db")
            self.objeto_enganche = modelo_alumnos238.Enganchedb(basedatos)
            self.objeto_enganche.constructor_tabla()
            self.objeto_vista.selector_curso["values"] = self.objeto_enganche.identificador_cursos()
            aviso=" Se ha cargado la base de datos 'planillaalumnos1.db'"
            
        except:
            self.objeto_vista.salida()
            aviso=" Ha fallado la carga de la base de datos 'planillaalumnos1.db'"

        return aviso
            
    @comenta_estado
    @limpiaycarga
    def control_carga(self):
        """ Carga de datos tras verificarse la ausencia de errores. """
            
        if self.objeto_vista.error_apellido():
            aviso=" Error, el Apellido solo acepta letras y espacios"
        elif self.objeto_vista.error_curso():
            aviso=" Error, debe ingresarse un curso"
       
        else:
            
            self.objeto_alumno = modelo_alumnos238.Alumno(lista_datos=self.objeto_vista.tomador_de_datos())
            self.objeto_enganche + self.objeto_alumno.tupla_carga
            self.objeto_vista.selector_curso["values"] = self.objeto_enganche.identificador_cursos() 
            aviso= " Se ha cargado una nueva entrada bajo el Apellido: "+self.objeto_vista.enapellido.get()
            self.objeto_vista.limpiador_ingresos()
        
        return aviso

    @comenta_estado
    @limpiaycarga
    def control_eliminar(self):
        """ Elimina la entrada seleccionada. """

        try:
            self.objeto_alumno = modelo_alumnos238.Alumno(lista_datos=self.objeto_vista.tomador_de_datos())
            self.objeto_enganche - (self.objeto_alumno.tupla_carga+self.objeto_vista.identif)
            self.objeto_vista.selector_curso["values"] = self.objeto_enganche.identificador_cursos()
            aviso=" Se ha eliminado la entrada bajo el apellido: "+self.objeto_vista.enapellido.get()
            self.objeto_vista.limpiador_ingresos()
        except:
            self.objeto_vista.falta_eleccion()
            aviso=" Error, debe seleccionar una entrada para eliminar"
        
        return aviso

    @comenta_estado
    @limpiaycarga
    def control_modificar(self):
        """ Modifica la entrada seleccionada tras confirmar la ausencia de errores. """
           
        if self.objeto_vista.identif==():
            self.objeto_vista.falta_eleccion()
            aviso=" Error, debe seleccionar una entrada para modificar"
        
        else:
            if self.objeto_vista.error_apellido():
                aviso=" Error, el Apellido debe comenzar con MAYÚSCULA"
            elif self.objeto_vista.error_curso():
                aviso=" Error, debe ingresarse un curso"
                    
            else:
                            
                self.objeto_alumno = modelo_alumnos238.Alumno(lista_datos=self.objeto_vista.tomador_de_datos())
                self.objeto_enganche * (self.objeto_alumno.tupla_carga+self.objeto_vista.identif)
                aviso=" Se ha modificado la  entrada bajo el Apellido "+self.objeto_vista.enapellido.get()
                self.objeto_vista.selector_curso["values"] = self.objeto_enganche.identificador_cursos()
                self.objeto_vista.limpiador_ingresos()
                self.objeto_vista.identif=()        
        
        return aviso

    @comenta_estado
    @limpiaycarga
    def control_filtro_apellido(self):
        """ Impone el filtro por primera letra del apellido. """ 
            
        self.objeto_enganche.filtra_apellido(self.objeto_vista.fapellido.get())
        self.interruptor_planilla = False
        aviso=" Solo se muestran entradas cuyo Apellido comienza con "+self.objeto_vista.fapellido.get()

        return aviso

    @comenta_estado
    @limpiaycarga
    def control_filtro_curso(self):
        """ Impone el filtro por curso. """
        self.objeto_enganche.filtra_curso(self.objeto_vista.fcurso.get())
        self.interruptor_planilla = False
        aviso=" Solo se muestran entradas correspondientes al curso: "+self.objeto_vista.fcurso.get()

        return aviso

    @comenta_estado
    @limpiaycarga
    def control_sin_filtro(self):
        """ Elimina todos los filtros. """
            
        aviso=" Se muestran todas las entradas existentes"
        self.interruptor_planilla = True

        return aviso

    @comenta_estado
    @limpiaycarga
    def control_salida(self):
        """ Cierra el programa. """
        self.objeto_vista.salida()
        if self.objeto_vista.terminar=="yes":
            aviso=" La ejecución del programa a terminado"
            self.objeto_vista.master.destroy()
            raizlanza=Tk()
            regreso=Lanzador(raizlanza)
            
        else: aviso=" Cancelada la terminación de la ejecución del programa"
        
        return aviso


procesoparalelo = ""

class ControladorServer:
    def __init__(self,):
        self.mainserver=Tk()
        self.objetovistaserver=VentanaServer(self.mainserver)
        
        self.raiz = Path(__file__).resolve().parent
        self.ruta_server = os.path.join(self.raiz,  'server.py')

        

        self.objetovistaserver.boton_apagar.config(command=lambda:self.finalizarserver())
        self.objetovistaserver.boton_prender.config(command=lambda:self.threadconexion())
        self.objetovistaserver.boton_salida.config(command=lambda:self.salir())
                

    def threadconexion(self, ): 

        if procesoparalelo != "":
            procesoparalelo.kill()
            threading.Thread(target=self.conectar, args=(True,), daemon=True).start()
        else:
            threading.Thread(target=self.conectar, args=(True,), daemon=True).start()

    def conectar(self,var):
        the_path =  self.ruta_server
        if var==True:
            global procesoparalelo
            procesoparalelo = subprocess.Popen([sys.executable, the_path])
            procesoparalelo.communicate()
            
        else:
            print("")
        
        
    def finalizarserver(self,):
        global procesoparalelo
        if procesoparalelo !="":
            procesoparalelo.kill() 
    
    def salir(self,):
        self.objetovistaserver.salida()
        if self.objetovistaserver.terminar=="yes":
            
            self.objetovistaserver.root.destroy()
            raizlanza=Tk()
            regreso=Lanzador(raizlanza)
        
        

        
        


