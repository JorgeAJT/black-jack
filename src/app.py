from src.utils import (card_generator, bet, player_turn, dealer_turn,
                       check_results, distribute_money, check_int_input)


def black_jack():
    round = 1
    dealer_bank = 10000 # static variables always declare them at the top of the logical block
    print(f"The dealer's bank is {dealer_bank}")

    player_bank = check_int_input("bank")
    amounts = {"dealer_bank": dealer_bank, "player_bank": player_bank}

    while amounts["player_bank"] > 0:
        print(f"Round: {round}")
        generated_cards = [] # empty variables always declare them at the top of the logical block

        round += 1
        bet(amounts)

        player_card1, generated_cards = card_generator(generated_cards) # this is duplicated 4 times, make a function for it
        player_card2, generated_cards = card_generator(generated_cards)
        dealer_card1, generated_cards = card_generator(generated_cards)
        dealer_card2, generated_cards = card_generator(generated_cards)

        print("Your cards", player_card1, player_card2)
        print("Dealer cards", dealer_card1, "[?, ?]")

        player_result, generated_cards = player_turn(player_card1, player_card2, generated_cards)
        input("Press Enter key to continue with the dealer's turn...")



        dealer_result, generated_cards = dealer_turn(dealer_card1, dealer_card2, generated_cards)
        input("Press Enter key to check results...")

        result = check_results(player_result, dealer_result)
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

