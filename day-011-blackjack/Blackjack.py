import random
import os   

def playgame():
    '''Play a single round of blackjack.
    '''
    def draw():
        ''' Draws a card from deck
        '''
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        return cards[random.randint(0, len(cards) - 1)]

    def player_draw(hand=[]):
        ''' Draw a card for a player
        '''
        if len(hand) == 0:
            hand.append(draw())

        hand.append(draw())     
        
        if 11 in hand and sum(hand) > 21:
            hand[hand.index(11)] = 1

        return sum(hand)

    def comp_draw(hand=[]):
        ''' Draw a card for a computer
        '''
        hand.append(draw())

        if sum(hand) < 17 and len(hand) > 1:
            hand.append(draw())

        return sum(hand)
    
    #initial draw
    player = {"hand": [], "score": 0} 
    comp = {"hand": [], "score": 0}

    player["score"] = player_draw(player["hand"])
    comp["score"] = comp_draw(comp["hand"])

    #next draw

    print(f"\t Your Cards: {player['hand']}, Current Score: {player['score']}")
    print(f"\t Dealer's Card(s): {comp['hand']}, Dealer's Score: {comp['score']}")
    
    if player['score'] <= 21:
        draw_again = input("Type 'y' to get another card, type 'n' to pass: ").lower()

        if draw_again == 'y':
            player["score"] = player_draw(player["hand"])

        comp["score"] = comp_draw(comp["hand"])
        print(f"\t Your Cards: {player['hand']}, Current Score: {player['score']}")
        print(f"\t Dealer's Card(s): {comp['hand']}, Dealer's Score: {comp['score']}")


    #decide outcome
    if player["score"]  > 21:
        print("You went over. You lose!")
        return
    
    if player["score"] < comp["score"]:
        print("Delear's hand is higher than yours. You lose!")
        return
    
    if player["score"] > comp["score"]:
        print("Delear's hand is lower than yours. You win!")
        return
    
    print("Draw!!!")
    return

while (input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y'):
    os.system('cls||clear')
    playgame()
    print("")




