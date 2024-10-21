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

# Initializes the dummy data generator
fake = Faker(LOCALE)

# Create the tournament
tournament = Tournament(
    name=fake.name(),
    location=fake.city(),
    start_date=fake.date(),
    end_date=fake.date()
)


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
        generated_players.append([player])  # [Player, points, opponents_list]
    return generated_players


def play_round(current_tournament, round_number):
    """Play a full round with the pairs of players."""
    print(TOUR_LABEL.format(round_number))
    sorted_players = sorted(current_tournament.players, key=lambda player: player[1], reverse=True)
    matches = []
    match1 = Match(sorted_players[0][0], sorted_players[1][0])
    match2 = Match(sorted_players[2][0], sorted_players[3][0])
    match3 = Match(sorted_players[4][0], sorted_players[5][0])
    match4 = Match(sorted_players[6][0], sorted_players[7][0])
    round = Round("round " + str(round_number))
    round.matches.append(match1)
    round.matches.append(match2)
    round.matches.append(match3)
    round.matches.append(match4)

    match1.play()
    match2.play()
    match3.play()
    match4.play()

    current_tournament.add_round(round)
    for match in round.matches:
        for player in current_tournament.players:
            if player[0] == match.match[0][0]:
                player[1] += match.match[0][1]
            if player[0] == match.match[1][0]:
                player[1] += match.match[1][1]

        print(
            f"Match terminé: {match.match[0][0]}"
            f"  vs  "
            f"{match.match[1][0]}"
            f"Score: {match.match[0][1]} - {match.match[1][1]}"
        )

    return


def play_tournament(tournament, number_of_rounds=4):
    """Simulates a tournament with a given number of rounds."""
    players = generate_players()
    for player in players:
        tournament.add_player(player)

    # Display players
    for player in players:
        print(player[0])

    players = tournament.players

    for round_number in range(1, number_of_rounds + 1):
        play_round(tournament, round_number)


def display_matchups(pairs):
    """Shows player matchups for a round."""
    print("Matchups:")
    for player1, player2 in pairs:
        print(MATCHUP_DISPLAY.format(player1[0].first_name, sum(player1[1]), player2[0].first_name, sum(player2[1])))


def display_final_results(players):
    """Shows the final results of the tournament."""
    print(FINAL_RESULTS_LABEL)
    for player in sorted(players, key=lambda p: sum(p[1]), reverse=True):
        print(PLAYER_RESULTS_DISPLAY.format(player[0].first_name,
                                            player[0].last_name,
                                            sum(player[1])))


def generate_player_pairs(players):
    """Generates player pairs for a round based on points."""
    sorted_players = sorted(players, key=lambda player: player[1], reverse=True)
    print(sorted_players[0])
    pairs = []
    used_players = set()

    for i, player1 in enumerate(sorted_players):
        if player1 in used_players:
            continue
        for player2 in sorted_players[i + 1:]:
            if player2 not in used_players and player2[0] not in player1[2]:
                pairs.append((player1, player2))
                used_players.add(player1)
                used_players.add(player2)
                player1[2].append(player2[0])
                player2[2].append(player1[0])
                break

    return pairs
