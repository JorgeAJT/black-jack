from .card_generator import card_generator
from .check_card import check_card


def player_turn(card1_gen, card2_gen, generated_cards):
    print("Player turn:")
    face_cards = {10, "J", "Q", "K"}

    if (card1_gen[0] == "A" and card2_gen[0] in face_cards) or (card2_gen[0] == "A" and card1_gen[0] in face_cards): # Good
        addition = 21
        return {"addition": addition, "cards": 2}, generated_cards
    else:
        if card1_gen[0] == "A" and card2_gen[0] == "A":
            addition = 12
        else:
            card1 = check_card(card1_gen, "player")
            card2 = check_card(card2_gen, "player")
            addition = card1[0] + card2[0]

        all_cards = [card1_gen, card2_gen]
        while True:
            print(f"The sum of your cards are {addition}")
            response = input("Would you like other card?(Y/N): ")

            if response.lower() == "n":
                break

            if response.lower() == "y":
                new_card_gen, generated_cards = card_generator(generated_cards)
                all_cards.append(new_card_gen)
                print(all_cards)

                new_card = check_card(new_card_gen, "player")
                addition += new_card[0]

                if addition >= 21:
                    print(f"The sum of your cards are {addition}")
                    break

        return {"addition": addition, "cards": len(all_cards)}, generated_cards
