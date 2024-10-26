from views.view import View


class PlayerView(View):
    def __init__(self):
        super().__init__()

    def display_player_score(self, player):
        print(f"Score de {player.lastname} {player.firstname} : {player.score}")