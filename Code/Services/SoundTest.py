import pygame
from SoundManager import SoundManager

# Initialize Pygame
pygame.init()

# Create a window (necessary for some Pygame sound functions)
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("SoundManager Test")

# Initialize the SoundManager
sound_manager = SoundManager()

# Running flag
running = True

# Instructions for testing
print("Press '1' for win sound, '2' for lose sound, '3' for jump sound, 'M' to stop music, and 'Q' to quit.")

# Main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                sound_manager.playSound("win")

            elif event.key == pygame.K_2:
                sound_manager.playSound("lose")

            elif event.key == pygame.K_3:
                sound_manager.playSound("jump")

            elif event.key == pygame.K_m:
                sound_manager.stopMusic()

            elif event.key == pygame.K_q:
                running = False

# Quit Pygame
pygame.quit()
