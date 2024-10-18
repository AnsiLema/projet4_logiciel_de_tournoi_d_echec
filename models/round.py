from models.match import Match
import datetime


class Round:
    def __init__(self, name):
        self.name = name
        self.matches = []
        self.start_date = datetime.datetime.now()
        self.end_date = None

    def finish_round(self):
        self.end_date = datetime.datetime.now()

    def add_match(self, player1, player2):
        match = Match(player1, player2)
        self.matches.append(match)

    def __repr__(self):
        return (f"{self.name} - "
                f"Début: {self.start_date}, "
                f"Fin: {self.end_date} - "
                f"Matches: {len(self.matches)}")
