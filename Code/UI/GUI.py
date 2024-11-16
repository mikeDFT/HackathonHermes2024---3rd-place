import pygame
from Code.Domain.Buttons import Button
from Code.Domain.Title import Title
from Code.Domain.Platform import Platform


class GUI:
    def __init__(self):
        pygame.init()
        self.running = True
        self.current_screen = "menu"  # Start in the menu screen
        self.setup_screen()
        self.player = pygame.Rect(200, 400, 50, 50)  # Starting position of the player
        self.player_velocity = 0  # Vertical velocity for jumping
        self.gravity = 1  # Simple gravity effect
        self.on_ground = False  # Check if player is on the ground

    def render_map(self):
        """
        Render the game map. This could be an image, objects, or any game elements.
        Here we render a simple placeholder for the map.
        """
        if self.current_screen == "game":
            self.screen.fill((135, 206, 235))  # Sky-blue background for the game map

            # Create platforms
            platforms = [
                Platform(self.screen, 100, 500),
                Platform(self.screen, 100, 400),
                Platform(self.screen, 100, 300)
            ]

            # Render platforms
            for platform in platforms:
                platform.render()



    def setup_screen(self):
        """
        Setup the screen with the menu, including buttons and title.
        """
        self.screen = pygame.display.set_mode((500, 800))
        self.screen.fill((171, 186, 124))  # Background color for the menu
        play_button = Button("PLAY", self.screen, (61, 83, 0), 500 / 2 - 250 / 2, 300, 250, 100, "PLAY", font_size=40)
        settings_button = Button("SETTINGS", self.screen, (61, 83, 0), 500 / 2 - 250 / 2, 450, 250, 100, "SETTINGS",
                                 font_size=40)
        title = Title("TITLE", self.screen, "Jocul Nostru", 245, 100)
        self.objects = [play_button, settings_button, title]
        self.game_loop(self.objects)

    def game_loop(self, objects):
        """
        The main game loop where events are handled and the screen is updated.
        """
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    for obj in objects:
                        if isinstance(obj, Button) and obj.is_pressed(mouse_pos):
                            if obj.getId() == "PLAY":
                                # Switch to the game screen when PLAY is clicked
                                self.current_screen = "game"
                            elif obj.getId() == "SETTINGS":
                                # Add settings functionality if needed
                                print("Settings button clicked!")

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
