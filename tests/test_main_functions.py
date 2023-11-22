import pytest
from zdd_casino.main_functions import count_cards


def test_count_cards_no_aces():
    assert count_cards(['2', '3', '4']) == 9

@pytest.mark.parametrize("cards, points",
                         [(['A', '3', '4'], 18),
                          (['A', 'A', '9'], 21),
                          (['A', 'J'], 21),
                          (['A', 'J', 'A'], 12),
                          (["A", "A", "A", "A"], 14),
                          ])
def test_count_cards_with_aces(cards, points):
    assert count_cards(cards) == points
