from views.view import View


class PlayerView(View):
    def get_new_player_info(self):
        lastname = self.get_input("Nom: ")
        firstname = self.get_input("Prénom: ")
        national_id = self.get_input("Nationale ID: ")
        birth_date = self.get_input("Date de naissance (jj/mm/aaaa): ")
        return {
            "lastname": lastname,
            "firstname": firstname,
            "national_id": national_id,
            "birth_date": birth_date
        }

    def show_player_added(self, player):
        self.display_message(f"Joueur {player} ajouté avec succes")

    def search_players(self):
        return self.get_input("Entrez les premières lettres du nom du joueur: ")

