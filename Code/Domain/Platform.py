import pygame

class Platform:
    def __init__(self, screen, x, y, width=130, height=5, color=(252, 186, 3)):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width  # Allows different platform widths
        self.height = height  # Allows different platform heights
        self.color = color  # Customizable color

    def render(self):
        """Render the platform on the screen."""
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def is_colliding(self, player_rect):
        """
        Check if the platform is colliding with a given player's rect.
        The player_rect should be a pygame.Rect object.
        """
        platform_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        return platform_rect.colliderect(player_rect)
