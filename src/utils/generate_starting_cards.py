from .card_generator import card_generator

def generate_starting_cards():
    generated_cards = []
    for i in range(4):
        card, generated_cards = card_generator(generated_cards)

    return [generated_cards[0], generated_cards[1]], [generated_cards[2], generated_cards[3]], generated_cards
