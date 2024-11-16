from codecs import namereplace_errors

import pygame
from Code.Domain.Buttons import Button

class GUI:
    def __init__(self):
        self.objects = []
        pygame.init()
        self.running = True
        self.setup_screen()
        self.game_loop()

    def render_map(self):
        pass

    def setup_screen(self):
        self.screen = pygame.display.set_mode((500, 800))
        self.screen.fill((171, 186, 124))
        button = Button(self.screen, (61, 83, 0), 150, 100, 100, 50, "salut")
        self.objects.append(button)


    def game_loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Clear the screen
            self.screen.fill((171, 186, 124))

            # Render the map
            self.render_map()

            # Example: Render a button
            for object in self.objects:
                object.render()

            # Update the display
            pygame.display.flip()

        pygame.quit()



if __name__ == "__main__":
    gui = GUI()
    gui.render_map()
