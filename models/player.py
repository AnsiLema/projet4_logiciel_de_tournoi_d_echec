from faker import Faker

fake = Faker("fr_FR")

class Player:
    def __init__(self, lastname, firstname, national_id, date_of_birth):
        self.lastname = lastname
        self.firstname = firstname
        self.national_id = national_id
        self.date_of_birth = date_of_birth
        self.points = 0

    def __str__(self):
        return (f"{self.firstname} {self.lastname}, ID: {self.national_id}, "
                f"Date Of Birth: {self.date_of_birth}, Points: {self.points})")

# Création des joueurs en utilisant la classe Player
players = []
for _ in range(8):  # Crée 8 joueurs
    player = Player(
        lastname=fake.last_name(),
        firstname=fake.first_name(),
        national_id=fake.bothify(text='??#####').upper(),
        date_of_birth=fake.date_of_birth(minimum_age=14, maximum_age=80).strftime('%d-%m-%Y')
    )
    players.append(player)

# Affichage des joueurs créés
for player in players:
    print(player)

