class UserLoader:
    def __init__(self, player_list):
        self.player_list = player_list

    def loadUser(self, user_obj):
        self.player_list.append(user_obj)
