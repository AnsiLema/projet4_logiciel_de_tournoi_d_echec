class View:
    def __init__(self):
        pass

    def display_tournament_name(self, tournament_name):
        print(f"Nom du tournoi : {tournament_name}")

    def display_player_info(self, player):
        print(f"Nom : {player.lastname} {player.firstname}")
        print(f"Identifiant national : {player.national_id}")
        print(f"Date de naissance : {player.birth_date}")

    def display_tournament_players(self, players):
        print("Liste des joueurs du tournoi :")
        for player in players:
            self.display_player_info(player)
            print()

    def display_tournament_rounds(self, rounds):
        print("Liste des tours du tournoi :")
        for round in rounds:
            print(f"Tour {round}")

    def display_menu(self):
        print("Menu :")
        print("1. Créer un tournoi")
        print("2. Lancer un tournoi")
        print("3. Quitter")

    def get_user_input(self, prompt):
        return input(prompt)