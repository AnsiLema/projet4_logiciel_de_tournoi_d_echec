from models.match import Match
from models.tournament import Tournament
from models.player import Player
from faker import Faker
from models.round import Round

# Extract constants for tournament information
LOCALE = "fr_FR"
TOUR_LABEL = "--- Tour {} ---"
MATCHUP_DISPLAY = "{} ({}) vs {} ({})"
FINAL_RESULTS_LABEL = "--- Résultats finaux ---"
PLAYER_RESULTS_DISPLAY = "{} {} - Points: {}"
STANDINGS_LABEL = "--- Classement après le tour {} ---"
PLAYER_STANDING_DISPLAY = "{} {} - Points totaux: {}"

# Initializes the dummy data generator
fake = Faker(LOCALE)

def generate_players(num_players=8):
    generated_players = []
    for _ in range(num_players):
        player = Player(
            lastname=fake.last_name(),
            firstname=fake.first_name(),
            national_id=fake.bothify(text='??#####').upper(),
            birth_date=fake.date_of_birth(
                minimum_age=14,
                maximum_age=95).strftime('%d-%m-%Y')
        )
        generated_players.append(player)
    return generated_players

def generate_player_pairs(players):
    pairs = []
    players_with_opponents = []

    for player in players:
        player_data = {
            'name': player[0],
            'score': player[1],
            'opponents': player[2]
        }
        players_with_opponents.append(player_data)

    while len(players_with_opponents) > 1:
        players_with_opponents.sort(key=lambda x: x['score'], reverse=True)
        player1 = players_with_opponents[0]
        player2 = None

        for opponent in players_with_opponents[1:]:
            if opponent['name'] not in player1['opponents']:
                player2 = opponent
                break

        if player2 is None:
            raise ValueError("Impossible de trouver un adversaire pour le joueur {}".format(player1['name']))

        pairs.append((player1['name'], player2['name']))
        player1['opponents'].append(player2['name'])
        player2['opponents'].append(player1['name'])
        players_with_opponents.remove(player1)
        players_with_opponents.remove(player2)

    return pairs

def play_round(current_tournament, round_number):
    print(TOUR_LABEL.format(round_number))

    sorted_players = sort_players(current_tournament)
    pairs = generate_player_pairs(sorted_players)

    round = Round(f"round {round_number}")
    round.matches.extend(pairs)

    for match in round.matches:
        match.play()

    current_tournament.add_round(round)

    update_player_info(current_tournament, round)
    display_match_results(round)

def sort_players(current_tournament):
    return sorted(current_tournament.players, key=lambda player: player[1], reverse=True)

def create_matches(sorted_players):
    return [
        Match(sorted_players[i][0], sorted_players[i + 1][0])
        for i in range(0, len(sorted_players), 2)
    ]

def update_player_info(current_tournament, round):
    for match in round.matches:
        player1, score1 = match.match[0]
        player2, score2 = match.match[1]
        update_player_stats(current_tournament, player1, score1, player2)
        update_player_stats(current_tournament, player2, score2, player1)

def update_player_stats(current_tournament, player, score, opponent):
    for p in current_tournament.players:
        if p[0] == player:
            p[1] += score
            if opponent not in p[2]:
                p[2].append(opponent)

def display_match_results(round):
    for match in round.matches:
        print(
            f"Match terminé: {match.match[0][0]} vs {match.match[1][0]} "
            f"Score: {match.match[0][1]} - {match.match[1][1]}"
        )

def play_tournament(tournament, number_of_rounds=4):
    players = generate_players()
    for player in players:
        tournament.add_player(player)

    for round_number in range(1, number_of_rounds + 1):
        play_round(tournament, round_number)

    for player in tournament.players:
        print(player[0].lastname + " - " + str(player[1]))
        for opponent in player[2]:
            print(opponent.lastname)

def display_matchups(pairs):
    print("Matchups:")
    for player1, player2 in pairs:
        print(MATCHUP_DISPLAY.format(player1[0].first_name, sum(player1[1]),
                                     player2[0].first_name, sum(player2[1])))

def display_final_results(players):
    print(FINAL_RESULTS_LABEL)
    for player in sorted(players, key=lambda p: sum(p[1]), reverse=True):
        print(PLAYER_RESULTS_DISPLAY.format(player[0].first_name,
                                            player[0].last_name,
                                            sum(player[1])))