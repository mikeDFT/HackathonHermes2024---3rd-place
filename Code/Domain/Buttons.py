import pygame
from Code.Domain.Entity import Entity

import pygame
from Code.Domain.Entity import Entity

class Button(Entity):
    def __init__(self, id, screen, color, x, y, length, width, text=None, text_color=(0, 0, 0), font_size=20, shadow_opacity=128):
        """
        Initialize a button with text centered on it and a semi-transparent shadow.

        :param screen: The Pygame surface where the button will be rendered.
        :param color: The button's background color (RGB tuple).
        :param x: The x-coordinate of the top-left corner of the button.
        :param y: The y-coordinate of the top-left corner of the button.
        :param length: The horizontal length of the button.
        :param width: The vertical width of the button.
        :param text: The text to display on the button (default: None).
        :param text_color: The color of the text (default: black).
        :param font_size: The font size for the text (default: 20).
        :param shadow_opacity: Opacity of the shadow (0 to 255, 255 being fully opaque).
        """
        self.id = id
        self.color = color
        self.length = length
        self.width = width
        self.screen = screen
        self.x = x
        self.y = y
        self.text = text
        self.text_color = text_color
        self.font_size = font_size
        self.shadow_opacity = shadow_opacity

        self.font = pygame.font.Font('Code/Domain/RetroBlendy-LVOm3.otf', self.font_size)  # Replace with your retro font path
        self.render()

    def render(self):
        """
        Draw the button with a semi-transparent shadow and centered text.
        """
        # Create a shadow with transparency (alpha channel)
        shadow_color = (self.color[0], self.color[1], self.color[2], self.shadow_opacity)
        shadow_surface = pygame.Surface((self.length, self.width), pygame.SRCALPHA)
        shadow_surface.fill(shadow_color)

        # Draw the shadow rectangle slightly offset
        self.screen.blit(shadow_surface, (self.x + 5, self.y + 5))  # Offset by (5, 5)

        # Draw the button rectangle
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.length, self.width))
        self.rect = pygame.rect.Rect(self.x, self.y, self.length, self.width)
        # If text is provided, render and center it
        if self.text:
            text_surface = self.font.render(self.text, True, self.text_color)
            text_rect = text_surface.get_rect(center=(self.x + self.length // 2, self.y + self.width // 2))
            self.screen.blit(text_surface, text_rect)


    def is_pressed(self, mouse_pos):
        """Check if the button is pressed by the mouse."""
        return self.rect.collidepoint(mouse_pos)