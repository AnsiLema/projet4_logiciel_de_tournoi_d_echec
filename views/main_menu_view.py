from views.view import View


class MainMenuView(View):
    """Main menu view"""

    def display_menu(self):
        """Display the main menu"""
        options = self.get_options()
        for key, value in options.items():
            print(f"{key}. {value}")

    def get_options(self):
        return {
        "1": "Créer un tournoi",
        "2": "Charger un tournoi",
        "3": "Quitter"
        }

