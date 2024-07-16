def check_card(card, role, addition=0):

    face_cards = {"J", "Q", "K"}
    if card[0] in face_cards:
        card[0] = 10

    elif card[0] == "A" and role == "player":
        while True:
            value = input("Type wisely the value you want for your ACE (1 or 11): ")
            if value == "1":
                break
            elif value == "11":
                break

        value_int = int(value)
        card[0] = value_int

    elif card[0] == "A" and role == "dealer":
        if addition + 11 > 21:
            card[0] = 1
        else:
            card[0] = 11

    return card
