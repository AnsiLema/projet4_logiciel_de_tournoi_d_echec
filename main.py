from controllers.tournament_controller import play_tournament
from models.tournament import Tournament

if __name__ == "__main__":
    number_of_rounds = 4
    tournament = Tournament('New Tournament', "Cognac", "12/05/2024", "14/05/2024", "-", number_of_rounds)
    play_tournament(tournament, number_of_rounds)
