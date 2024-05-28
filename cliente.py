import socket
import sys

class Client:
    def __init__(self, host, port):
        self.host= host
        self.port= port
        data = " ".join(sys.argv[1:])
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
    def enviar_msj(self, mensaje):
        self.mensaje = mensaje

        self.sock.sendto(mensaje.encode("UTF-8"), (self.host,self.port))

        received = self.sock.recvfrom(1024)

        print(received )      

if __name__ == "__main__":
    cliente=Client("localhost", 9999)
    cliente.enviar_msj("+, (KK, dfsjfgklj, 10, 3, 5, 6, 8)")
    cliente.enviar_msj("a, B")
