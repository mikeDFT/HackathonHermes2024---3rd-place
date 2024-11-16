from Code.Domain.game_data import GameSettings
from Code.Domain.player_instance import PlayerInstance
from Code.Domain.player_data import PlayerData

class PlayerProfile:
    def __init__(self, audio_level, name, unique_id, wins, losses):
        self.game_settings = GameSettings(audio_level)
        self.player = PlayerInstance(name, unique_id)
        self.player_data = PlayerData(wins, losses)

