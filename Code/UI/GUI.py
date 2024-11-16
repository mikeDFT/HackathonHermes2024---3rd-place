import pygame
from Code.Domain.Buttons import Button
from Code.Domain.Title import Title

from Code.Services import EventsHandler, Controls, Networking, MainServices

class GUI:
    def __init__(self):
        pygame.init()
        self.running = True
        self.current_screen = "menu"  # Start in the menu screen
        self.mainServices = MainServices.MainServices()
        self.setup_screen()

    def render_map(self):
        """
        Render the game map. This could be an image, objects, or any game elements.
        Here we render a simple placeholder for the map.
        """
        if self.current_screen == "game":
            self.screen.fill((0, 128, 0))  # Green background for the game map
            font = pygame.font.Font(None, 36)
            text = font.render("This is the Game Map", True, (255, 255, 255))
            self.screen.blit(text, (150, 100))  # Draw some text on the map

    def setup_screen(self):
        """
        Setup the screen with the menu, including buttons and title.
        """
        self.screen = pygame.display.set_mode((500, 800))
        self.screen.fill((171, 186, 124))  # Background color for the menu
        play_button = Button("PLAY", self.screen, (61, 83, 0), 500 / 2 - 250 / 2, 300, 250, 100, "PLAY", font_size=40)
        settings_button = Button("SETTINGS", self.screen, (61, 83, 0), 500 / 2 - 250 / 2, 450, 250, 100, "SETTINGS", font_size=40)
        title = Title("TITLE", self.screen, "Jocul Nostru", 245, 100)
        self.objects = [play_button, settings_button, title]
        self.connectEvents(self.objects)

    def quit(self):
        self.running = False
        
    def handleButtonClick(self, objects):
        mouse_pos = pygame.mouse.get_pos()
        for obj in objects:
            if isinstance(obj, Button) and obj.is_pressed(mouse_pos):
                if obj.getId() == "PLAY":
                    # Switch to the game screen when PLAY is clicked
                    self.current_screen = "game"
                elif obj.getId() == "SETTINGS":
                    # Add settings functionality if needed
                    print("Settings button clicked!")
    
    def connectEvents(self, objects):
        # quit
        self.mainServices.eventsHandler.connectEvent({
            "ID": 1,
            "Type": pygame.QUIT,
            "Func": self.quit,
            "Args": []
        })
        
        # button click events
        self.mainServices.eventsHandler.connectEvent({
            "ID": 2,
            "Type": pygame.MOUSEBUTTONDOWN,
            "Func": self.handleButtonClick,
            "Args": [objects]
        })
        

        while self.running:
            self.mainServices.refresh()
            
            # Clear the screen based on current screen state
            if self.current_screen == "menu":
                self.screen.fill((171, 186, 124))  # Menu background color
                for obj in objects:
                    obj.render()
            else:
                self.render_map()  # Render the game map when in the game screen

            # Update the display
            pygame.display.flip()

        pygame.quit()

if __name__ == "__main__":
    gui = GUI()
