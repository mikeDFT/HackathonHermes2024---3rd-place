from Code.Services import EventsHandler
from Code.Domain import Player
import pygame

class Controls:
	def __init__(self, eventsHandler: EventsHandler):
		self.__eventsHandler = eventsHandler
		self.__player = None
		
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
			},
			"S": {
				"FuncDown": self.__moveDown,
				"ArgsDown": [],
				"EventKey": pygame.K_s,
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
					"Func": controls["FuncUp"],
					"EventKey": controls["EventKey"],
					"Args": controls["ArgsUp"]
				})
			
	def passPlayer(self, player: Player):
		self.__player = player
			
	def __checkKey(self, keyLetter: str, keyState: str, func, args):
		func(*args)
				
	def __jump(self):
		if not self.__player:
			return
		
		print("Jump")
		self.__player.velocity_y = self.__player.jump_strength
		
	def __moveLeft(self):
		if not self.__player:
			return
		
		self.__player.velocity_x = self.__player.speed * -1
		print("Move left")
	
	def __moveRight(self):
		if not self.__player:
			return
		
		self.__player.velocity_x = self.__player.speed
		print("Move right")
		
		
	def __stopMove(self):
		if not self.__player:
			return
		
		self.__player.velocity_x = 0
		print("Stop move")
		
		
	def __moveDown(self):
		if not self.__player:
			return
		
		self.__player.velocity_y = self.__player.speed*50
		print("Move down")
		
	