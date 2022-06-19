from gpio import *
from tcp import *
from time import *

serverIP = "1.1.1.1" # GANTI IP
serverPort = 1234

client = TCPClient()

def onTCPConnectionChange(type):
	print("connection to " + client.remoteIP() + " changed to state " + str(type))

def onTCPReceive(data):
	print("received from " + client.remoteIP() + " with data: " + data)

def main():
	client.onConnectionChange(onTCPConnectionChange)
	print(client.connect(serverIP, serverPort))

	count = 0
	while True:
		count += 1
		# Membaca Suhu
		adc = analogRead(A0);
		volt = adc/float(1024)
		temp = 100-(volt*100)
		# Mengirim Suhu
		data = str(round(temp,2)) + " Celsius"
		print("sending to " + client.remoteIP() + " with data: " + data)
		client.send(data)
		sleep(5)

if __name__ == "__main__":
	main()
