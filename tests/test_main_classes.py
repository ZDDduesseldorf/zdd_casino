import pytest
from zdd_casino.main_classes import CardDeck


def test_card_deck():
    deck = CardDeck()
    assert len(deck.cards) == 52
    deck = CardDeck(num_copies=2)
    assert len(deck.cards) == 26

def test_draw_cards():
    deck = CardDeck()
    cards = deck.draw_cards(3)
    assert cards == ["A", "K", "Q"]
    # Test if cards were removed
    assert len(deck.cards) == 49

def test_card_deck_shuffle():
    deck = CardDeck(num_copies=10)
    before_shuffle = deck.cards.copy()
    deck.shuffle()
    after_shuffle = deck.cards.copy()
    assert before_shuffle != after_shuffle

def test_card_deck_empty():
    deck = CardDeck()
    deck.draw_cards(52)
    with pytest.raises(IndexError) as exc:
        deck.draw_cards(1)
    assert "pop from empty list" in str(exc.value)
