from gpio import *
from tcp import *
from time import *

port = 1234
server = TCPServer()
data_server = "0"

def onTCPNewClient(client):
    def onTCPConnectionChange(type):
        print("Terkoneksi ke " + client.remoteIP() + " merubah status ke " + str(type))

    def onTCPReceive(data):
        global data_server
        print("Menerima Perintah dari " + client.remoteIP() + " : " + data)
        data_server = data
        client.send("Sukses")

    client.onConnectionChange(onTCPConnectionChange)
    client.onReceive(onTCPReceive)

def main():
    global data_server
    server.onNewClient(onTCPNewClient)
    print(server.listen(port))
    pinMode(0, OUT)

    # don't let it finish
    while True:
        # Set Lampu dengan customWrite ke D0
        customWrite(0, int(data_server))
        sleep(5)

if __name__ == "__main__":
    main()