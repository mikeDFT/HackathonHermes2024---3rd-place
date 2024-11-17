import pygame


class Platform:
    def __init__(self, screen, icon, x, y, width=130, height=5, color=(252, 186, 3), font_color=(0, 0, 0)):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width  # Allows different platform widths
        self.height = height  # Allows different platform heights
        self.color = color  # Customizable platform color
        self.font_color = font_color  # Color for the coordinates text
        self.font = pygame.font.Font(None, 24)  # Default font and size
        self.icon = pygame.transform.scale(icon, (width, height))

    def render(self):
        """Render the platform on the screen."""
        # Draw the platform rectangle
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.screen.blit(self.icon, (self.rect.x, self.rect.y))

        #pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))

        # Render the coordinates as text
        #coord_text = f"({self.x}, {self.y})"
        #text_surface = self.font.render(coord_text, True, self.font_color)

        # Calculate text position to center it on the platform
        # text_x = self.x + (self.width - text_surface.get_width()) / 2
        # text_y = self.y + (self.height - text_surface.get_height()) / 2
        #
        # # Draw the text on the screen
        # self.screen.blit(text_surface, (text_x, text_y))

    def is_colliding(self, player_rect):
        """
        Check if the platform is colliding with a given player's rect.
        The player_rect should be a pygame.Rect object.
        """
        platform_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        return platform_rect.colliderect(player_rect)
