import pygame
import os

class SoundMan:
    def __init__(self, soundsPath: str = None):
        pygame.mixer.init()

        # Determine the path for sounds relative to this script's directory if not specified
        if soundsPath is None:
            soundsPath = os.path.join(os.path.dirname(__file__), "Sounds/")

        # Global volume scale for all sounds
        soundScale = 1

        self.musicName = "gameMusic"  # Updated for consistency

        # Sound configuration data
        self.soundsData = {

            "win": {"name": "Win.wav", "volume": 1 * soundScale},

            "lose": {"name": "DeathLose.wav", "volume": 0.1 * soundScale},

            "takingDamage": {"name": "TakingDamage.wav", "volume": 1 * soundScale},

            "jump": {"name": "Jump.wav", "volume": 100 * soundScale},

            "gameMusic": {"name": "GameplayMusic.mp3", "volume": 0.3 * soundScale},

            "enemyTakingDamage": {"name": "EnemyTakingDamage.wav", "volume": 1 * soundScale},

            "buttonSelect": {"name": "MenuSelect.wav", "volume": 1 * soundScale}

        }

        # Dictionary to store loaded sounds
        self.sounds = {}

        # Load sounds and set volume
        for name in self.soundsData:
            try:
                self.sounds[name] = pygame.mixer.Sound(soundsPath + self.soundsData[name]["name"])
                self.sounds[name].set_volume(self.soundsData[name]["volume"])
            except pygame.error as e:
                print(f"Error loading sound '{name}': {e}")

        # Initialize music
        self.initMusic()

    def initMusic(self):
        """Play background music in a loop"""
        try:
            self.playSound(self.musicName, -1)
        except SoundError as e:
            print(e)

    def playSound(self, name: str, loops: int = 0):
        """Play a specific sound effect or music by name."""
        if name not in self.sounds:
            raise SoundError(f"Sound '{name}' not found")
        pygame.mixer.Sound.play(self.sounds[name], loops=loops)

    def stopMusic(self):
        """Stop background music"""
        pygame.mixer.music.stop()

    def setVolume(self, name: str, volume: float):
        """Set volume for a specific sound"""
        if name in self.sounds:
            self.sounds[name].set_volume(volume)
        else:
            raise SoundError(f"Sound '{name}' not found")


class SoundError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return "[SoundError]: " + str(self.message)


