from src.utils import (bet, player_turn, dealer_turn, distribute_money, check_int_input,
                       generate_starting_cards, is_blackjack, check_player_results, check_general_results)


def black_jack():
    round = 1
    dealer_bank = 10000 # static variables always declare them at the top of the logical block
    print(f"The dealer's bank is {dealer_bank}")

    player_bank = check_int_input("bank")
    amounts = {"dealer_bank": dealer_bank, "player_bank": player_bank}

    while amounts["player_bank"] > 0:
        print(f"Round: {round}")

        round += 1
        bet(amounts)

        player_cards, dealer_cards, generated_cards = generate_starting_cards()

        print("Your cards", player_cards[0], player_cards[1])
        print("Dealer cards", dealer_cards[0], "[?, ?]")

        result = is_blackjack(player_cards, dealer_cards)

        if result == "continue playing":
            player_result, generated_cards = player_turn(player_cards[0], player_cards[1], generated_cards)
            result = check_player_results(player_result)

            if result == "continue playing":
                input("Press Enter key to continue with the dealer's turn...")
                dealer_result, generated_cards = dealer_turn(dealer_cards[0], dealer_cards[1], generated_cards)

                input("Press Enter key to check results...")
                result = check_general_results(player_result, dealer_result)

        distribute_money(result, amounts)

        if amounts["player_bank"] == 0:
            break

        while True:
            stop = input("Would you like to continue?(Y/N): ")

            if stop.lower() == "n":
                print(f"The game was ended, you left it with the amount of {amounts['player_bank']}")
                return print("Please play again soon! 😉")
            elif stop.lower() == "y":
                break
            else:
                print("Invalid input. Please enter 'Y' to continue or 'N' to stop.")

    print(f"The game was ended, the player doesn't have enough money to bet 😢")
    return print("Please recharge your bank and play again soon! 😉")
