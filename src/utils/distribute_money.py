def distribute_money(result, amounts):
    # Good!
    if result == "loose":
        amounts['dealer_bank'] += amounts['bet_amount']
        print(f"Now your bank is {amounts['player_bank']}")
    elif result == "win":
        amounts['player_bank'] += (amounts['bet_amount'] * 2)
        amounts['dealer_bank'] = amounts['dealer_bank'] - amounts['bet_amount']
        print(f"Now your bank is {amounts['player_bank']}")
    elif result == "tie":
        amounts['player_bank'] += amounts['bet_amount']
        print(f"Your bank is as it was at the beginning of this round with {amounts['player_bank']}")

    return amounts
