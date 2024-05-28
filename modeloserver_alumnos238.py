import datetime


def traducir_mensaje(mensaje):
        
    mensaje=mensaje.replace("(","")
    mensaje=mensaje.replace(")","")
    listatemp = mensaje.split(", ")
    operador=listatemp[0]
    if len(listatemp)==0: pass
    elif len(listatemp)<3:
        
        tuplasalida=tuple(listatemp[1])
    else:
        listadatos=listatemp[1:4]
        listavalores=[int(i) for i in listatemp[4:(len(listatemp)-2)]]
        nota=[float(listatemp[8])]
        indice=[(int(listatemp[-1]))]
        tuplasalida=tuple(listadatos+listavalores+nota+indice)
    print("Orden recibida:")
    print(f"Operador: {operador}")
    print(f"Tupla de información: {tuplasalida}")
    
    return operador,tuplasalida


def escribaserver(mensaje):
    fecha=datetime.datetime.now()
    operador,tuplasalida=traducir_mensaje(mensaje)
    escriba=open("registrodecambios.txt","a")
    escriba.write("\n" + fecha.strftime("%c")+" "+str(operador)+str(tuplasalida))



if __name__ == "__main__":
    #trad=Traductor_de_Server()
    oper,datos=traducir_mensaje("+, (-5, 4, 6, 7, 8, 25, 30, 1.0, 3)")
    print(oper,datos)
    escribaserver("+ ,( KK, dfsjfgklj, 10, 7, 8, 25, 30, 1.0, 3)")
