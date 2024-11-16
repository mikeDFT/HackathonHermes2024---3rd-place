from Code.Services import EventsHandler
import pygame

class Controls:
	def __init__(self, eventsHandler: EventsHandler):
		self.__eventsHandler = eventsHandler
		
		self.__controls = {
			"W": {
				"FuncDown": self.__jump,
				"ArgsDown": [],
				"EventKey": pygame.K_w,
			},
			"A": {
				"FuncDown": self.__moveLeft,
				"ArgsDown": [],
				"FuncUp": self.__stopMove,
				"ArgsUp": [],
				"EventKey": pygame.K_a,
			},
			"D": {
				"FuncDown": self.__moveRight,
				"ArgsDown": [],
				"FuncUp": self.__stopMove,
				"ArgsUp": [],
				"EventKey": pygame.K_d,
			}
		}
		
		ID = 1000
		for key in self.__controls:
			controls = self.__controls[key]
			
			self.__eventsHandler.connectEvent({
				# "State": "MainMenu", # no state => always
				"ID": ID,  # ID=-1 is for events that won't ever be unbinded
				"Type": pygame.KEYDOWN,
				"Func": controls["FuncDown"],
				"EventKey": controls["EventKey"],
				"Args": controls["ArgsDown"]
			})
			ID += 1
			
			if "FuncUp" in controls:
				self.__eventsHandler.connectEvent({
					# "State": "MainMenu", # no state => always
					"ID": ID,  # ID=-1 is for events that won't ever be unbinded
					"Type": pygame.KEYUP,
					"Func": controls["FuncDown"],
					"EventKey": controls["EventKey"],
					"Args": controls["ArgsUp"]
				})
			
			
			
	def __checkKey(self, keyLetter: str, keyState: str, func, args):
		func(*args)
				
	def __jump(self):
		print("Jump")
		
	def __moveLeft(self):
		print("Move left")
	
	def __moveRight(self):
		print("Move right")
		
	def __stopMove(self):
		print("Stop move")