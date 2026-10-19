from team.team import Team

"""Update both teams in place using standard Elo with a K-factor of 32.

result must be "W", "L", or "D", relative to team1.
"""

def calculate_elo_rating(team1: Team, team2: Team, result: str) -> None:

    scores = {"W": 1.0, "L": 0.0, "D": 0.5}
    if result not in scores:
        raise ValueError('result must be "W", "L", or "D"')

    k_factor = 32
    expected_team1 = 1 / (1 + 10 ** ((team2.elo_rating - team1.elo_rating) / 400))
    adjustment = k_factor * (scores[result] - expected_team1)

    team1.elo_rating += adjustment
    team2.elo_rating -= adjustment


