
import Controls, EventsHandler, Networking
import threading


class MainServices:
	def __init__(self):
		self.__controls = Controls.Controls()
		self.__eventsHandler = EventsHandler.EventsHandler()
		self.__networking = Networking.Networking("192.168.35.243", 1234, "192.168.35.244", 1234)
		
		self.__thread = threading.Thread(target=self.__networking.refresh)
		self.__thread.start()
		
	def refresh(self):
		while True:
			self.__controls.refresh()
			self.__eventsHandler.refresh()
			self.__networking.refresh()