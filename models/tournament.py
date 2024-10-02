from models import player

class Tournament:
    def __init__(self, name, number_of_rounds, location, start_date, end_date, ):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.number_of_rounds = number_of_rounds
        self.current_round = 0
        self.rounds = []
        self.players = []

    def add_player(self, player):
        for player in self.players:
            self.players.append(player)

