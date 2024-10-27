from models.match import Match
from models.tournament import Tournament
from models.player import Player
from models.round import Round
from views.player_view import PlayerView
from views.tournament_view import TournamentView
from views.view import View

# Extract constants for tournament information
LOCALE = "fr_FR"
TOUR_LABEL = "--- Tour {} ---"
MATCHUP_DISPLAY = "{} ({}) vs {} ({})"
FINAL_RESULTS_LABEL = "--- Résultats finaux ---"
PLAYER_RESULTS_DISPLAY = "{} {} - Points: {}"
STANDINGS_LABEL = "--- Classement après le tour {} ---"
PLAYER_STANDING_DISPLAY = "{} {} - Points totaux: {}"


def play_round(current_tournament, round_number):
    """Play a full round with the pairs of players."""
    print(TOUR_LABEL.format(round_number))

    # Générer les paires dynamiquement en utilisant les points et les adversaires déjà rencontrés
    pairs = generate_player_pairs(current_tournament.players)
    matches = []

    round = Round("round " + str(round_number))

    for player1, player2 in pairs:
        match = Match(player1[0], player2[0])
        match.play()
        matches.append(match)
        round.matches.append(match)

    current_tournament.add_round(round)

    # Mettre à jour les scores des joueurs après les matchs
    for match in round.matches:
        for player in current_tournament.players:
            if player[0] == match.match[0][0]:
                player[1] += match.match[0][1]
            if player[0] == match.match[1][0]:
                player[1] += match.match[1][1]

        print(
            f"Match terminé: {match.match[0][0].firstname} vs {match.match[1][0].firstname} "
            f"Score: {match.match[0][1]} - {match.match[1][1]}"
        )


def play_tournament(tournament, number_of_rounds=4):
    """Simulates a tournament with a given number of rounds."""

    print(f"Tournament: {tournament.name}")
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
    """Generates player pairs for a round based on points, ensuring no repeat matchups."""
    # Trier les joueurs par leurs points (le score est le deuxième élément de la liste)
    sorted_players = sorted(players, key=lambda player: player[1], reverse=True)
    pairs = []
    used_players = set()

    for i, player1 in enumerate(sorted_players):
        if player1 in used_players:
            continue

        # Trouver un adversaire approprié qui n'a pas déjà joué contre player1
        for player2 in sorted_players[i + 1:]:
            if player2 not in used_players and player2[0] not in player1[2]:
                # Créer la paire
                pairs.append((player1, player2))
                # Ajouter les joueurs utilisés à la liste
                used_players.add(player1)
                used_players.add(player2)
                # Mettre à jour la liste des adversaires rencontrés pour chaque joueur
                player1[2].append(player2[0])
                player2[2].append(player1[0])
                break

    return pairs
