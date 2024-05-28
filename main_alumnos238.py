""" ######################################################
    ### Trabajo realizado por: MAZZEO, Leonardo Mario ####
    ######################################################

    Alumnos238 es una aplicación destinada a la gestion de notas de cursos de secundaria.
            
    main.py es el módulo que controla el arranque del programa y su único objetivo es instanciar el objeto Lanzador albergado en control_alumnos238.

"""

from tkinter import *
from control_alumnos238seg import Lanzador

if __name__ == "__main__":
    main=Tk()
    aplicacion=Lanzador(main)
    
    main.mainloop()


