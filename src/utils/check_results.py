def is_blackjack(player_cards, dealer_cards):
    face_cards = {10, "J", "Q", "K"}

    player_blackjack = (player_cards[0][0] == "A" and player_cards[1][0] in face_cards) or (
            player_cards[1][0] == "A" and player_cards[0][0] in face_cards)
    dealer_blackjack = (dealer_cards[0][0] == "A" and dealer_cards[1][0] in face_cards) or (
            dealer_cards[1][0] == "A" and dealer_cards[0][0] in face_cards)

    if player_blackjack and dealer_blackjack:
        print(f"Player Blackjack and Dealer Blackjack! 😱")
        return "tie"
    elif player_blackjack:
        print(f"Player Blackjack! 🎯")
        return "win"
    elif dealer_blackjack:
        print(f"Dealer Blackjack! 🎰")
        return "loose"
    else:
        return "continue playing"


def check_player_results(player_result):
    if player_result["addition"] == 21:
        print("Player wins 😁!, the sum of the player's cards was exactly 21 💪!")
        return "win"
    elif player_result["addition"] > 21:
        print(f"Player loose ☹, the sum of the player's cards was {player_result['addition']}")
        return "loose"
    else:
        return "continue playing"


def check_general_results(player_result, dealer_result):
    if dealer_result["addition"] > 21:
        print(f"Player wins 😁!, the sum of the dealer's cards was {dealer_result['addition']}")
        return "win"
    elif player_result["addition"] == dealer_result["addition"]:
        if player_result["cards"] < dealer_result["cards"]:
            print(f"Player wins 😁!, although both had {player_result['addition']}, player had less cards")
            return "win"
        elif player_result["cards"] > dealer_result["cards"]:
            print(f"Player loose ☹, although both had {player_result['addition']}, dealer had less cards")
            return "loose"
        else:
            print(f"The round ended with a tie 😱 with {player_result['addition']}")
            return "tie"
    elif player_result["addition"] > dealer_result["addition"]:
        print(f"Player wins 😁!, the sum of the player's cards was {player_result['addition']}")
        return "win"
    elif player_result["addition"] < dealer_result["addition"]:
        print(f"Player loose ☹, the sum of the dealer's cards was {dealer_result['addition']}")
        return "loose"
