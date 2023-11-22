import random


class CardDeck:
    def __init__(self, num_copies = 4):
        self.cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"] * num_copies

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_cards(self, num_cards):
        cards = []
        for _ in range(num_cards):
            cards.append(self.cards.pop())
        return cards
