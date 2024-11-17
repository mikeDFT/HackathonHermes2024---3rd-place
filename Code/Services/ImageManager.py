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
            hearth = pygame.image.load(self.soundsPath + "redHeart.png")
            hearth = pygame.transform.scale(hearth, (50, 50))
        elif str == "green":
            hearth = pygame.image.load(self.soundsPath + "greenHeart.png")
            hearth = pygame.transform.scale(hearth, (50, 50))
        else:
            hearth = pygame.image.load(self.soundsPath + "redHeart.png")
            hearth = pygame.transform.scale(hearth, (50, 50))

        return hearth