import random


class Match:
    MATCH_SCORE = [(1, 0), (0.5, 0.5), (0, 1)]

    def __init__(self, player1, player2):
        self.match = (
            [player1, 0],
            [player2, 0]
        )
        """self.score1 = 0
        self.score2 = 0
"""
    def play(self):
        """simulates a match with random outcome"""
        match_score = random.choice(self.MATCH_SCORE)
        # Update scores
        self.match[0][1] += match_score[0]
        self.match[1][1] += match_score[1]

    def __repr__(self):
        return (f"{self.match[0][0].firstname} {self.match[0][0].lastname} "
                f"{self.match[0][1]} - "
                f"{self.match[1][1]} {self.match[1][0].firstname} "
                f"{self.match[1][0].lastname}")
