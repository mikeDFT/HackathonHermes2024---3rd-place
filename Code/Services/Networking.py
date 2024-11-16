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
		
		
	
	def __listen(self):
		while True:
			self.__socket.
			data = self.__socket.recv(1024)
			print(data)
	
	
	def refresh(self):
	
	
	