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
print('-------------------------------------------')
temp=deck_of_cards.new_card()
temp2=deck_of_cards.new_card()
print(temp)
print(temp2)
print('+++++++++')
deck_of_cards.remove_card(temp)
deck_of_cards.remove_card(temp2)
print(deck_of_cards.new_deck)


def get_deck():
    """Return a deck of cards"""
    return[[rank, suit] for rank in ranks for suit in suits]



class People:
    def __init__(self, name, money):
        self.name = name
        self.money = 0

    def add_money(self, temp):
        self.money += temp

    def subtract_money(self, temp):
        self.money -= temp

John = People(name='John', money=10)
John.add_money(11)
print(John.name)
print(John.money)
John.add_money(10)
print(John.money)
John.subtract_money(19)
print(John.money)
print(vars(John))


# print(Card.card_face)
# output shows:
# ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
# print(Card().card_suit)
# output shows:
# this is the beginning of Card class instantiation
# ['Clubs', 'Diamonds', 'Hearts', 'Spades']
