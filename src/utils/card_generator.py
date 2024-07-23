from random import randint, choice


def card_generator(generated_cards):
    while True:
        card_number = randint(1,13)

        special_cards = {
            1: "A",
            11: "J",
            12: "Q",
            13: "K"
        }

        card_number = special_cards.get(card_number, card_number)

        card_suit = choice(["♣", "♥", "♠", "♦"])
        card = [card_number, card_suit]

        if card not in generated_cards:
            generated_cards.append(card)
            return card, generated_cards