
# Напишите однокарточную версию игры "Война", структура раунда в которой такова:
# все игроки тянут по дной карте, а выигрывает тот, у кого номинал карты оказывается наибольшим.

import cards, games


class WarHand(cards.Hand):

    def __init__(self, name):
        super(WarHand, self).__init__()
        self.name = name

    def __str__(self): 
        return self.name + ": " + super(WarHand, self).__str__()

    def ranks(self):
      RANKS = cards.Card.RANKS[1:] + cards.Card.RANKS[0:1]
      return RANKS

    def position_card(self):
      card = self.cards[0]
      return card.get_rank(WarHand.ranks(self))


class WarGame(object):

    def __init__(self, names):      
        self.players = []
        for name in names:
            player = WarHand(name)
            self.players.append(player)

        self.deck = cards.Deck()
        self.deck.populate()
        self.deck.shuffle()

    def play(self):
        self.deck.deal(self.players, per_hand = 1)
        win_position = 0
        win = ''
        for player in self.players:
          print(player)
          card_position = player.position_card()
          name = player.name
          player.clear()

          if card_position > win_position:
            win_position = card_position
            win = name
          elif card_position == win_position:
            win += ' and ' + name
        print('-----')
        print('Win:', win)
        

def main():
    print("\t\tWelcome to War!\n")
    
    names = []
    number = games.ask_number("How many players? (2 - 4): ", low = 2, high = 5)
    for i in range(number):
        name = input("Enter player name: ")
        names.append(name)
    print()

    again = None
    while again != "n":
        game = WarGame(names)
        game.play()
        again = games.ask_yes_no("\nDo you want to play again?: ")
        print()


main()