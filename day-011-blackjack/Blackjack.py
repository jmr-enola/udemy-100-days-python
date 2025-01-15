import random

def playgame():
    
    def draw():
        ''' Draws a card from deck
        '''
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        return cards[random.randint(0, len(cards))]

    def player_draw(hand=[]):
        ''' Draw a card for a player
        '''
        if len(hand) == 0:
            hand.append(draw())

        hand.append(draw())     
        
        if 11 in hand and sum(hand) > 21:
            hand[hand.index(11)] = 1

        return hand

    def comp_draw(hand=[]):
        ''' Draw a card for a computer
        '''
        hand.append(draw())

        if sum(hand) < 17:
            hand.append(draw)

        return hand




