import random
from Code.Domain.Platform import Platform
from Code.Services.ImageManager import ImageManager


class MapManager:
    def __init__(self, screen):
        self.screen = screen
        manager = ImageManager()
        self.background = manager.getPlatformBackground()
        self.maps = [
            {},
            {
                "MAP": [
                Platform(self.screen, self.background, 150, 100, 250, 50),
                Platform(self.screen, self.background, 850, 450, 200, 40),
                Platform(self.screen, self.background, 400, 300, 190, 55),
                Platform(self.screen, self.background, 650, 250, 310, 50),
                Platform(self.screen, self.background, 100, 550, 170, 45),
                Platform(self.screen, self.background, 450, 500, 160, 40),
                Platform(self.screen, self.background, 750, 100, 280, 35),
                Platform(self.screen, self.background, 250, 650, 210, 50),
                Platform(self.screen, self.background, 950, 400, 230, 45)
                ],
                "ID": 1
            },
            {
                "MAP": [
                Platform(self.screen, self.background, 100, 150, 200, 40),
                Platform(self.screen, self.background, 800, 500, 220, 60),
                Platform(self.screen, self.background, 300, 350, 180, 50),
                Platform(self.screen, self.background, 600, 200, 300, 45),
                Platform(self.screen, self.background, 50, 500, 180, 35),
                Platform(self.screen, self.background, 500, 550, 150, 50),
                Platform(self.screen, self.background, 700, 50, 270, 30),
                Platform(self.screen, self.background, 200, 600, 220, 60),
                Platform(self.screen, self.background, 900, 350, 240, 40)
                ],
                "ID": 2
            },
            {
                "MAP": [
                Platform(self.screen, self.background, 120, 120, 230, 50),
                Platform(self.screen, self.background, 900, 490, 210, 45),
                Platform(self.screen, self.background, 350, 300, 200, 60),
                Platform(self.screen, self.background, 650, 180, 280, 40),
                Platform(self.screen, self.background, 80, 520, 190, 50),
                Platform(self.screen, self.background, 480, 480, 170, 40),
                Platform(self.screen, self.background, 730, 80, 260, 35),
                Platform(self.screen, self.background, 280, 620, 220, 55),
                Platform(self.screen, self.background, 970, 390, 250, 50)
                ],
                "ID": 3
            },
            {
                "MAP":[
                Platform(self.screen, self.background, 130, 110, 250, 60),
                Platform(self.screen, self.background, 800, 650, 210, 45),
                Platform(self.screen, self.background, 370, 340, 180, 50),
                Platform(self.screen, self.background, 620, 190, 300, 55),
                Platform(self.screen, self.background, 90, 510, 190, 50),
                Platform(self.screen, self.background, 780, 70, 280, 30),
                Platform(self.screen, self.background, 260, 640, 220, 50),
                Platform(self.screen, self.background, 950, 410, 230, 40)
                ],
                "ID": 4
            }

        ]

    def getRandomMap(self):
        rnd = random.randint(1, len(self.maps)-1)
        return self.maps[rnd]

    def getMapById(self, id):
        return self.maps[id]