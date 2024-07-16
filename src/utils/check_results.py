
# TODO:
# - This should be divided, if a player / dealer get a 21 they should win instantanesously and the next iteration of the while loop should be called, use continue ;)

def check_results(player_result, dealer_result):
    if player_result["addition"] > 21:
        print(f"Player loose ☹, the sum of the player's cards was {player_result['addition']}")
        return "loose"
    elif dealer_result["addition"] > 21:
        print(f"Player wins 😁!, the sum of the dealer's cards was {dealer_result['addition']}")
        return "win"
    elif player_result["addition"] == 21 and dealer_result["addition"] < 21:
        print("Player wins 😁!, the sum of the player's cards was exactly 21 💪!")
        return "win"
    elif dealer_result["addition"] == 21 and player_result["addition"] < 21:
        print("Player loose ☹, the sum of the dealer's cards was exactly 21 🦾")
        return "loose"
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

# instawin and instaloose