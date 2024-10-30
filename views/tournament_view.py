from views.view import View


class TournamentView(View):
    def get_tournament_info(self):
        name = self.get_input("Nom du tournoi: ")
        location = self.get_input("Lieu du tournoi: ")
        start_date = self.get_input("Date de commencement du tournoi (jj/mm/aaaa): ")
        description = self.get_input("Description du tournoi: ")
        number_of_rounds = self.get_input("Nombre de rounds: ")
        return {
            "name": name,
            "location": location,
            "start_date": start_date,
            "end_date": None,
            "description": description,
            "number_of_rounds": int(number_of_rounds)
        }

    def show_tournament(self, tournament):
        self.display_message(f"tournoi crée avec succes: {tournament.name}")
