from views.view import View


class TournamentView(View):
    def __init__(self):
        super().__init__()

    def display_tournament_info(self, tournament):
        self.display_tournament_name(tournament.name)
        self.display_tournament_players(tournament.players)
        self.display_tournament_rounds(tournament.rounds)