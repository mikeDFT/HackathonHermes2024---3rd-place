import os
import pygame

class ImageManager:
    def __init__(self, soundsPath: str = None):
        # Determine the path for sounds relative to this script's directory if not specified
        if soundsPath is None:
            self.soundsPath = os.path.join(os.path.dirname(__file__), "Images/")

    def getHeart(self, str):
        heart = None
        if str == "red":
            heart = pygame.image.load(self.soundsPath + "redHeart.png")
            heart = pygame.transform.scale(heart, (50, 50))
        elif str == "green":
            heart = pygame.image.load(self.soundsPath + "greenHeart.png")
            heart = pygame.transform.scale(heart, (50, 50))
        else:
            heart = pygame.image.load(self.soundsPath + "redHeart.png")
            heart = pygame.transform.scale(heart, (50, 50))

        return heart

    def getBackground(self):
        background = pygame.image.load(self.soundsPath + "background.png")

        return background

