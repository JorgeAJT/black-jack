def check_int_input(kind, amounts=None):
    while True:
        if kind == "bank":
            player_bank_input = input("Please, insert your bank: ")
            try:
                player_bank_input = int(player_bank_input)
                return player_bank_input
            except ValueError:
                print("Please, type a number, not a word or letter 😅")

        if kind == "bet":
            bet_amount_input = input("Please insert your bet: ")
            try:
                bet_amount_input = int(bet_amount_input)
            except ValueError:
                print("Please, type a number, not a word or letter 😅")
            else:
                if bet_amount_input > amounts['player_bank']:
                    print("You cannot bet more than your bank!🤦‍♂️")
                else:
                    return bet_amount_input
