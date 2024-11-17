import os
import random

import pygame

class ImageManager:
    def __init__(self, imagesPath: str = None):
        # Determine the path for sounds relative to this script's directory if not specified
        if imagesPath is None:
            self.imagesPath = os.path.join(os.path.dirname(__file__), "Images/")

    def getHeart(self, str):
        heart = None
        if str == "red":
            heart = pygame.image.load(self.imagesPath + "redHeart.png")
            heart = pygame.transform.scale(heart, (50, 50))
        elif str == "green":
            heart = pygame.image.load(self.imagesPath + "greenHeart.png")
            heart = pygame.transform.scale(heart, (50, 50))
        else:
            heart = pygame.image.load(self.imagesPath + "redHeart.png")
            heart = pygame.transform.scale(heart, (50, 50))

        return heart

    def getBackground(self):
        background = pygame.image.load(self.imagesPath + "background.png")

        return background

    def getGameBackground(self, width, height):
        version = random.choice(["1.jpeg","2.jpeg"])
        name = "game_background" + version
        background = pygame.image.load(self.imagesPath + name)
        background = pygame.transform.scale(background, (width, height))

        return background

    def getPlayerIcon(self, str):
        player = None

        if str == "red":
            player = pygame.image.load(self.imagesPath + "redGuy.png")
        elif str == "blue":
            player = pygame.image.load(self.imagesPath + "blueGuy.png")

        return player