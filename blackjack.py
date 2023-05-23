import random
from random import shuffle

class Card:
    card_number_or_face = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    face_card = ['Ace', 'J', 'Q', 'K']
    card_suit = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

    def __init__(self):
        print('this is the beginning of Card class instantiation')

    def calculate_value(self):
        value_of_card = {'Ace': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
                     'J': 10, 'Q': 10, 'K': 10}
        return value_of_card

class Deck(Card):
    new_deck = []
    for i in Card.card_suit:
        for j in Card.card_number_or_face:
            new_deck.append(j + ' of ' + i)

    length_of_deck = len(new_deck)

    def new_card(self):
        return (self.new_deck[random.randint(0, len(self.new_deck)-1)])
    def remove_card(self, card):
        self.new_deck.remove(card)
    def shuffle_cards(self):
        random.shuffle(deck_of_cards.new_deck)

class People(Deck):

    def __init__(self, name="NoName", money=0):
        self.name = name
        self.money = money
    def add_money(self, temp):
        self.money += temp
    def subtract_money(self, temp):
        self.money -= temp
    def deal_player(self):

        self.card1 = Deck.new_deck[Deck.length_of_deck-1]
        self.card2 = Deck.new_deck[Deck.length_of_deck-3]

        #find_of_position = str.find(self.card1, 'of')

        self.card1value = self.card1[0:str.find(self.card1, ' of')]
        self.card2value = self.card2[0:str.find(self.card2, ' of')]


    def deal_dealer(self):

        self.card1 = Deck.new_deck[Deck.length_of_deck - 2]
        self.card2 = Deck.new_deck[Deck.length_of_deck - 4]

        self.card1value = self.card1[0:str.find(self.card1, ' of')]
        self.card2value = self.card2[0:str.find(self.card2, ' of')]

deck_of_cards = Deck()

def get_deck():
    """Return a deck of cards"""
    return[[rank, suit] for rank in ranks for suit in suits]

print('+++++++++=================================================')

deck_of_cards.shuffle_cards()
print(deck_of_cards.new_deck)
print(deck_of_cards.new_deck[0])


print('++++++++++++++++++++++++++++++++++')
Dealer = People(name='Dealer', money=0)
Sean = People('Sean', 100)

Sean.deal_player()
print(Sean.name, 'has', Sean.card1,'and', Sean.card2)
print(Sean.card1value, Sean.card2value)
print('total value:', Sean.calculate_value()[Sean.card1value] + Sean.calculate_value()[Sean.card2value] )

Dealer.deal_dealer()
print('Dealer has', Dealer.card1,'and', Dealer.card2)
print(Dealer.card1value, Dealer.card2value)
print(Dealer.calculate_value()[Dealer.card1value], Dealer.calculate_value()[Dealer.card2value])
print('total value:', Dealer.calculate_value()[Dealer.card1value] + Dealer.calculate_value()[Dealer.card2value] )


# print(Card.card_face)
# output shows:
# ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
# print(Card().card_suit)
# output shows:
# this is the beginning of Card class instantiation
# ['Clubs', 'Diamonds', 'Hearts', 'Spades']