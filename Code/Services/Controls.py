from Code.Services import EventsHandler
from Code.Domain import Player
import pygame

from Code.Services import SoundManager
sound_manager = SoundManager.SoundMan()

class Controls:
	# sound_manager = SoundManager()
	def __init__(self, eventsHandler: EventsHandler):
		self.__eventsHandler = eventsHandler
		self.__player = None
		
		self.__movingRight = False
		self.__movingLeft = False
		
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
				"ArgsUp": ["left"],
				"EventKey": pygame.K_a,
			},
			"D": {
				"FuncDown": self.__moveRight,
				"ArgsDown": [],
				"FuncUp": self.__stopMove,
				"ArgsUp": ["right"],
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
		
	
	def __move(self):
		if not self.__player:
			return
		
		velo = 0
		if self.__movingLeft:
			velo -= self.__player.speed
		if self.__movingRight:
			velo += self.__player.speed
		
		self.__player.velocity_x = velo
	
	def __jump(self):
		if not self.__player:
			return
		
		print(pygame.time.get_ticks() - self.__player.on_ground)
		if pygame.time.get_ticks() - self.__player.on_ground > 4000:
			return
		
		self.__player.rect.y -= 10
		self.__player.on_ground = 0
		sound_manager.playSound("jump")
		
		print("Jump")
		self.__player.velocity_y = self.__player.jump_strength
		
		
	def __moveLeft(self):
		if not self.__player:
			return
		
		self.__movingLeft = True
		
		self.__move()
		print("Move left")
	
	def __moveRight(self):
		if not self.__player:
			return
		
		self.__movingRight = True
		
		self.__move()
		print("Move right")
		
		
	def __stopMove(self, direction: str):
		if not self.__player:
			return
		
		if direction == "left":
			self.__movingLeft = False
		elif direction == "right":
			self.__movingRight = False
		
		self.__move()
		
	def __moveDown(self):
		return
		if not self.__player:
			return
		
		self.__player.velocity_y = self.__player.speed*50
		print("Move down")
		
	