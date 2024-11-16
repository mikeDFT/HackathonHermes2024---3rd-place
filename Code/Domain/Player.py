import pygame

class Player:
    def __init__(self, screen, x, y, width=50, height=50, color=(255, 0, 0)):
        """
        Initialize the player.

        :param screen: The Pygame surface where the player will be rendered.
        :param x: The x-coordinate of the player.
        :param y: The y-coordinate of the player.
        :param width: The width of the player (default: 50).
        :param height: The height of the player (default: 50).
        :param color: The color of the player (default: red).
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.oldX = x
        self.oldY = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)  # Use rect for collision detection
        self.velocity_x = 0  # Horizontal velocity (left/right movement)
        self.velocity_y = 0  # Vertical velocity (up/down movement)
        self.speed = 5  # Speed of player movement
        self.gravity = 5  # Gravity constant for falling
        self.terminalVelo = 10  # Terminal velocity for falling
        self.x_drag = 1  # like gravity but on the X axis
        self.jump_strength = -15  # Jump strength (negative to go up)
        self.on_ground = False  # To check if player is standing on the ground
        self.on_ceiling = False  # To check if player is standing on the ceiling
        self.life = 3


    def render(self):
        """Draw the player on the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)


    def apply_gravity(self):
        """Apply gravity to the player, causing them to fall when not on the ground."""
        if not self.on_ground:
            self.velocity_y += self.gravity  # Apply gravity to vertical velocity


    # def move(self, keys):
    #     """Move the player based on keyboard input (left, right, jumping)."""
    #     if keys[pygame.K_LEFT]:
    #         self.velocity_x = -self.speed  # Move left
    #     elif keys[pygame.K_RIGHT]:
    #         self.velocity_x = self.speed  # Move right
    #     else:
    #         self.velocity_x = 0  # Stop horizontal movement
    #
    #     if keys[pygame.K_SPACE] and self.on_ground:
    #         self.velocity_y = self.jump_strength  # Jump when space is pressed and player is on the ground


    def update(self, timeDelta, networkSend):
        """Update the player's position and handle collisions with platforms."""
        self.oldX = self.x
        self.oldY = self.y
        
        self.x += self.velocity_x*(timeDelta/10)  # Update horizontal position
        self.y += self.velocity_y*(timeDelta/10)  # Update vertical position

        self.rect.x = self.x
        self.rect.y = self.y
        
        networkSend(self.x + "," + self.y)

        self.velocity_y += self.gravity*(timeDelta/100)  # Apply gravity to vertical velocity
        self.velocity_y = min(self.terminalVelo, self.velocity_y)  # Limit falling speed

        if self.rect.y > 800:  # Assuming screen height is 800
            self.reset_position()  # Reset player position
            self.life -= 1  # Decrease life count
            self.on_ground = False  # Player is no longer on the ground

        # if self.velocity_y > 0:
        #     self.velocity_y = min(0, self.velocity_y - self.gravity*(timeDelta/100))
        # if self.velocity_y < 0:
        #     self.velocity_y = max(0, self.velocity_y + self.gravity*(timeDelta/100))
        #
        # if self.velocity_x > 0:
        #     self.velocity_x = max(0, self.velocity_x - self.x_drag*(timeDelta/100))
        # if self.velocity_x < 0:
        #     self.velocity_x = min(0, self.velocity_x + self.x_drag*(timeDelta/100))
        

    def handle_collisions(self, platforms):
        """Check for collisions with platforms and stop falling."""
        self.on_ground = False  # Assume player is not on the ground
        self.on_ceiling = False  # Assume player is not on the ceiling
        
        for platform in platforms:
            if self.rect.colliderect(platform.rect):  # If player collides with platform
                # Simple collision resolution (stop the player from falling through)
                if self.oldY < platform.rect.y:
                    self.rect.bottom = platform.rect.top+1  # Place player on top of platform
                    self.on_ground = True  # Player is on the ground
                    self.velocity_y = 0
                elif self.oldY > platform.rect.y:
                    self.rect.top = platform.rect.bottom+2  # Place player below platform
                    self.velocity_y = -self.jump_strength/2
                    
                # if self.oldX < platform.rect.x:
                #     self.rect.right = platform.rect.left+1
                # elif self.oldX > platform.rect.x:
                #     self.rect.left = platform.rect.right-1
            


    def getHealth(self):
        return self.life

    def reset_position(self):
        """Reset the player's position after falling."""
        self.x = 50  # Starting x position
        self.y = 150  # Starting y position
        self.rect.x = self.x
        self.rect.y = self.y