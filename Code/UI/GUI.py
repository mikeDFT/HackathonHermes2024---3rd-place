import pygame
from Code.Domain.Buttons import Button
from Code.Domain.Title import Title
from Code.Domain.Platform import Platform
from Code.Services import MainServices
from Code.Domain.Player import Player
from Code.Domain.InputBox import InputBox
from Code.Services import SoundManager
from Code.Services.ImageManager import ImageManager

sound_manager = SoundManager.SoundMan()
image_manager = ImageManager()

class GUI:
    def __init__(self):
        pygame.init()
        self.lastTick = 0
        self.mainServices = MainServices.MainServices()
        self.running = True
        self.width = 1200
        self.height = 700
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.setup_screen()
        self.player = None
        self.otherPlayer = None


    def render_map(self):
        """
        Render the game map. This could be an image, objects, or any game elements.
        Here we render a simple placeholder for the map.
        """
        if self.mainServices.eventsHandler.getState() == "Game":
            self.screen.fill((135, 206, 235))  # Sky-blue background for the game map

            # Create platforms
            platforms = [
                Platform(self.screen, 150, 100, 250, 50),
                Platform(self.screen, 850, 450, 200, 40),
                Platform(self.screen, 400, 300, 190, 55),
                Platform(self.screen, 650, 250, 310, 50),
                Platform(self.screen, 100, 550, 170, 45),
                Platform(self.screen, 450, 500, 160, 40),
                Platform(self.screen, 750, 100, 280, 35),
                Platform(self.screen, 250, 650, 210, 50),
                Platform(self.screen, 950, 400, 230, 45)
            ]

            if self.player.getHealth() == 0:
                self.mainServices.eventsHandler.changeState("GameOver")

            if self.otherPlayer.getHealth() == 0:
                self.mainServices.eventsHandler.changeState("GameWon")

            greenHeart = image_manager.getHeart("green")
            for i in range(self.player.getHealth()):
                self.screen.blit(greenHeart, (i * 60 + 50, 25))

            # Render platforms
            for platform in platforms:
                platform.render()

            currTick = pygame.time.get_ticks()
            deltaTime = currTick - self.lastTick
            self.lastTick = currTick

            # Handle and render the player
            self.player.update(deltaTime, self.mainServices.networking.send)  # Update the player's position
            self.player.handle_collisions(platforms)  # Check collisions with platforms
            self.player.handle_otherPlayer_collisions(self.otherPlayer)
            self.mainServices.networking.send("POS:" + str(self.player.rect.x) + "," + str(self.player.rect.y))
            self.player.render()  # Draw the player on the screen
            self.otherPlayer.render()

            redHeart = image_manager.getHeart("red")
            for i in range(self.otherPlayer.getHealth()):
                self.screen.blit(redHeart, (i * 52 + 1000, 25))
            # if self.otherPlayer:
            #     self.otherPlayer.render()


            if self.otherPlayer:
                self.otherPlayer.render()
            #self.mainServices.refresh()

    def setup_screen(self):
        """
        Setup the screen with the menu, including buttons and title.
        """
        self.screen.fill((171, 186, 124))  # Background color for the menu
        play_button = Button("PLAY", self.screen, (61, 83, 0), self.width / 2 - 250 / 2, 300, 250, 100, "PLAY", font_size=40)
        settings_button = Button("SETTINGS", self.screen, (61, 83, 0), self.width / 2 - 250 / 2, 450, 250, 100, "SETTINGS",
                                 font_size=40)
        title = Title("TITLE", self.screen, "THE GAME", self.width / 2, 100)
        self.mainMenuObjects = [play_button, settings_button, title]


        self.screen.fill((171, 186, 124))  # Background color for the menu
        return_button = Button("RETURN", self.screen, (61, 83, 0), self.width / 2 - 250 / 2, 300, 250, 100, "RETURN",
                               font_size=40)
        title = Title("TITLE", self.screen, "GAME OVER", self.width / 2, 100)
        self.gameOverObjects = [return_button, title]

        title = Title("TITLE", self.screen, "YOU WON", self.width / 2, 100)
        self.gameWonObjects = [return_button, title]

        title = Title("TITLE", self.screen, "SETTINGS", self.width / 2, 100)
        ip_input_field = InputBox(self.screen, self.width / 2 - 450/2, 200, 450, 50)

        self.settingObjects = [ip_input_field, title, return_button]

        self.connectEvents()


    def quit(self):
        self.running = False


    def handleButtonClickMenus(self, objects):
        mouse_pos = pygame.mouse.get_pos()
        for obj in objects:
            if isinstance(obj, Button) and obj.is_pressed(mouse_pos):
                sound_manager.playSound("buttonSelect")
                if obj.getId() == "PLAY":
                    # Switch to the game screen when PLAY is clicked
                    self.mainServices.eventsHandler.changeState("Game")
                    # Initialize the player when entering the game
                    self.player = Player(self.screen, 50, 150, color=(50, 205, 50))  # You can adjust player start position

                    self.otherPlayer = Player(self.screen, 300, 150)
                    self.otherPlayer.rect.x = 100000

                    self.mainServices.passPlayer(self.player)
                    self.mainServices.passOtherPlayer(self.otherPlayer)
                    
                    self.mainServices.networking.send("LIFE:" + str(self.player.life))
                elif obj.getId() == "SETTINGS":
                    # Add settings functionality if needed
                    self.mainServices.eventsHandler.changeState("Settings")
                    self.render_setting()
                elif obj.getId() == "RETURN":
                    # Switch back to the main menu when RETURN is clicked
                    self.mainServices.eventsHandler.changeState("MainMenu")
                    self.render_main_menu()  # Reset the menu screen

    def handleKeypressInputbox(self, event):
        for obj in self.settingObjects:
            if isinstance(obj, InputBox):
                obj.handle_event(event)

    def keypress_wrapper(self):
        """
        Wrapper to handle keypress events by injecting the current event.
        """

        def wrapper(event):
            self.handleKeypressInputbox(event)

        return wrapper

    def connectEvents(self):
        # quit
        self.mainServices.eventsHandler.connectEvent({
            "ID": 1,
            "Type": pygame.QUIT,
            "State": "MainMenu",
            "Func": self.quit,
            "Args": []
        })

        # button click events
        self.mainServices.eventsHandler.connectEvent({
            "ID": 2,
            "Type": pygame.MOUSEBUTTONDOWN,
            "State": "MainMenu",
            "Func": self.handleButtonClickMenus,
            "Args": [self.mainMenuObjects]
        })

        # button click events
        self.mainServices.eventsHandler.connectEvent({
            "ID": 3,
            "Type": pygame.MOUSEBUTTONDOWN,
            "State": "GameOver",
            "Func": self.handleButtonClickMenus,
            "Args": [self.gameOverObjects]
        })

        self.mainServices.eventsHandler.connectEvent({
            "ID": 4,
            "Type": pygame.MOUSEBUTTONDOWN,
            "State": "GameWon",
            "Func": self.handleButtonClickMenus,
            "Args": [self.gameWonObjects]
        })

        self.mainServices.eventsHandler.connectEvent({
            "ID": 5,
            "Type": pygame.MOUSEBUTTONDOWN,
            "State": "Settings",
            "Func": self.handleButtonClickMenus,
            "Args": [self.settingObjects]
        })

        self.mainServices.eventsHandler.connectEvent({
            "ID": 6,
            "Type": pygame.KEYDOWN,
            "State": "Settings",
            "Func": lambda event: self.handleKeypressInputbox(event),  # Pass the event dynamically
            "Args": []  # No static arguments needed
        })

        while self.running:
            self.mainServices.refresh()

            state = self.mainServices.eventsHandler.getState()

            # Clear the screen based on current screen state
            if state == "MainMenu":
                self.screen.fill((171, 186, 124))  # Menu background color
                for obj in self.mainMenuObjects:
                    obj.render()
            elif state == "Game":
                self.render_map()  # Render the game map when in the game screen

            elif state == "GameOver":
                self.render_game_over()  # Render the game over screen

            elif state == "GameWon":
                self.render_game_won()

            elif state == "Settings":
                self.render_setting()
            # Update the display
            pygame.display.flip()

        pygame.quit()
    
    
    def render_main_menu(self):
        self.screen.fill((171, 186, 124))
        
        for button in self.mainMenuObjects:
            button.render()
            

    def render_game_over(self):
        self.screen.fill((171, 186, 124))
        # sound_manager.playSound("lose")
        for object in self.gameOverObjects:
            object.render()

    def render_game_won(self):
        self.screen.fill((171, 186, 124))
        for object in self.gameWonObjects:
            object.render()

    def render_setting(self):
        self.screen.fill((171, 186, 124))
        for object in self.settingObjects:
            object.render()


if __name__ == "__main__":
    gui = GUI()
