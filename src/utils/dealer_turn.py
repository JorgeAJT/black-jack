from .card_generator import card_generator
from .check_card import check_card


def dealer_turn(card1_gen, card2_gen, generated_cards):
    print("Dealer turn:")
    all_cards = [card1_gen, card2_gen]
    print(all_cards)

    if card1_gen[0] == "A" and card2_gen[0] == "A": # if AA == "".join(card_gen) ;)
        addition = 12
    else:
        card1 = check_card(card1_gen, "dealer")
        card2 = check_card(card2_gen, "dealer")
        addition = card1[0] + card2[0]
    while True:
        if addition < 17:
            new_card_gen, generated_cards = card_generator(generated_cards)
            all_cards.append(new_card_gen)
            print(all_cards)
            new_card = check_card(new_card_gen, "dealer", addition)
            addition += new_card[0]
        else:
            print(f"The sum of dealer's cards are {addition}")
            break

    return {"addition": addition, "cards": len(all_cards)}, generated_cards
