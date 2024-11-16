import json

class PlayerDataHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def add_player(self, user_name, user_id, audio_level, wins, losses, score):
        # Check if user_id already exists in the JSON file
        if self.is_user_id_in_use(user_id):
            print(f"Error: The user_id {user_id} is already in use.")
            return

        # Create a new player entry
        new_player = {
            "user_name": user_name,
            "user_id": user_id,
            "audio_level": audio_level,
            "wins": wins,
            "losses": losses,
            "score": score
        }

        # Read the existing data from the JSON file
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            # If the file does not exist, initialize an empty structure
            data = {"players": []}

        # Add the new player to the list of players
        data["players"].append(new_player)

        # Write the updated data back to the JSON file
        with open(self.file_path, 'w') as file:
            json.dump(data, file, indent=4)

        print(f"Player {user_name} added successfully!")

    def is_user_id_in_use(self, user_id):
        # Read the existing data from the JSON file
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            # If the file does not exist, initialize an empty structure
            data = {"players": []}

        # Check if the user_id already exists in the list of players
        for player in data["players"]:
            if player["user_id"] == user_id:
                return True  # user_id is already in use
        return False  # user_id is not in use
