import pytest
from zdd_casino.main_functions import count_cards
from zdd_casino.main_functions import play_game, play_game_robot_version
from zdd_casino.main_classes import CardDeck
from io import StringIO


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


def test_single_player_blackjack(monkeypatch):
    """Simulate a single player getting Blackjack."""
    def mock_user_input():
        # This simulates the user input
        def fake_input(prompt):
            if "number of players" in prompt:
                return "1"
            return "n"
        return fake_input
    
    def mock_draw_cards(self, n):
        # This simulates the drawing of cards.
        return ["A", "10"]

    # Mock single player game
    monkeypatch.setattr('builtins.input', mock_user_input())

    # Mock CardDeck to deal a Blackjack hand
    monkeypatch.setattr(CardDeck, 'draw_cards', mock_draw_cards)

    # Capture output
    output = StringIO()
    monkeypatch.setattr('sys.stdout', output)

    play_game()

    assert "Player 1, your cards: A, 10" in output.getvalue()
    assert "You have 21 points." in output.getvalue()
    assert "Winner(s): Player 1" in output.getvalue()


def test_play_robot_game():
    thresholds = [25, 10, 25]
    results = []
    for _ in range(20):
        results.extend(play_game_robot_version(thresholds))
    results.sort()
    assert results[10] == "Bot 2", "Median should be Bot 2."
