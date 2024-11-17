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
		self.player = None
		self.map = None
		self.generateRndMap = None
		self.applyMapID = None
		
		self.__socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.__socket.bind((localIP, localPort))
		
		self.__thread = threading.Thread(target=self.__listen)
		self.__thread.start()
		
	def passPlayer(self, player: Player):
		self.player = player
		
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
			
			dataType = data.split(":")[0]
			if dataType == "POS":
				if not self.otherPlayer:
					continue
					
				data = data.split(":")[1]
				otherPlayerX, otherPlayerY = data.split(",")
				self.otherPlayer.rect.x = float(otherPlayerX)
				self.otherPlayer.rect.y = float(otherPlayerY)
			elif dataType == "LIFE":
				if not self.otherPlayer:
					continue
					
				self.otherPlayer.life = int(data.split(":")[1])
			elif dataType == "MAP":
				map_id = int(data.split(":")[1])  # Extract map ID as integer
				
				if map_id == 0: # other player has no map
					self.generateRndMap()
					continue
				
				# Retrieve the map from MapManager
				self.applyMapID(map_id)
			elif dataType == "REQ|MAP":
				if self.map:
					self.send("MAP:" + str(self.map["ID"]))
				else:
					self.send("MAP:0")
			elif dataType == "SABO":
				type = data.split(":")[1]
				value = data.split(":")[2]
				if type == "SPEED":
					self.player.speed = int(value)
				elif type == "JUMP":
					self.player.jump_strength = int(value)
				elif type == "KNOCK":
					self.player.pushStrength = int(value)
				

# if __name__ == "__main__":
# 	networking = Networking("192.168.35.243", 1234, "192.168.35.244", 1234)
