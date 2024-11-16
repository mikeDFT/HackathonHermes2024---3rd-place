
from Code.Services import Controls, EventsHandler, Networking
import threading


class MainServices:
	def __init__(self):
		self.__eventsHandler = EventsHandler.EventsHandler()
		self.__controls = Controls.Controls(eventsHandler=self.__eventsHandler)
		self.__networking = Networking.Networking("192.168.35.243", 1234, "192.168.35.244", 1234)
		
		self.__thread = threading.Thread(target=self.refresh)
		self.__thread.start()
		
	def refresh(self):
		while True:
			# self.__controls.refresh()
			self.__eventsHandler.refresh()
			self.__networking.refresh()
			
			
			
			