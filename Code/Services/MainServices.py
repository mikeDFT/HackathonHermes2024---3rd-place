
from Code.Services import Controls, EventsHandler, Networking
import threading
import socket

class MainServices:
	def __init__(self):
		self.eventsHandler = EventsHandler.EventsHandler()
		self.controls = Controls.Controls(eventsHandler=self.eventsHandler)
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s.connect(("8.8.8.8", 80))
		print("Your IP is: " + s.getsockname()[0])
		self.networking = Networking.Networking(s.getsockname()[0], 1234, "192.168.35.249", 1234)
		# self.networking = Networking.Networking("192.168.35.243", 1234, "192.168.35.249", 1234)
		# self.refresh()
		# self.__thread = threading.Thread(target=self.refresh)
		# self.__thread.start()
		
		
	def refresh(self):
		self.eventsHandler.refresh()
		
	
	def passPlayer(self, player):
		self.networking.passPlayer(player)
		self.controls.passPlayer(player)
	
	
	def passOtherPlayer(self, player):
		self.networking.passOtherPlayer(player)
			