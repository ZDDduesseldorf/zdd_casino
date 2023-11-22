from main_functions import count_cards


def test_count_cards_no_aces():
    assert count_cards(['2', '3', '4']) == 9

def test_count_cards_with_aces():
    assert count_cards(['A', '3', '4']) == 18
    assert count_cards(['A', 'A', '9']) == 21
    assert count_cards(['A', 'J']) == 21
    assert count_cards(['A', 'J', 'A']) == 12
