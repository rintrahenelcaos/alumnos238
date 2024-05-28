from cliente import Client

class Sujeto:

    observadores = []

    def agregar(self, obj):
        self.observadores.append(obj)

    def quitar(self, obj):
        pass

    def notificar(self, *args):
        for observador in self.observadores:
            observador.update(args)


class Observador:
    def update(self):
        raise NotImplementedError("Delegación de actualización")

class ConcreteObserverCliente(Observador):
    
    def __init__(self, obj):
        self.observado_a = obj
        self.observado_a.agregar(self)
        self.clienteobs=Client("localhost", 9999)

    def update(self, *args):
        print("Actualización dentro de ConcreteObserverCliente")
        print(f"Aquí están los parámetros: {args[0][0]},{args[0][1]}")
        self.clienteobs.enviar_msj(str(args[0][0])+","+str(args[0][1]))

class ConcreteObserverPuro(Observador):
    def __init__(self, obj):
        self.observado_puro = obj
        self.observado_puro.agregar(self)
        

    def update(self, *args):
        print("Actualización dentro de ConcreteObserverPuro")
        print(f"Aquí están los parámetros: {args[0][0]},{args[0][1]}")

