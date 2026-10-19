from data_utils import fetch_data, process_game
import os

if __name__ == "__main__":
    api_key = os.getenv("API_KEY")
    data = fetch_data.fetch_data("https://api.collegefootballdata.com/games?year=2026&week=7", api_key=api_key)
    if data is not None:
        process_game.process_games(data)
