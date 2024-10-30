from controllers.tournament_controller import play_tournament
from controllers.main_controller import MainController
if __name__ == "__main__":
    # Créer une instance du contrôleur principal
    main_controller = MainController()

    # Lancer le menu principal de l'application
    main_controller.run()

    # Lancer le tournoi
    if main_controller.current_tournament:
        play_tournament(main_controller.current_tournament, main_controller.current_tournament.number_of_rounds)
