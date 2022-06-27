from tcp import *
from time import *

port = 1234
server = TCPServer()

def onTCPNewClient(client):
	def onTCPConnectionChange(type):
		print("connection to " + client.remoteIP() + " changed to state " + str(type))

	def onTCPReceive(data):
		print("received from " + client.remoteIP() + " Suhu Rumah: " + data)
		client.send("Accepted")

	client.onConnectionChange(onTCPConnectionChange)
	client.onReceive(onTCPReceive)

def main():
	server.onNewClient(onTCPNewClient)
	print(server.listen(port))

	# don't let it finish
	while True:
		sleep(3600)

if __name__ == "__main__":
	main()
