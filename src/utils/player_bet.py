from .check_int_input import check_int_input


def bet(amounts):
    print(f"The dealer's bank is {amounts['dealer_bank']}")
    print(f"Your bank is {amounts['player_bank']}")

    bet_amount = check_int_input("bet", amounts)
    amounts['bet_amount'] = bet_amount
    amounts['player_bank'] = amounts['player_bank'] - bet_amount

    return amounts
