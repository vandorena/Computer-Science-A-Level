import random


class Card:
    """ A class to describe cards in a pack """
    def __init__(self, number):
        self._card_number = number

    def get_suit(self):
        """ return a string 'C', 'S', 'H', 'D' """
        pass

    def get_value(self):
        """ return a string 'A'..'10', 'J', 'Q', 'K' """
        pass

    def get_short_name(self):
        """ return card name eg '10D' '8C' 'AH' """
        pass

    def get_long_name(self):
        """ return card name eg 'Ten of Diamonds' """
        pass
    
    def get_suit(self):
        self.suit = "nothing"
        self.tempcardnum = self._card_number
        if self.get_cardval() == "king":
            self.tempcardnum = self._card_number - 1
        if self.tempcardnum // 13 == 0:
            self.suit = "Hearts"
        elif self.tempcardnum // 13 == 1:
            self.suit = "Diamonds"
        elif self.tempcardnum // 13 == 2:
            self.suit = "Spades"
        elif self.tempcardnum // 13 == 3:
            self.suit = "Clubs"
        return self.suit
    
    def get_cardval(self):
        valueweight = self._card_number % 13
        if valueweight < 11 and valueweight != 0:
            self.card_value = str(valueweight)
        elif valueweight == 11:
            self.card_value = "jack"
        elif valueweight == 12:
            self.card_value = "queen"
        elif valueweight == 0:
            self.card_value = "king"
        else:
            self.card_value = "error"
        return str(self.card_value)


class Deck:
    """ A class to contain a pack of cards with methods for shuffling, adding or removing cards etc. """
    def __init__(self):
        self._card_list = []
        for i in range(52):
            self._card_list.append(Card(i))

    def length(self):
        """ returns the number of cards still in the deck """
        pass

    def shuffle_deck(self):
        """ shuffles the cards """
        random.shuffle(self._card_list)

    def take_top_card(self):
        """ removes the top card from the deck and returns it (as a card object) """
        pass
    
    

for i in range (1,53):
    card = Card(i)
    print(card.get_suit())
    print(card.get_cardval())
# deck = Deck()
# deck.shuffle_deck()
# for _ in range(deck.length()):
#     card = deck.take_top_card()
#     print(card.get_long_name())