import json

class DataExtractor:
    def __init__(self):
        self.file_path = "user_saved_data/user_data.json"

    def readData(self):
        # Open the file and read line by line
        with open(self.file_path, 'r') as file:
            for line in file:
                print(line.strip())  # Optional: Print or process each line

    def parsePlayerData(self):
        # Open and load the JSON file
        with open(self.file_path, 'r') as file:
            data = json.load(file)

        # Extract the first player's data (or None if no players exist)
        player_data = data.get("players", [{}])[0]

        # Extract necessary fields
        extracted_data = {
            "user_name": player_data.get("user_name", ""),
            "user_id": player_data.get("user_id", ""),
            "audio_level": player_data.get("audio_level", ""),
            "wins": player_data.get("wins", ""),
            "losses": player_data.get("losses", ""),
        }

        return extracted_data

