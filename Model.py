from Player import Player
from Deck import Deck
from PlayersStats import PlayersStats

def checkCurrentCardOnTable(card, ifFirstRound=0):

    if ("6" in card[0]):
        if (game.getCurrentPlayer() == 0): i = PLAYERNUM-1;
        else : i = game.getCurrentPlayer()-1
        game.playersArray[i].takeCardfromDeck(deck.giveCard())
        if (game.howMuchPlayers() == 2): game.nextPlayerTurn()
        return

    if ("7" in card[0]):
        if (game.getCurrentPlayer() == PLAYERNUM-1): i = 0
        else : i = game.getCurrentPlayer()+1
        for j in range (0, 2):
            game.playersArray[i-ifFirstRound].takeCardfromDeck(deck.giveCard())
        game.nextPlayerTurn()
        return

    if ("9d" in card):
        if (game.getCurrentPlayer() == PLAYERNUM-1): i = 0
        else : i = game.getCurrentPlayer()+1
        for j in range (0, 5):
            game.playersArray[i-ifFirstRound].takeCardfromDeck(deck.giveCard())
        game.nextPlayerTurn()
        return

    if ("A" in card[0]):
        game.nextPlayerTurn()
        return

def checkIfNotEnd():
    for i in range (0, PLAYERNUM):
        if (len(game.playersArray[i].getPlayerCards()) == 0):
            return False
    return True

def isGoodCard(chosenCard):
    if (chosenCard[0:-1] == 'J'):
        return True
    if (chosenCard[-1:] == deck.getCurrentSuit()):
        return True
    if (chosenCard[0:-1] == deck.getCurrentCardType()):
        return True
    return False

def calculatePlayerScore():
    for i in range(0, PLAYERNUM):
        score = 0
        cardType = ''
        for j in range(0, len(game.playersArray[i].getPlayerCards())):
            cardType = game.playersArray[i].getPlayerCards()[j][0:-1]
            try:
                score += int(cardType)
            except ValueError:
                if (cardType == 'A'): score += 11
                if (cardType == 'K'): score += 4
                if (cardType == 'Q'):
                    if (len(game.playersArray[i].getPlayerCards()) == 1): score += 30
                    else: score +=3
                if (cardType == 'J'):
                    if (len(game.playersArray[i].getPlayerCards()) == 1): score += 20
                    else: score +=2
        game.setPlayersScore(i, score)
    if(deck.getCurrentCardType() == "Q"): game.setPlayersScore(game.getCurrentPlayer()-1, -30)
    if(deck.getCurrentCardType() == "J"): game.setPlayersScore(game.getCurrentPlayer()-1, -20)

PLAYERNUM = 4

deck = Deck()

game = PlayersStats(PLAYERNUM, deck.cardsDeck[0:-len(deck.cardsDeck)+PLAYERNUM*4])  # Give cards to players (at the begin 4 to each)
deck.cardsDeck = deck.cardsDeck[-len(deck.cardsDeck)+PLAYERNUM*4:]

deck.putCardOnTable (deck.giveCard())

checkCurrentCardOnTable(deck.getCurrentCardOnTable(), 1)


calculatePlayerScore()

while checkIfNotEnd():

    for i in range(0, PLAYERNUM):
        print(game.playersArray[i].getPlayerCards())

    print("current card:", deck.getCurrentCardType())
    print ("current suit:", deck.getCurrentSuit())
    print("on table:",deck.getAllCardsOnTable())
    print ("current:", deck.getCurrentCardOnTable())

    print ("No:", game.getCurrentPlayer()+1, ":")
    print (game.playersArray[game.getCurrentPlayer()].getPlayerCards())

######################### PLAYER CHOOSE CARD FOR TURN ###################################
    while (True):
        chosenCard = input("CHOUSE NUMBER THE CARD (\"Press enter\" if no card):")

        if (chosenCard != '' and isGoodCard(''.join(game.playersArray[game.getCurrentPlayer()].getPlayerCards(int(chosenCard)-1, int(chosenCard))))):
                deck.putCardOnTable(game.playersArray[game.getCurrentPlayer()].makeTurn(int(chosenCard)-1))
                if (deck.getCurrentCardType() == 'J' and len(game.playersArray[game.getCurrentPlayer()].getPlayerCards())>0):
                    newSuit = input("CHANGE SUIT:")
                    deck.setNewSuit(newSuit)
                checkCurrentCardOnTable(deck.getCurrentCardOnTable())
                break
        if (chosenCard == ''):
            game.playersArray[game.getCurrentPlayer()].takeCardfromDeck(deck.giveCard())
            print ("No:", game.getCurrentPlayer()+1, ":")
            print (game.playersArray[game.getCurrentPlayer()].getPlayerCards())
            while (True):
                chosenCard = input("CHOUSE NUMBER THE CARD (\"Press enter\" if no card):")
                if (chosenCard != '' and isGoodCard(''.join(game.playersArray[game.getCurrentPlayer()].getPlayerCards(int(chosenCard)-1, int(chosenCard))))):
                    deck.putCardOnTable(game.playersArray[game.getCurrentPlayer()].makeTurn(int(chosenCard)-1))
                    checkCurrentCardOnTable(deck.getCurrentCardOnTable())
                    if (deck.getCurrentCardType() == 'J'):
                        newSuit = input("CHANGE SUIT:")
                        deck.setNewSuit(newSuit)
                    break
                if (chosenCard == ''):
                    break
                print ("wrong card")
            break
        print ("wrong card")

################################ END OF BLOCK #########################################

    game.nextPlayerTurn()

calculatePlayerScore()
