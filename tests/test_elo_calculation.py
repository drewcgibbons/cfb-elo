from unittest.mock import Mock

import pytest

from elo_utils.elo_calculation import calculate_elo_rating
from team.team import Team


@pytest.mark.parametrize(
    "rating1, rating2, result, expected1, expected2",
    [
        (1500, 1500, "W", 1516, 1484),
        (1500, 1500, "L", 1484, 1516),
        (1500, 1500, "D", 1500, 1500),
        (1900, 1500, "W", 1902.9090909091, 1497.0909090909),
        (1900, 1500, "L", 1870.9090909091, 1529.0909090909),
        (1900, 1500, "D", 1886.9090909091, 1513.0909090909),
    ],
)
def test_calculate_elo_rating_updates_both_teams(
    rating1, rating2, result, expected1, expected2
):
    team1 = Mock(spec=Team, elo_rating=rating1)
    team2 = Mock(spec=Team, elo_rating=rating2)

    calculate_elo_rating(team1, team2, result)

    assert team1.elo_rating == pytest.approx(expected1)
    assert team2.elo_rating == pytest.approx(expected2)
    assert team1.elo_rating + team2.elo_rating == pytest.approx(rating1 + rating2)


def test_calculate_elo_rating_rejects_invalid_result_without_changing_ratings():
    team1 = Mock(spec=Team, elo_rating=1500)
    team2 = Mock(spec=Team, elo_rating=1600)

    with pytest.raises(ValueError, match="result must be"):
        calculate_elo_rating(team1, team2, "invalid")

    assert team1.elo_rating == 1500
    assert team2.elo_rating == 1600
