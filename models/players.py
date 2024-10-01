
from faker import Faker

fake = Faker("fr_FR")

# Générer des données fictives pour les joueurs
players = []
for _ in range(8):  # Génère 4 joueurs, vous pouvez changer ce nombre
    player = {
        "lastname": fake.last_name(),
        "firstname": fake.first_name(),
        "national_id": fake.bothify(text='??#####').upper(),
        "date_of_birth": fake.date_of_birth(minimum_age=14, maximum_age=95).strftime('%d-%m-%Y')
    }
    players.append(player)

# Afficher les joueurs générés
for player in players:
    print(player)


class Player:
    def __init__(self, lastname, firstname, national_id, date_of_birth):
        self.lastname = lastname
        self.firstname = firstname
        self.national_id = national_id
        self.date_of_birth = date_of_birth
        self.points = 0

    def __repr__(self):
        return f" {self.lastname} {self.firstname} (Points: {self.points})"

