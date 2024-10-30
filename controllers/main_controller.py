from faker import Faker
from views.main_menu_view import MainMenuView
from views.tournament_view import TournamentView
from models.tournament import Tournament
from models.player import Player


class MainController:
    def __init__(self):
        self.main_menu_view = MainMenuView()
        self.tournament_view = TournamentView()
        self.current_tournament = None
        self.players = []

    def run(self):
        """Lance le menu principal de l'application."""
        while True:
            # Afficher le menu principal
            self.main_menu_view.display_menu()

            # Demander à l'utilisateur de faire un choix
            choice = input("Votre choix : ")

            if choice == "1":
                self.create_tournament()
            elif choice == "2":
                self.load_tournament()
            elif choice == "3":
                print("Au revoir !")
                break
            else:
                print("Choix invalide. Veuillez réessayer.")

    def create_tournament(self):
        """Créer un nouveau tournoi en utilisant TournamentView et générer des joueurs."""
        tournament_info = self.tournament_view.get_tournament_info()
        self.current_tournament = Tournament(
            name=tournament_info["name"],
            location=tournament_info["location"],
            start_date=tournament_info["start_date"],
            end_date=tournament_info["end_date"],
            description=tournament_info["description"],
            num_rounds=tournament_info["number_of_rounds"]
        )
        self.tournament_view.show_tournament(self.current_tournament)

        # Générer les joueurs
        num_players = int(input("Entrez le nombre de joueurs : "))
        self.players = self.generate_players(num_players)

        # Lancer le premier round
        self.start_round()

    # Initialiser Faker avec la locale française
    fake = Faker("fr_FR")

    def generate_players(self, num_players):
        """Génère une liste de joueurs fictifs."""
        faker = Faker()
        players = []
        for _ in range(num_players):
            name = faker.name()
            ranking = faker.random_int(min=1, max=100)
            player = Player(
                lastname=name.split(" ")[0],
                firstname=name.split(" ")[1],
                national_id=faker.bothify(text='??#####').upper(),
                birth_date=faker.date_of_birth(
                    minimum_age=14,
                    maximum_age=95).strftime('%d-%m-%Y')
                )
            players.append((player, ranking))
            print(f"Joueur généré : {name}, Classement : {ranking}")
        return players

    def start_round(self):
        """Démarre un round en appariant les joueurs et enregistrant les scores."""
        print("\n--- Premier Round ---")
        matches = self.create_matches()

        for match in matches:
            print(f"Match : {match[0].firstname} vs {match[1].firstname}")
            result = input("Résultat (1: Victoire Joueur 1, 2: Victoire Joueur 2, N: Nul) : ")
            if result == "1":
                match[0].score += 1
            elif result == "2":
                match[1].score += 1
            elif result.upper() == "N":
                match[0].score += 0.5
                match[1].score += 0.5
            else:
                print("Entrée invalide. Le match est déclaré nul par défaut.")
                match[0].score += 0.5
                match[1].score += 0.5

    def create_matches(self):
        """Crée les paires de matchs pour le round."""
        # Supposons qu'on utilise un simple appariement en prenant les joueurs par paires dans la liste
        matches = []
        for i in range(0, len(self.players), 2):
            if i + 1 < len(self.players):
                matches.append((self.players[i], self.players[i + 1]))
        return matches

    def load_tournament(self):
        """Fonctionnalité pour charger un tournoi existant."""
        print("Cette fonctionnalité n'est pas encore implémentée.")
