import pygame
from Code.Domain.Buttons import Button
from Code.Domain.Title import Title
from Code.Domain.Platform import Platform
from Code.Services import MainServices
from Code.Domain.Player import Player


class GUI:
    def __init__(self):
        pygame.init()
        self.lastTick = 0
        self.mainServices = MainServices.MainServices()
        self.running = True
        self.width = 1200
        self.height = 700
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.current_screen = "menu"  # Start in the menu screen
        self.setup_screen()
        self.player = None
        self.otherPlayer = None


    def render_map(self):
        """
        Render the game map. This could be an image, objects, or any game elements.
        Here we render a simple placeholder for the map.
        """
        if self.current_screen == "game":
            self.screen.fill((135, 206, 235))  # Sky-blue background for the game map

            # Create platforms
            platforms = [
                Platform(self.screen, 100, 150, 200, 40),
                Platform(self.screen, 800, 500, 220, 60),
                Platform(self.screen, 300, 350, 180, 50),
                Platform(self.screen, 600, 200, 300, 45),
                Platform(self.screen, 50, 500, 180, 35),
                Platform(self.screen, 500, 550, 150, 50),
                Platform(self.screen, 700, 50, 270, 30),
                Platform(self.screen, 200, 600, 220, 60),
                Platform(self.screen, 900, 350, 240, 40)
            ]

            if self.player.getHealth() == 0:
                self.current_screen = "game_over"

            for i in range(self.player.getHealth()):
                pygame.draw.circle(self.screen, (220, 20, 60), (i * 50 + 50, 50), 25)

            # Render platforms
            for platform in platforms:
                platform.render()

            currTick = pygame.time.get_ticks()
            deltaTime = currTick - self.lastTick
            self.lastTick = currTick

            # Handle and render the player
            self.player.update(deltaTime, self.mainServices.networking.send)  # Update the player's position
            self.player.handle_collisions(platforms)  # Check collisions with platforms
            self.player.render()  # Draw the player on the screen

            # if self.otherPlayer:
            #     self.otherPlayer.render()

    def render_game_over(self):
        if self.current_screen == "game_over":
            self.screen.fill((171, 186, 124))  # Background color for the menu
            return_button = Button("RETURN", self.screen, (61, 83, 0), self.width / 2 - 250 / 2, 300, 250, 100, "RETURN",
                                   font_size=40)
            title = Title("TITLE", self.screen, "GAME OVER", self.width / 2, 100)
            self.objects = [return_button, title]
            return_button.render()
            title.render()

    def setup_screen(self):
        """
        Setup the screen with the menu, including buttons and title.
        """
        self.screen.fill((171, 186, 124))  # Background color for the menu
        play_button = Button("PLAY", self.screen, (61, 83, 0), self.width / 2 - 250 / 2, 300, 250, 100, "PLAY", font_size=40)
        settings_button = Button("SETTINGS", self.screen, (61, 83, 0), self.width / 2 - 250 / 2, 450, 250, 100, "SETTINGS",
                                 font_size=40)
        title = Title("TITLE", self.screen, "Jocul Nostru", self.width / 2, 100)
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
                    # Initialize the player when entering the game
                    self.player = Player(self.screen, 50, 150)  # You can adjust player start position
                    self.otherPlayer = Player(self.screen, 50, 150)

                    self.otherPlayer = Player(self.screen, 300, 150)

                    self.mainServices.passPlayer(self.player)
                    self.mainServices.passOtherPlayer(self.otherPlayer)

                    self.mainServices.passPlayer(self.player)
                    self.mainServices.passOtherPlayer(self.otherPlayer)
                elif obj.getId() == "SETTINGS":
                    # Add settings functionality if needed
                    print("Settings button clicked!")
                elif obj.getId() == "RETURN":
                    # Switch back to the main menu when RETURN is clicked
                    self.current_screen = "menu"
                    self.setup_screen()  # Reset the menu screen

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
                for obj in self.objects:
                    obj.render()
            elif self.current_screen == "game":
                self.render_map()  # Render the game map when in the game screen
            elif self.current_screen == "game_over":
                self.render_game_over()  # Render the game over screen

            # Update the display
            pygame.display.flip()

        pygame.quit()


if __name__ == "__main__":
    gui = GUI()
