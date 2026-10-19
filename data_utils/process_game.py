import json
import os
import elo_utils.elo_calculation as elo_calculation
import team.team as t
import data_utils.fetch_data as fetch_data

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
    print(f"{homeTeam.name}: {home_points}, {awayTeam.name}: {away_points}")
    print(awayTeam)
    print("-" * 40)  # Separator for clarity

def process_games(data: list[dict]) -> None:
    games = fbs_filter(data)
    for game_data in games:
        process_game(game_data)

def fbs_filter(games: list[dict]) -> list:
    fbs_teams = fetch_data.fetch_data("https://api.collegefootballdata.com/teams/fbs", api_key=os.getenv("API_KEY"))
    fbs_teams = set(team["school"] for team in fbs_teams)
    
    fbs_games = []
    for game in games:
        if game.get("homeTeam") in fbs_teams or game.get("awayTeam") in fbs_teams:
            fbs_games.append(game)
    return fbs_games