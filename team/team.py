class Team():
    def __init__(self, name: str, elo_rating: float):
        self.name = name
        self.elo_rating = elo_rating
    def __str__(self):
        return f"Team: {self.name}, Elo Rating: {self.elo_rating}"