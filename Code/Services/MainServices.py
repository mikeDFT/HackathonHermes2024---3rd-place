
import Controls, EventsHandler, Networking

class MainServices:
	def __init__(self):
		self.__controls = Controls.Controls()
		self.__eventsHandler = EventsHandler.EventsHandler()
		self.__networking = Networking.Networking()
		
		
	def refresh(self):
		self.__controls.refresh()
		self.__eventsHandler.refresh()
		self.__networking.refresh()