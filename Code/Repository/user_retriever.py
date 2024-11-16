from repository.data_extractor import DataExtractor
from domain.player_profile import PlayerProfile

class UserRetriever:
    def __init__(self):
        self.data_extractor = DataExtractor()  # Assuming DataExtractor is properly implemented

    def loadUserData(self):
        # Extract the user data using the data extractor
        user_data = self.data_extractor.parsePlayerData()  # Assuming parsePlayerData() returns a dictionary

        # Unpack user data into variables
        audio_level = user_data.get("audio_level", "")
        user_name = user_data.get("user_name", "")
        user_id = user_data.get("user_id", "")
        wins = user_data.get("wins", 0)
        losses = user_data.get("losses", 0)

        # Create and return a PlayerProfile instance
        user_to_insert = PlayerProfile(
            audio_level=audio_level,
            name=user_name,
            unique_id=user_id,
            wins=wins,
            losses=losses,
        )

        return user_to_insert
