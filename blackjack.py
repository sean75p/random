import random
from random import shuffle

class Card:
    card_face = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    card_suit = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

    def __init__(self):
        print('this is the beginning of Card class instantiation')

    def card_value(self):
        value_of_card = {'Ace': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8 , '9': 9, '10': 10,
                         'J': 10, 'Q': 10, 'K':10 }

        return value_of_card

class Deck(Card):
    new_deck = []

    for i in Card.card_suit:
        for j in Card.card_face:
            new_deck.append(j + ' of ' + i)

    def new_card(self):
        return (self.new_deck[random.randint(0, len(self.new_deck)-1)])

    def remove_card(self, card):
        self.new_deck.remove(card)

deck_of_cards = Deck()

print(deck_of_cards.new_deck)
print('asdf1')
temp=deck_of_cards.new_card()
print(temp)
deck_of_cards.remove_card(temp)
print(deck_of_cards.new_deck)


def get_deck():
    """Return a deck of cards"""
    return[[rank, suit] for rank in ranks for suit in suits]



# class People:
#     def __init__(self, name, money):
#         self.name = name
#         self.money = 0
#
#     add_money =12
#     subtract_money =13
#
# john = People('John',0)
#
# print(john.name);
# print(john.money)
#
# print(john.add_money)
# print(john.subtract_money)
#
# print(Card.card_face)
