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

    random.shuffle(new_deck)

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
        self.card_list = []
    def add_money(self, temp):
        self.money += temp
    def subtract_money(self, temp):
        self.money -= temp

    def deal_cards_for_two_players(self, newdeck):

        self.card1 = Deck.new_deck[-1]
        self.card2 = Deck.new_deck[-3]
        self.card3 = Deck.new_deck[-2]
        self.card4 = Deck.new_deck[-4]


    def card_to_integer(self, card):
        # find_of_position = str.find(self.card_list, ' of')
        temp = []
        for i in card:
            self.cardxvalue = i[0:str.find(i, ' of')]
            self.cardxvalue = self.calculate_value()[self.cardxvalue]
            temp.append(self.cardxvalue)

        self.cardxvalue = temp

    def deal_one_card_from_top_of_deck(self, deck):
        self.card_list.append(deck.pop(-1))

deck_of_cards = Deck()

def get_deck():
    """Return a deck of cards"""
    return[[rank, suit] for rank in ranks for suit in suits]

print('=================================================')


print(deck_of_cards.new_deck)

print('++++++++++++++++++++++++++++++++++')
Dealer = People(name='Dealer', money=0)
Sean = People('Sean', 100)

Sean.deal_one_card_from_top_of_deck(Sean.new_deck)

Dealer.deal_one_card_from_top_of_deck(Sean.new_deck)

Sean.deal_one_card_from_top_of_deck(Sean.new_deck)

Dealer.deal_one_card_from_top_of_deck(Sean.new_deck)

print("Sean's cards", Sean.card_list)
Sean.card_to_integer(Sean.card_list)
print(Sean.cardxvalue, 'total', sum(Sean.cardxvalue))
print("Dealer's cards", Dealer.card_list)
Dealer.card_to_integer(Dealer.card_list)
print(Dealer.cardxvalue, 'total', sum(Dealer.cardxvalue))


#end

# print(Card.card_face)
# output shows:
# ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
# print(Card().card_suit)
# output shows:
# this is the beginning of Card class instantiation
# ['Clubs', 'Diamonds', 'Hearts', 'Spades']
