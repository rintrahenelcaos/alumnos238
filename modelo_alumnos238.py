"""######################################################
### Trabajo realizado por: MAZZEO, Leonardo Mario ####
######################################################

modelo_alumnos238 es el módulo encargado del manejo de datos y vínculo con la base de datos

"""

from tkinter import *
from observador_alumnos238 import Sujeto
import sqlite3



class Alumno:

    """ Clase definida para ingresar datos al sistema antes de ingresarlos a la base de datos"""

    peso_tp1 = 1 / 6
    peso_tp2 = 1 / 6
    peso_tp3 = 1 / 6
    peso_examen = 1 - peso_tp1 - peso_tp2 - peso_tp3

    def __init__(self, lista_datos):

        self.apellido = lista_datos[0]
        self.nombre = lista_datos[1]
        self.curso = lista_datos[2]
        self.tp1 = lista_datos[3]
        self.tp2 = lista_datos[4]
        self.tp3 = lista_datos[5]
        self.examen = lista_datos[6]
        self.nota = round(
            self.tp1 * self.peso_tp1
            + self.tp2 * self.peso_tp2
            + self.tp3 * self.peso_tp3
            + self.examen * self.peso_examen,
            0,
        )

        self.tupla_carga = (
            self.apellido,
            self.nombre,
            self.curso,
            self.tp1,
            self.tp2,
            self.tp3,
            self.examen,
            self.nota,
        )


class Procesodb(Sujeto):

    """ Clase definida para la modificación de la base de datos"""

    def __init__(self,basededatos):
        
        self.conector = basededatos
        self.apuntador=self.conector.cursor()
        self.tuplavista = ()
        self.lista_enganche = []
        
    

    def constructor_tabla(self):  
        """ Método que crea la tabla en la base de datos"""
        
        tabla = "CREATE TABLE IF NOT EXISTS alumnos(id INTEGER PRIMARY KEY AUTOINCREMENT, apellido TEXT NOT NULL, nombre TEXT NOT NULL, curso TEXT NOT NULL, tp1 INTEGER NOT NULL, tp2 INTEGER NOT NULL, tp3 INTEGER NOT NULL, examen INTEGER NOT NULL, nota INTEGER NOT NULL)"
        self.apuntador.execute(tabla)
        self.conector.commit()

    
    
    def __add__(self,tuplaadd):
        """ Método de carga de datos
        
        parametro: tuplacarga(Any)
            tupla de datos a cargar en la base de datos.

        """
        carga = "INSERT INTO alumnos(apellido, nombre, curso, tp1, tp2, tp3, examen, nota) VALUES (?,?,?,?,?,?,?,?)"
        self.apuntador.execute(carga, tuplaadd)
        self.conector.commit()
        self.notificar("+",tuplaadd)

    
    def __sub__(self,tuplasub):
        """Método de eliminación de la base de datos
        
        parametro: identif(Any)
            tupla de datos a eliminar de la base de datos consistente en el número de índice de entrada.

        """
        identif=(tuplasub[-1],)

        elimina = "DELETE FROM alumnos WHERE id=?;"
        self.apuntador.execute(elimina, identif)
        self.conector.commit()
        self.notificar("-",tuplasub)

    
   
    
    def __mul__(self, tuplamul):
        
        """Método de modoficación de la base de datos

        parametro: identif(Any)
            tupla de datos a eliminar de la base de datos consistente en el número de índice de entrada.
        parametro: tuplamodif(Any)
            tupla de datos a modificar en la base de datos.
                
        """
        
        cambio = "UPDATE alumnos SET apellido=?, nombre=?, curso=?, tp1=?, tp2=?, tp3=?, examen=?, nota=? WHERE id=?"
        self.apuntador.execute(cambio, tuplamul)
        self.conector.commit()
        self.notificar("*",tuplamul)



class Enganchedb(Procesodb):

    """ 
    Clase definida para la lectura de la base de datos y la devolución de información al módulo de control para su 
    presentación en el módulo visual.
    
    """
    def __init__(self, basededatos):
        super().__init__(basededatos)

    def identificador_cursos(self):  
        
        """Método que permite mostrar los cursos existentes en el filtro de la vista.
        
        retorno: lista_cursos(list)
            lista conteniendo los cursos para ingresar al filtro por curso

        """
        
        listatemp = []
        
        total_sql = "SELECT curso FROM alumnos"
        self.apuntador.execute(total_sql)
        tupla_cursos = self.apuntador.fetchall()
        for x in tupla_cursos:
            listatemp.append(str(x[0]))

        set_cursos = set(listatemp)
        lista_cursos = list(set_cursos)
                
        return lista_cursos

    def filtra_curso(self, nro):  
        
        """Método que filtra los datos a partir de un curso

        parametro: nro(Any)
            tupla que indica a la base de datos qué entradas devolver en función del curso

        retorno: tuplavista(tuple)
            tupla con los índices de las entradas a mostrar    
        
        """

        lista_tempporal = []
        
        total_sql = "SELECT * FROM alumnos"
        self.apuntador.execute(total_sql)
        fichas = self.apuntador.fetchall()
        for caminante in fichas:
            testeable = caminante[3]
            if testeable == str(nro):
                lista_tempporal.append(caminante[0])
                self.tuplavista = tuple(lista_tempporal)
        #self.notificar()
        
        return self.tuplavista

    def enganche_planilla(self, interruptor_planilla=True):  
        
        """Método de lectura de la base de datos para aplicar los filtros
        
        parametro: interruptor_planilla(bool)
            indica si se deben devolver todas las entradas o se han aplicado filtros
            por descarte interruptor_planilla=True -> se devuelven todas las entradas

        retorno: datos_planilla(list)
            lista de listas con los datos a mostrar en la planilla

        """
        
        lista_enganche = []
        
        if interruptor_planilla == True:
            seleccion_sql = "SELECT * FROM alumnos"
            self.apuntador.execute(seleccion_sql)
            filas = self.apuntador.fetchall()
            for identif in filas:
                lista_enganche.append(identif[0])
            
        elif interruptor_planilla == False:
            for x in self.tuplavista:
                seleccion_sql = "SELECT * FROM alumnos WHERE id=?;"
                self.apuntador.execute(seleccion_sql, (x,))
                filas = self.apuntador.fetchall()
                for identif in filas:
                    lista_enganche.append(identif[0])
            
        datos = []
        datos_planilla=[]
        
        tupl_gancho = tuple(lista_enganche)
        
        for x in tupl_gancho:
            tuplauso = (x,)
            seleccion_sql = "SELECT * FROM alumnos WHERE id=?;"
            self.apuntador.execute(seleccion_sql, tuplauso)
            datos = self.apuntador.fetchall()

            for ficha in datos:
                datos_planilla.append(ficha)
                
            
        return datos_planilla

    
    def filtra_apellido(self, letra):  
        
        """Método que filtra los datos a partir de la primera letra del apellido

        parametro: letra (Any)
            tupla que indica a la base de datos qué entradas devolver en función de la letra del apellido

        retorno: tuplavista(tuple)
            tupla con los índices de las entradas a mostrar    
        
        """
        
        lista_tempporal = []
        
        total_sql = "SELECT * FROM alumnos"
        self.apuntador.execute(total_sql)
        fichas = self.apuntador.fetchall()
        for caminante in fichas:
            testeable = caminante[1]
            if testeable[0] == letra:
                lista_tempporal.append(caminante[0])
        self.tuplavista = tuple(lista_tempporal)
        #self.notificar()
        
        return self.tuplavista