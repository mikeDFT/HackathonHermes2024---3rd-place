import random
from Code.Domain.Platform import Platform

class MapManager:
    def __init__(self, screen):
        self.screen = screen
        self.maps = [
            {},
            {
                "MAP": [
                Platform(self.screen, 150, 100, 250, 50),
                Platform(self.screen, 850, 450, 200, 40),
                Platform(self.screen, 400, 300, 190, 55),
                Platform(self.screen, 650, 250, 310, 50),
                Platform(self.screen, 100, 550, 170, 45),
                Platform(self.screen, 450, 500, 160, 40),
                Platform(self.screen, 750, 100, 280, 35),
                Platform(self.screen, 250, 650, 210, 50),
                Platform(self.screen, 950, 400, 230, 45)
                ],
                "ID": 1
            },
            {
                "MAP": [
                Platform(self.screen, 100, 150, 200, 40),
                Platform(self.screen, 800, 500, 220, 60),
                Platform(self.screen, 300, 350, 180, 50),
                Platform(self.screen, 600, 200, 300, 45),
                Platform(self.screen, 50, 500, 180, 35),
                Platform(self.screen, 500, 550, 150, 50),
                Platform(self.screen, 700, 50, 270, 30),
                Platform(self.screen, 200, 600, 220, 60),
                Platform(self.screen, 900, 350, 240, 40)
                ],
                "ID": 2
            },
            {
                "MAP": [
                Platform(self.screen, 120, 120, 230, 50),
                Platform(self.screen, 900, 490, 210, 45),
                Platform(self.screen, 350, 300, 200, 60),
                Platform(self.screen, 650, 180, 280, 40),
                Platform(self.screen, 80, 520, 190, 50),
                Platform(self.screen, 480, 480, 170, 40),
                Platform(self.screen, 730, 80, 260, 35),
                Platform(self.screen, 280, 620, 220, 55),
                Platform(self.screen, 970, 390, 250, 50)
                ],
                "ID": 3
            },
            {
                "MAP":[
                Platform(self.screen, 130, 110, 250, 60),
                Platform(self.screen, 800, 650, 210, 45),
                Platform(self.screen, 370, 340, 180, 50),
                Platform(self.screen, 620, 190, 300, 55),
                Platform(self.screen, 90, 510, 190, 50),
                Platform(self.screen, 780, 70, 280, 30),
                Platform(self.screen, 260, 640, 220, 50),
                Platform(self.screen, 950, 410, 230, 40)
                ],
                "ID": 4
            }

        ]

    def getRandomMap(self):
        return random.choice(self.maps)

    def getMapById(self, id):
        return self.maps[id]