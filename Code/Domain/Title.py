from Code.Domain.Entity import Entity
import pygame

class Title(Entity):
    def __init__(self, id, screen, text, x, y, font_size=50, text_color=(0, 0, 0), font_name=None):
        """
        Initializes a title text object that can be rendered on the screen.

        :param screen: The Pygame surface where the title will be rendered.
        :param text: The title text to display.
        :param x: The x-coordinate of the top-left corner of the title.
        :param y: The y-coordinate of the top-left corner of the title.
        :param font_size: The font size for the title (default is 50).
        :param text_color: The color of the title text (default is black).
        :param font_name: Optional font name for the title (default is None, which uses the default font).
        """
        self.id = id
        self.screen = screen
        self.text = text
        self.x = x
        self.y = y
        self.font_size = font_size
        self.text_color = text_color
        self.font_name = font_name if font_name else None

        self.font = pygame.font.Font(self.font_name, self.font_size)  # Set font (default or custom)
        self.render()

    def render(self):
        """
        Renders the title text on the screen at the given position.
        """
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=(self.x, self.y))  # Centering the text at (x, y)
        self.screen.blit(text_surface, text_rect)  # Draw the text on the screen
