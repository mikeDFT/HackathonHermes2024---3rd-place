import socket

import threading

class Networking:
	def __init__(self, localIP, localPort, otherIP, otherPort):
		self.__otherIP = otherIP
		self.__otherPort = otherPort
		self.__localIP = localIP
		self.__localPort = localPort
		
		self.__socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.__socket.bind((localIP, localPort))
		
		self.__thread = threading.Thread(target=self.__listen)
		self.__thread.start()
		
	
	def send(self, data: str):
		self.__socket.sendto(data.encode(), (self.__otherIP, self.__otherPort))
	
	
	def __listen(self):
		while True:
			self.send("Testing " + self.__localIP)
			data = self.__socket.recv(1024)
			print(data.decode())
	
	
	def refresh(self):
		pass
	
	
def __main__():
	networking = Networking("", 1234, "", 1234)
	