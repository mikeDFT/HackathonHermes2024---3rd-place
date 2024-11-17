import time

import pygame
from Code.Domain.Buttons import Button
from Code.Domain.Title import Title
from Code.Services import MainServices
from Code.Domain.Player import Player
from Code.Domain.InputBox import InputBox
from Code.Services import SoundManager
from Code.Services.ImageManager import ImageManager
from Code.Services.MapManager import MapManager

sound_manager = SoundManager.SoundMan()
image_manager = ImageManager()

class GUI:
    def __init__(self):
        pygame.init()
        self.lastTick = 0
        self.mainServices = MainServices.MainServices()
        self.mainServices.networking.generateRndMap = self.generateRndMap
        self.mainServices.networking.applyMapID = self.applyMapID
        self.running = True
        self.width = 1200
        self.height = 700
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = image_manager.getBackground()
        self.game_background = None
        self.platforms = None
        self.setup_screen()
        self.player = None
        self.otherPlayer = None



    def render_map(self):
        """
        Render the game map. This could be an image, objects, or any game elements.
        Here we render a simple placeholder for the map.
        """
        if self.mainServices.eventsHandler.getState() == "Game":
            self.screen.blit(self.game_background, (0, 0))  # background image

            if self.player.getHealth() == 0:
                self.mainServices.eventsHandler.changeState("GameOver")

            if self.otherPlayer.getHealth() == 0:
                self.mainServices.eventsHandler.changeState("GameWon")

            greenHeart = image_manager.getHeart("green")
            for i in range(self.player.getHealth()):
                self.screen.blit(greenHeart, (i * 60 + 50, 25))

            # Render platforms
            for platform in self.platforms:
                platform.render()

            currTick = pygame.time.get_ticks()
            deltaTime = currTick - self.lastTick
            self.lastTick = currTick

            # Handle and render the player
            self.player.update(deltaTime, self.mainServices.networking.send)  # Update the player's position
            self.player.handle_collisions(self.platforms)  # Check collisions with platforms
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
        self.screen.blit(self.background, (0, 0)) #background image

        play_button = Button("PLAY", self.screen, (76, 31, 122), self.width / 2 - 250 / 2, 325, 250, 100, "PLAY", font_size=40)
        settings_button = Button("SETTINGS", self.screen, (76, 31, 122), self.width / 2 - 250 / 2, 475, 250, 100, "SETTINGS",
                                 font_size=40)
        title = Title("TITLE", self.screen, "THE GAME", self.width / 2, 225)
        self.mainMenuObjects = [play_button, settings_button, title]


        self.screen.blit(self.background, (0, 0)) #background image
        title = Title("TITLE", self.screen, "GAME OVER", self.width / 2, 225)

        return_button = Button("RETURN", self.screen, (76, 31, 122), self.width / 2 - 250 / 2, 325, 250, 100, "RETURN",
                               font_size=40)
        self.gameOverObjects = [return_button, title]

        title = Title("TITLE", self.screen, "YOU WON", self.width / 2, 225)
        self.gameWonObjects = [return_button, title]

        title = Title("TITLE", self.screen, "SETTINGS", self.width / 2, 225)
        ip_input_field = InputBox(self.screen, self.width / 2 - 450/2, 325, 450, 50)

        self.settingObjects = [ip_input_field, return_button, title]

        self.connectEvents()


    def quit(self):
        self.running = False


    def handleButtonClickMenus(self, objects):
        mouse_pos = pygame.mouse.get_pos()
        for obj in objects:
            if isinstance(obj, Button) and obj.is_pressed(mouse_pos):
                sound_manager.playSound("buttonSelect")
                if obj.getId() == "PLAY":
                    if not self.platforms:
                        self.mainServices.networking.send("REQ|MAP:")
    
                        while not self.platforms:
                            time.sleep(0.05)
                    
                        
                    # Switch to the game screen when PLAY is clicked
                    self.mainServices.eventsHandler.changeState("Game")
                    # Initialize the player when entering the game
                    playerIcon = image_manager.getPlayerIcon("blue")
                    self.player = Player(self.screen, 50, 150, playerIcon, color=(50, 205, 50))  # You can adjust player start position
                    self.player.x, self.player.y = self.player.spawnPoint(self.platforms)

                    playerIcon = image_manager.getPlayerIcon("red")
                    self.otherPlayer = Player(self.screen, 300, 150, playerIcon)
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

    def applyMapID(self, map_id):
        map = MapManager(self.screen).getMapById(map_id)
        self.mainServices.networking.map = map
        self.game_background = image_manager.getGameBackground(self.width, self.height)
        self.platforms = map["MAP"]


    def generateRndMap(self):
        # Create platforms (map)
        map = MapManager(self.screen).getRandomMap()
        self.mainServices.networking.map = map
        self.game_background = image_manager.getGameBackground(self.width, self.height)
        self.platforms = map["MAP"]
        
        # Send map to the other user
        # print("MAP:" + str(map["ID"]))
        self.mainServices.networking.send("MAP:" + str(map["ID"]))

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
                self.screen.blit(self.background, (0, 0))  # background image
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
        self.screen.blit(self.background, (0, 0))  # background image

        for button in self.mainMenuObjects:
            button.render()
            

    def render_game_over(self):
        self.screen.blit(self.background, (0, 0))  # background image
        # sound_manager.playSound("lose")
        for object in self.gameOverObjects:
            object.render()

    def render_game_won(self):
        self.screen.blit(self.background, (0, 0))  # background image
        for object in self.gameWonObjects:
            object.render()

    def render_setting(self):
        self.screen.blit(self.background, (0, 0))  # background image
        for object in self.settingObjects:
            object.render()


if __name__ == "__main__":
    gui = GUI()
