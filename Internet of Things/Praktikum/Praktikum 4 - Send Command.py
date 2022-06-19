from tcp import *
from time import *

serverIP = "1.1.1.1" # GANTI IP
serverPort = 1234
set_lampu = "2" # Terang = 2, Redup = 1, dan Mati = 0
client = TCPClient()

def onTCPConnectionChange(type):
    print("Terkoneksi ke " + client.remoteIP() + " merubah status ke " + str(type))

def onTCPReceive(data):
    print("Status Perintah dari " + client.remoteIP() + " : " + data)

def main():
    global set_lampu
    client.onConnectionChange(onTCPConnectionChange)
    client.onReceive(onTCPReceive)
    print(client.connect(serverIP, serverPort))

    count = 0
    while True: # Kirim Perintah 3x
        # Mengirim Data dalam bentuk List
        print("Mengirim Perintah ke " + client.remoteIP() + " : " + set_lampu)
        client.send(set_lampu)
        sleep(5)

if __name__ == "__main__":
    main()

