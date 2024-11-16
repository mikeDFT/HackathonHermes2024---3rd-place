
from Code.Services import Controls, EventsHandler, Networking
import threading


class MainServices:
	def __init__(self):
		self.eventsHandler = EventsHandler.EventsHandler()
		self.controls = Controls.Controls(eventsHandler=self.eventsHandler)
		self.networking = Networking.Networking("localhost", 1234, "192.168.35.244", 1234)
		
		# self.refresh()
		# self.__thread = threading.Thread(target=self.refresh)
		# self.__thread.start()
		
	def refresh(self):
		# self.__controls.refresh()
		self.eventsHandler.refresh()
		self.networking.refresh()
		
	
	def passPlayer(self, player):
		self.controls.passPlayer(player)
	
	def passOtherPlayer(self, player):
		self.networking.passOtherPlayer(player)
			