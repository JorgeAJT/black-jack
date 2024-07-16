from random import randint, choice


def card_generator(generated_cards):
    while True:
        card_number = randint(1,13)

        if card_number == 1:
            card_number = "A"
        elif card_number == 11:
            card_number = "J"
        elif card_number == 12:
            card_number = "Q"
        elif card_number == 13:
            card_number = "K"


        ## ================>
        #
        # You could have also done a simpler map, which avoids processing
        special_cards = {
            1: "A",
            11: "J",
            12: "Q",
            13: "K"
        }

        card_number = special_cards[card_number]

        ## <================

        card_suit = choice(["♣", "♥", "♠", "♦"])
        card = [card_number, card_suit]

        if card not in generated_cards:
            generated_cards.append(card)
            return card, generated_cards

# dictionary.get(llave que quiero acceder, lo que retorna si la llave no existe)