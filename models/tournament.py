class Tournament:
    def __init__(self, name, location,
                 start_date, end_date,
                 description="", num_rounds=4):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.num_rounds = num_rounds
        self.current_round = 1
        self.rounds = []
        self.players = []

    def add_player(self, player):
        """Adds player to the tournament."""
        self.players.append([player, 0, []])
        # Initializes score to 0 and empty opponents list

    def add_round(self, round):
        """Adds a round to the tournament"""
        self.rounds.append(round)

    def __repr__(self):
        return (f"Tournament(name={self.name},"
                f" location={self.location}, "
                f"start_date={self.start_date}, end_date={self.end_date})")
