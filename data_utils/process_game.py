import json
import elo_utils.elo_calculation as elo_calculation
from team import team
import team.team as t

"""
Processes the game data and prints the results.

Args:
    data (str): The game data in string format.
"""
def process_game(game_data: dict) -> None:
    home_team = game_data["homeTeam"]
    home_points  = game_data["homePoints"]
    away_team = game_data["awayTeam"]
    away_points = game_data["awayPoints"]


    homeTeam = t.Team(home_team, 1200)  # Assuming a default Elo rating of 1200
    awayTeam = t.Team(away_team, 1200)  # Assuming a default Elo rating of 1200

    if home_points > away_points:
        result = "W"
    elif home_points < away_points:
        result = "L"
    else:
        result = "D"

    elo_calculation.calculate_elo_rating(homeTeam, awayTeam, result)

    print(homeTeam)
    print(awayTeam)

def process_games(data: str) -> None:
    games = json.loads(data)
    for game_data in games:
        process_game(game_data)
