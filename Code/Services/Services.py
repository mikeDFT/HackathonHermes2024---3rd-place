import pygame

from Code.Repository import Repo

class Services:
	def __init__(self):
		self.__Events = []
		self.__state = "MainMenu"
		self.__repo = Repo.Repo()
	
	def connectEvent(self, eventDict: dict):
		# eventDict = { # template
		# 	"State": "MainMenu",
		# 	"ID": 123,  # ID=-1 is for events that won't ever be unbinded
		# 	"Type": pygame.MOUSEBUTTONDOWN,
		# 	"Func": self.__clickedButton,
		# 	"Args": [button.x, button.y, button.width, button.height, func, extraArgsClick]
		# }
		
		self.__Events.append(eventDict)
		return eventDict["ID"]
	
	
	def disconnectEvent(self, eventID: int):
		for event in self.__Events:
			if event["ID"] == eventID:
				self.__Events.remove(event)
				return
			
	
	def __handleEvents(self):
		for event in pygame.event.get():
			for eventFunction in self.__Events:
				if ("State" not in eventFunction or eventFunction["State"] == self.__state) and eventFunction["Type"] == event.type:
					eventFunction["Func"](*eventFunction["Args"])
					


	def refresh(self):
		self.__handleEvents()
	