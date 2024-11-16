class MainData:
    def __init__(self, user_list):
        self.contain_user_profiles = user_list

    def check_if_unique_id(self, user_id):
        for player in self.contain_user_profiles:
            if player["user_id"] == user_id:
                return player
        return None