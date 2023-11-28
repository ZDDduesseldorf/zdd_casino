from zdd_casino.main_classes import CardDeck


def count_cards(cards):
    """Counts the total value of the given cards in a blackjack game."""
    card_values = {str(n): n for n in range(2, 11)}
    card_values.update({'J': 10, 'Q': 10, 'K': 10, 'A': 11})

    total, aces = 0, 0
    for card in cards:
        total += card_values[card]
        if card == 'A':
            aces += 1

    while total > 21 and aces:
        total -= 10
        aces -= 1

    return total


def play_game_robot_version(robot_risk_thresholds):
    """Multiple AIs play a game of Blackjack.
    
    Parameters
    ----------
    robot_risk_thresholds:
        List of numbers, each represents one AI bot.
        The bot will continue to draw cards if the current points are below this value.
    """
    players = [{"name": f"Bot {i+1}", "cards": [], "score": 0, "threshold": thres} \
               for i, thres in enumerate(robot_risk_thresholds)]

    card_deck = CardDeck(num_copies=4)
    card_deck.shuffle()

    # Initial dealing of two cards
    for player in players:
        player["cards"] = card_deck.draw_cards(2)

    # Each player's turn
    for player in players:
        while True:
            player["score"] = count_cards(player["cards"])

            if player["score"] >= 21:
                break

            if player["score"] >= player["threshold"]:
                break

            player["cards"] += card_deck.draw_cards(1)

    # Determine winner
    try:
        winning_score = max(player["score"] for player in players if player["score"] <= 21)
        winners = [player["threshold"] for player in players if player["score"] == winning_score]
    except ValueError:
        return []

    # Final scores and winner announcement  
    if winners:
        return winners
    return []


def play_game():
    """A game of Blackjack with multiple players."""
    num_players = int(input("Enter the number of players: "))
    players = [{"name": f"Player {i+1}", "cards": [], "score": 0} for i in range(num_players)]

    card_deck = CardDeck(num_copies=4)
    card_deck.shuffle()

    # Initial dealing of two cards
    for player in players:
        player["cards"] = card_deck.draw_cards(2)

    # Each player's turn
    for player in players:
        while True:
            print(f"{player['name']}, your cards: {', '.join(player['cards'])}")
            player['score'] = count_cards(player['cards'])
            print(f"You have {player['score']} points.")

            if player['score'] >= 21:
                break

            answer = input("Do you want another card? (y/n): ")
            if answer.lower() == 'n':
                break

            player['cards'] += card_deck.draw_cards(1)

    # Determine winner
    try:
        winning_score = max(player['score'] for player in players if player['score'] <= 21)
        winners = [player['name'] for player in players if player['score'] == winning_score]
    except ValueError:
        winners = None

    # Final scores and winner announcement
    print("\nFinal Scores:")
    for player in players:
        print(f"{player['name']}: {player['score']} points")
    
    if winners:
        print(f"Winner(s): {', '.join(winners)}")
    else:
        print("No winners this round.")


if __name__ == "__main__":
    play_game()
