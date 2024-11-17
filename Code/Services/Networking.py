import socket
import threading

from Code.Domain.Player import Player
from Code.Services.MapManager import MapManager


class Networking:
	def __init__(self, localIP, localPort, otherIP, otherPort):
		print("Networking: ", localIP, localPort, otherIP, otherPort)
		self.__otherIP = otherIP
		self.__otherPort = otherPort
		self.__localIP = localIP
		self.__localPort = localPort
		
		self.otherPlayer = None
		
		self.__socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.__socket.bind((localIP, localPort))
		
		self.__thread = threading.Thread(target=self.__listen)
		self.__thread.start()
		
	
	def passOtherPlayer(self, player: Player):
		self.otherPlayer = player
	
	
	def send(self, data: str):
		self.__socket.sendto(data.encode(), (self.__otherIP, self.__otherPort))
	
	
	def receive(self):
		data, addr = self.__socket.recvfrom(1024)
		return data.decode(), addr
	
	
	def __listen(self):
		while True:
			data, addr = self.receive()
			# print(f"Received: {data} from {addr}")
			
			if not self.otherPlayer:
				continue
			
			dataType = data.split(":")[0]
			if dataType == "MAP":
				map_id = int(data.split(":")[1])  # Extract map ID as integer
				# Retrieve the map from MapManager
				map_manager = MapManager(self.otherPlayer.screen)  # Assuming screen is accessible
				self.otherPlayer.platforms = map_manager.getMapById(map_id)["MAP"]
				self.otherPlayer.map_id = map_id
			elif dataType == "POS":
				data = data.split(":")[1]
				otherPlayerX, otherPlayerY = data.split(",")
				self.otherPlayer.rect.x = float(otherPlayerX)
				self.otherPlayer.rect.y = float(otherPlayerY)
			elif dataType == "LIFE":
				self.otherPlayer.life = int(data.split(":")[1])

# if __name__ == "__main__":
# 	networking = Networking("192.168.35.243", 1234, "192.168.35.244", 1234)
