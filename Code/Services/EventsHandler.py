import pygame

from Code.Repository import Repo

class EventsHandler:
	def __init__(self):
		self.__Events = []
		self.__state = "MainMenu" # "MainMenu", "Game", "GameOver", "GameWon", "Settings"
		self.__repo = Repo.Repo()
	
	
	def changeState(self, newState: str):
		self.__state = newState
		
	def getState(self):
		return self.__state
	
	
	def connectEvent(self, eventDict: dict):
		# eventDict = { # template
		# 	"State": "MainMenu",
		# 	"ID": 123,  # ID=-1 is for events that won't ever be unbinded
		# 	"Type": pygame.MOUSEBUTTONDOWN,
		# 	"Func": self.__clickedButton,
		#	"EventKey": pygame.K_W,
		# 	"Args": [button.x, button.y, button.width, button.height, func, extraArgsClick]
		# }
		
		self.__Events.append(eventDict)
		return eventDict["ID"]
	
	
	def disconnectEvent(self, eventID: int):
		for event in self.__Events:
			if event["ID"] == eventID:
				self.__Events.remove(event)
				return


	def refresh(self):
		for event in pygame.event.get():
			for eventDict in self.__Events:
				if (("EventKey" not in eventDict or (event.type in [pygame.KEYUP, pygame.KEYDOWN] and eventDict["EventKey"] == event.key)) and
						("State" not in eventDict or eventDict["State"] == self.__state) and
						eventDict["Type"] == event.type):
					eventDict["Func"](*eventDict["Args"])