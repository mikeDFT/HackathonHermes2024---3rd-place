import random

import pygame
from Code.Services import SoundManager
sound_manager = SoundManager.SoundMan()
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
        self.on_ground = 0  # To check if player is standing on the ground
        self.life = 3
        self.pushStrength = 50
        self.pushedVelocity = 0
        self.jumping = 0


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


    def update(self, timeDelta, networkSendFunction):
        """Update the player's position and handle collisions with platforms."""
        self.oldX = self.x
        self.oldY = self.y
        
        self.x += self.velocity_x*(timeDelta/10) + self.pushedVelocity*(timeDelta/30)  # Update horizontal position
        self.y += self.velocity_y*(timeDelta/10)  # Update vertical position

        self.rect.x = self.x
        self.rect.y = self.y
        
        self.pushedVelocity = self.pushedVelocity - self.pushedVelocity*(timeDelta/100)
        
        self.velocity_y += self.gravity*(timeDelta/100)  # Apply gravity to vertical velocity
        self.velocity_y = min(self.terminalVelo, self.velocity_y)  # Limit falling speed

        if self.rect.y > 800:  # Assuming screen height is 800
            self.reset_position()  # Reset player position
            self.life -= 1  # Decrease life count
            self.on_ground = 0  # Player is no longer on the ground
            networkSendFunction("LIFE:" + str(self.life))  # Send life count to other player

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
        self.on_ground = 0  # Assume player is not on the ground
        for platform in platforms:
            if self.rect.colliderect(platform.rect):  # If player collides with platform
                # Simple collision resolution (stop the player from falling through)
                if pygame.time.get_ticks() - self.jumping > 400:
                    self.rect.bottom = platform.rect.top  # Place player on top of platform
                    self.on_ground = pygame.time.get_ticks()  # Player is on the ground
                    self.velocity_y = 0
            
            
    def handle_otherPlayer_collisions(self, otherPlayer):
        """Check for collisions with other player and stop falling."""
        if self.rect.colliderect(otherPlayer.rect):
            rndVelo = random.randint(self.pushStrength*90, self.pushStrength*110)/100
            sound_manager.playSound("enemyTakingDamage")
            if self.rect.x < otherPlayer.rect.x:
                self.pushedVelocity = -rndVelo
            else:
                self.pushedVelocity = rndVelo
            
            self.velocity_y = -rndVelo/4
            

    def getHealth(self):
        return self.life

    def reset_position(self):
        """Reset the player's position after falling."""
        sound_manager.playSound("takingDamage")
        self.x = 50  # Starting x position
        self.y = 150  # Starting y position
        self.rect.x = self.x
        self.rect.y = self.y