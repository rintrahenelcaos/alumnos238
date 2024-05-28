import socketserver

import modeloserver_alumnos238





class MyUDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        
        
        data = self.request[0].strip()
        socket = self.request[1]
        
        
        print("recibida la orden: ",data)
        ordenrec=data.decode("UTF-8")
        modeloserver_alumnos238.escribaserver(ordenrec)

                
        value2 = 0xA0
        packed_data_2 = bytearray()
        packed_data_2 += value2.to_bytes(1, "big")
        socket.sendto(packed_data_2, self.client_address)
        self.accion=data.decode("UTF-8")
        


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    with socketserver.UDPServer((HOST, PORT), MyUDPHandler) as server:server.serve_forever()
