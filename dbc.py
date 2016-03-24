# This is a program written in Python to create a Deck Building
# Card game. This game is a one player game as the opponent is
# the computer. The player and the computer are provided with 
# an initial set of cards and an initial health value. Apart from 
# this, there are various cards available in the main deck, which 
# can be accessed and bought by players if the cards are placed in 
# the active part of the central area. A player may buy cards using 
# their accumulated wealth, and buying a card offers the player additions 
# in wealth and attack power. A player can choose to attack its opponent, 
# upon which the health of the opponent would be reduced by the amount of 
# attack power the player has. The players take turns to buy, attack and
# play cards. Finally the player which mananges to reduce the opponent's 
# health to 0 or below, wins the game.
import itertools, random

# Initialising the parameters which have been pre-decided 
# and will not change its values during the course of game.
# The parameters are:
# 1) The intiial health points given to each player.
# 2) The size of the player's Hand, that is, the maximum
#    number of cards that can be on the player's active area.
# 3) The maximum number of cards that are shifted from main 
#    deck to the active area for both players to choose from
initialHealth = 30
playerHandsize = 5
mainDeckActiveSize = 5

class Card(object):
    """
    Defining class Card, the object of which would be a card
    with a distinct name, its price or cost and the wealth and 
    attack points it will add on, if bought by a player.
    """

    def __init__(self, name, values, cost):
        """
        This method sets all parameterz of the card object created,
        that is, the name, cost and the wealth and attack power offered
        by the card.
        """

        self.name = name
        self.cost = cost
        self.values = values

    def __str__(self):
        """
        # This method prints the details of the card onto standard output.
        """

        return 'Name %s costing %s with attack %s and money %s' % (self.name, self.cost, self.values[0], self.values[1])

    def get_attack(self):
        """
        This method returns the attack power that the particular Card object,
        if bought, offers to the player.
        """

        return self.values[0]
    
    def get_money(self):
        """
        This method returns the value by which a player's wealth is increased,
        if the Card is bought.
        """

        return self.values[1]
    
    def getCost(self):
        """
        This method returns the cost of the card, that will be required to be
        paid by the player to buy that card
        """

        return self.cost
   
    def getName(self):
        """
        This method returns the name of the card.
        """
        
        return self.name

class Player:
    """
    Defining class Player, the object of which would be a Player with a
    distinct name, health, wealth and attack power. Apart from these, the
    player's Hand, the cards in the active area and the cards in the discard
    pile are also defined by this object.
    """

    def __init__(self, name, initialDeck):
        """
        This method initialises all attributes associated with the Player
        object being created. Parameters such as the name of the player,
        initial health condition, initial deck cards and the number of cards
        allowed to be at the Player!'s hand aea are all intitialised here.
        """

	self.name = name
	self.health = initialHealth
	self.deck = list(itertools.chain.from_iterable(initialDeck))
	self.hand = []
	self.active = []
	self.handSize = playerHandsize
	self.discard = []
        self.money = 0
        self.attack = 0
   
    def setHand(self):
        """
        This method selects cards from the player's deck, the number equal to
        the number of cards required to reach the maximum number of cards allowed
        to be present in the player's hand. If the player's deck dies not have any
        card, then the discard pile consisting of already played cards and cards
        that were bought are shuffled and placed in the deck.
        """

	for x in range(0, playerHandsize):
            if (len(self.deck) == 0):
                random.shuffle(self.discard)
                self.deck = self.discard
                self.discard = []
            card = self.deck.pop()
            self.hand.append(card)
 
    def setActive(self,card):
        """
        This method sets the card selected by the player from the Hand area to the
        active area.
        """

        self.active.append(card)
   
    def setDiscard(self, card):
        """
        This method sends a particular card to the discard pile for later use. Cards which
        are bought or are played in a player's turn, are sent to the discard pile.
        """
       
        self.discard.append(card)

    def setMoney(self, amount):
        """
        This method sets the new value of the amount of amoney a player has.
        """

        self.money = amount

    def setHealth(self, health):
        """
        This method sets the new health value for the player.
        """

        self.health = health

    def setAttack(self, attack):
        """
        This method updates the attack power of the player.
        """

        self.attack = attack

    def getHealth(self):
        """
        This method returns the health condition of the player, or the 
        value of health parameter of the player
        """

        return self.health

    def getDeck(self):
        """
        This method returns the list of cards in the player's deck area
        """

        return self.deck

    def getHand(self):
        """
        This method returns the list of cards in the player's Hand area
        """

        return self.hand

    def getActive(self):
        """
        This method returns the list of cards in the player's active area
        """

        return self.active

    def getDiscard(self):
        """
        This method returns the list of cards in the player's discard pile
        """

        return self.discard
    def getMoney(self):
        """
        This method returns the amount of wealth accumulated by the player
        """

        return self.money
    def getAttack(self):
        """
        This method returns the attack power the player has accumulated
        """

        return self.attack

    def getName(self):
        """
        This method returns the name of the player
        """

        return self.name

def initialiseCentralActiveArea(central):
    """
    This method initialises the central active area. At the start of the game,
    number of cards equal to the maximum number of cards that can be selected
    for the active area, are taken out from the main deck and shifted to the
    active area.
    """

    count = 0
    while count < mainDeckActiveSize:
        card = central['deck'].pop()
        central['active'].append(card)
        count = count + 1

def printAvailableCards():
    """
    This method prints in standard output the details of the available cards
    in the central active area and the supplement card details as well. This
    helps the player to look at all the options and then decide which card to buy.
    """

    print "\nAvailable Cards"
    indicator = 0
    for card in central['active']:
        print "[%s] %s" % (indicator, card)
        indicator = indicator + 1

    print "\nSupplement Cards"
    if len(central['supplement']) > 0:
        print "%s of %s" % (len(central['supplement']), central['supplement'][0])

def printPlayerHealth(player):
    """
    This method prints the Health condition of a player. It accepts the particular
    player object as its parameter and prints its health condition in standard output.
    """

    print "%s's Health: %s" % (player.getName(), player.getHealth())

def printHand(player):
    """
    This method prints information about all the cards that are present in a player's
    hand area. It accepts the player object as a parameter and prints the details of
    the cards in standard output.
    """

    print "\n%s's Hand" % (player.getName())
    index = 0
    for card in player.getHand():
        print "[%s] %s" % (index, card)
        index = index + 1
    if index == 0:
        print "NIL"

def printValues(player):
    """
    This method prints onto standard output, the wealth and the attack power for a
    player. It takes the player object as an input parameter and prints the wealth and
    attack power for that player.
    """

    print "\n%s's Values" % (player.getName())
    print "Wealth: %s, Attack Power: %s" % (player.getMoney(), player.getAttack())

def printActiveCards(player):
    """
    This method prints the details of the list of cards present in the player's
    active area. IT takes in the player object as an input parameter and prints
    information about the cards onto standard output.
    """

    print "\n%s's Active Cards" % (player.getName())
    for card in player.getActive():
        print card

def playAllCards(player):
    """
    This method selects all cards in the player's hand area and transfers them to
    the active area for being used to play against the opponent. As this method is
    called when player chooses to play with all cards, it accesses all the cards in
    the hand area and appends them to the active card list one by one.
    """

    if(len(player.getHand()) > 0):
        for x in range(0, len(player.getHand())):
            card = player.getHand().pop()
            setActiveForPlayer(player, card)

def setActiveForPlayer(player, card):
    """
    This method transfers the card selected by the user from the Hand area to the
    player's active area. This method is called when a single card is selected by the
    user. It takes the player object and the selected card as input parameters and
    removes that particular card from the hand area and appends it to the list of
    cards available in the active area.
    """

    player.setActive(card)
    player.setMoney(player.getMoney() + card.get_money())
    player.setAttack(player.getAttack() + card.get_attack())

def buyCardForPlayer(player, cardIndex, cardStack, indicator, central):
    """
    This method is used to purchase the chosen card for the player. It is first
    checked whether the player has sufficient money to buy the card or not. If
    not then an error message s printed to the user. Otherwise the wealth of
    the player is reduced by the cost of the card and the card is removed from
    the card list. Now, if the card list in question is the central active area
    cards, then a card from the central deck is taken and placed in the central
    active area in order to replenish the list. If no cards are available to be
    moved from the central deck then the active area size is reduced by one
    """

    if player.getMoney() >= cardStack[int(cardIndex)].getCost():
        player.setMoney(player.getMoney() - cardStack[int(cardIndex)].getCost())
        player.setDiscard(cardStack.pop(int(cardIndex)))
        if indicator == 'central':
            if (len(central['deck']) > 0):
               card = central['deck'].pop()
               central['active'].append(card)
            else:
               central['activeSize'] = central['activeSize'] - 1
        print "Card bought"
    else:
        print "insufficient money to buy"

def reduceOpponentHealth(player, opponent):
    """
    This method is used to reduce the opponent's health condition using the attack
    power the player has accumulated. This method takes in the player and opponent
    player objects and substracts a value equal to the attack power of the player
    from the health value of the opponent.
    It also sets the attack power of the player to zero, as its all used up to attack
    the opponent
    """

    print "%s attacks %s" % (player.getName(), opponent.getName())
    opponent.setHealth(opponent.getHealth() - player.getAttack())
    player.setAttack(0)

def setDiscardAtEOT(player):
    """
    This method is called at the end of each turnof a player. When a player decides
    to end their turn, this method removes all the cards in the player's  hand area
    and active area and appends them to the player's discard pile.
    """
    if len(player.getHand()) > 0:
        for x in range (0, len(player.getHand())):
            player.setDiscard(player.getHand().pop())
    if len(player.getActive()) > 0:
        for x in range (0, len (player.getActive())):
            player.setDiscard(player.getActive().pop())

def checkForResult(player, opponent):
    """
    This method checks whether the game is over or not. Whenever a player attacks
    the opponent, this method is called which checks whether the health value of any
    of the players has been reduces to zero or lesser. If yes then the other player
    is declared as the winner and it returns a string value indicating that the game
    has ended. However, if both players have positive health values, then the number
    of cards in the active area is checked. If that is zero, it indicates that there
    are no more cards left to be used and thus it checks which player has a better
    health condition and declares that player as the winner.
    If the central active area still has cords to be played with, then the game is
    considered to be still playable and thus, the string value sent back indicates that
    the game still has to be played further to reach a decision.
    """

    if player.getHealth() <= 0:
        print "%s wins" % opponent.getName()
        return "end"
    elif opponent.getHealth()  <= 0:
        print '%s wins' % player.getName()
        return "end"
    elif central['activeSize'] == 0:
        print "No more cards available"
        if playerOne.getHealth() > playerComputer.getHealth():
            print "Player One Wins on Health"
            return "end"
        elif playerComputer.getHealth() > playerOne.getHealth():
            print "Computer Wins on Health"
            return "end"
        else:
            print "Draw"
            return "end"
    else:
        return "not end"

if __name__ == '__main__':
    # Initialising a variable called 'result' as 'not end' at the start of the program.
    # This will only be set to 'end' when the game would be over and based on this value
    # the execution of the game would be stopped and another new game would be prompted to be started.
    result = "not end"
    # Initialsing the variable 'playedOnce' to false. Only when a game is chosen to be started that 
    # this variable is set to true.
    playedOnce = False

    while True:
        # Checking the value of playedOnce variable to print a proper message to the user, that is,
        # whether the user want to play a/another game or not. If the playedOnce variable is set to true
        # it means that the game has already been played once and so the request message should ask the
        # user whether another game is desired or not
        if not playedOnce:
            userChoice = raw_input('Do you want to play a game? (Y/N): ')
        else:
            userChoice = raw_input('Do you want to play another game? (Y/N): ')

        # The followng part of the program checks whether the choice entered by the user is a correct
        # one or not. If the user has entered a value which is neither equal to 'Y' or 'N', then
        # the program should let the user know that a wrong choice has been entered and also ask for a
        # re-entry of the option. Also if the user choice is 'N', the program exits. Lastly, if the
        # user choice entered is 'Y' then the game proceeds.
        if userChoice != 'Y' and userChoice != 'N':
            print "Please enter Y or N."
        elif userChoice == 'N':
            print "Bye! See you later."
            exit()
        else:
            # flag "playedOnce" is set to True, indicating that the game has been played once in this session.
            playedOnce = True
            
            # Finalising on the type of opponent desired by the user. There are two types of opponents that
            # a player may choose to play against. They are the aggressive and the acquisative modes. Here the program
            # asks the user to enter the type of opponent desired. If anythign other than the options available
            # is entered by the user, then proper error message is given to the user and the choice is
            # again asked to be specified.
            oppChSelected = False
            while not oppChSelected:
                oppChoice = raw_input("Do you want an aggressive (A) opponent or an Acquisative (Q) opponent: ")
                if oppChoice != 'A' and oppChoice != 'Q':
                    print "Please enter correct choice. Type A for Aggressive or Q for Acquisative."
                else:
                    oppChSelected = True
    
            # Initialising and creating all the different Card objects
            serf = Card('Serf', (0, 1), 0)
            squire = Card('Squire', (1, 0), 0)
            archer = Card('Archer', (3, 0), 2)
            baker = Card('Baker', (0, 3), 2)
            swordsman = Card('Swordsman', (4, 0), 3)
            knight = Card('Knight', (6, 0), 5)
            tailor = Card('Tailor', (0, 4), 3)
            crossbowman = Card('Crossbowman', (4, 0), 3)
            merchant = Card('Merchant', (0, 5), 4)
            thug = Card('Thug', (2, 0), 1)
            thief = Card('Thief', (1, 1), 1)
            catapault = Card('Catapault', (7, 0), 6)
            caravan = Card('Caravan', (1, 5), 5)
            assassin = Card('Assassin', (5, 0), 4)
            levy = Card('Levy', (1, 2), 2)

            # Initialising the main deck and filling it in with a list of cards objects
            mainDeckCards = [4 * [archer], 4 * [baker], 3 * [swordsman], 2 * [knight], \
                             3 * [tailor], 3 * [crossbowman], 3 * [merchant], 4 * [thug], \
                             4 * [thief], 2 * [catapault], 2 * [caravan], 2 * [assassin]]

            # Initialising and setting up the central area. The central area comprises the main deck,
            # where the list of cards are shuffled and placed, the supplementary cards and the active area.
            central = {'name': 'central', 'active': None, 'activeSize': mainDeckActiveSize, 'supplement': None, 'deck': None}
            supplement = 10 * [levy]
            mainDeck = list(itertools.chain.from_iterable(mainDeckCards))
            random.shuffle(mainDeck)
            central['deck'] = mainDeck
            central['supplement'] = supplement
            central['active'] = []

            # Initialising the central active area with cards equal to the number of active size area specified,
            # being transferred from the main deck to the active area.
            initialiseCentralActiveArea(central)

            # Initialising all player environments. Firstly as all players are initially provided with the same
            # set of cards, the player initial deck is created. Then the Player objects are created. The attributes
            # of the players are intialised. The initial deck is set and the Hand is also set by transferring cards
            # equal to the maximum number of cards which can be placed in the hand area, from the player deck to
            # the hand area. 
            playerInitialDeck = [8 * [serf], 2 * [squire]]

            playerOne = Player('Player One', playerInitialDeck)
            playerComputer = Player('Player Computer', playerInitialDeck)
            playerOne.setHand()
            playerComputer.setHand()
            
            while True:
                while True:
                    # Printing both the player's health condition
                    printPlayerHealth(playerOne)
                    printPlayerHealth(playerComputer)
                    
                    # Printing the list of cards availablle for buying fron=m the central active area.
                    printAvailableCards()
                    
                    # As Player One starts the turn, the cards in the player's hand and its wealth and
                    # power are printed.
                    printHand(playerOne)
                    printValues(playerOne)
                    
                    # Prompting the user to choose an action. There are different actions that a player may choose
                    # in order to complete their turn. The options are playing all cards available in the player's
                    # hand against the opponent, choosing a single card to play against the opponent, buy more cards
                    # from the central active area using their wealth, attacking the opponent and reducing their
                    # health value by the amount of attack power they have or to end the turn.
                    print "\nChoose Action: (P = play all, [0-n] = play that card, B = Buy Card, A = Attack, E = end turn)"

            	    userOption = raw_input("\nEnter Action: ")
                    if userOption == 'P':
                        # If the player chooses to play all cards in the hand area against the opponent, then
                        # all the cards in the hand area are transferred to the active area and the wealth and
                        # attack power of the player is increased by the amount of money and attack power
                        # offered by the cards. The updated values are printing onto standard output.
                        playAllCards(playerOne)
                        printValues(playerOne)
          
                    elif userOption.isdigit():
                        # If the user chooses just one card to be used against the opponent, then firstly it is
                        # checked whether the number entered by the user corresponds to the number of any of the
                        # cards or not. If not then proper error message is given to the user and a new option is
                        # asked for. If the number matches with the number given to one of the cards, then that
                        # particular card is removed from the player's hand area and transferred to the active area.
                        # The wealth and attack power are updated as per the values offered by the card and printed.
                        if (int(userOption) < len(playerOne.getHand())):
                            card = playerOne.getHand().pop(int(userOption))
                            setActiveForPlayer(playerOne, card)
			    printHand(playerOne)
                            printValues(playerOne)
                        else:
                            print "\nPlease enter the correct number of the card."

                    elif userOption == 'B':
                        # If the player chooses to buy cards from the central active area, then it is first checked
                        # whether the user has wealth greater than zero or not. If not then proper error message is
                        # given to the user and a new option is asked to be entered by the user. If the player has
                        # sufficient money to buy cards, then firstly all the available cards are printed for the
                        # user to see and decide. All the cards are uniquely numbered and the user is asked for
                        # options to select from the cards. The user may select cards from the central active area
                        # or from the supplement cards. As per selection the card is added to the discard pile of
                        # of the player and the wealth of the player is reduced by the cost of the card. The player
                        # also choose to end buying, upon which the player is returned back.
                        if playerOne.getMoney() <= 0:
                            print "\nYou do not have sufficient money to buy cards. Please choose another action."
                        while playerOne.getMoney() > 0:
                            printAvailableCards()

                            print "\nChoose a card to buy [0-n], S for supplement, E to end buying"
                            buyCard = raw_input("Choose option: ")
                            if buyCard == 'S':
                                buyCardForPlayer(playerOne, 0, central['supplement'], 'supplement', None)
                                """if len(central['supplement']) > 0:
                                    if playerOne.getMoney() >= central['supplement'][0].cost:
                                        playerOne.setMoney(playerOne.getMoney() - central['supplement'][0].cost)
                                        playerOne.setDiscard(central['supplement'].pop())
                                        print "Supplement Bought"
             		            else:
				        print "Insufficient money to buy"
		                else:
                                    print "No supplements left"""
		            elif buyCard == 'E':
              		        break;
		            elif buyCard.isdigit():
	    	                if int(buyCard) < len(central['active']):
                                    buyCardForPlayer(playerOne, buyCard, central['active'], 'central', central)
                                    """if playerOne.getMoney() >= central['active'][int(buyCard)].cost:
                                        playerOne.setMoney(playerOne.getMoney() - central['active'][int(buyCard)].cost)
                               	        playerOne.setDiscard(central['active'].pop(int(buyCard)))
                                        if (len(central['deck']) > 0):
                                            card = central['deck'].pop()
                                            central['active'].append(card)
                                        else:
                                            central['activeSize'] = central['activeSize'] - 1
                                        print "Card bought"
                                    else:
                                        print "insufficient money to buy"""
                                else:
                                    print "enter a valid index number"
                            else:
                                print "Enter a valid option"
		
                    elif userOption == 'A':
                        # If the player chooses to attack the opponent then the health of the opponent
                        # is reduced by the amount of attack power the player has and the attack power
                        # of the player is reset to zero. After reducing the attack power of the 
                        # opponent, it is checked whether the health of the opponent has been reduced to
                        # zero or lesser or not. If yes, then the game stops here.
                        reduceOpponentHealth(playerOne, playerComputer)
                        result = checkForResult(playerOne, playerComputer)
                        if result == 'end':
			    break;
                    elif userOption == 'E':
                        # If the player chooses to end their turn, then all cards in the player's hand and
                        # active area are removed and put in the discard pile and a new list of cards are
                        # selected from the player's deck to be put in the player's hand area.
                        setDiscardAtEOT(playerOne)
                        playerOne.setHand()
		        break;
                    else:
                        print "\nPlease enter correct option."

                if result == "end":
                    break;
               
                # Now the computer starts playing. Again the available cards in the central deck area are
                # printed. Health condition of both the players are printed.
                printAvailableCards()

                printPlayerHealth(playerOne)
                printPlayerHealth(playerComputer)
        	
                # Computer plays all cards in the hand area against player one. All the cards are 
                # shifted to the computer's active area and the wealth and the attack power of the
                # computer is uodated accordingly as per the values offered by the card.
                playAllCards(playerComputer)

                # Reducing the player's health by the attack power of the computer player. Checking
                # whether the health of the player has been reduced to zero or lesser. If yes then 
                # the game stops here.
                reduceOpponentHealth(playerComputer, playerOne)
                result = checkForResult(playerComputer, playerOne)
                if result == "end":
                    break;
                
                # printing the health condition of both the players.
                printPlayerHealth(playerOne)
                printPlayerHealth(playerComputer)

                printValues(playerComputer)
                
                # Computer buying cards from the central active area. The way the computer chooses to buy depends
                # on the opponent type chosen by the player at the start of the game.
                print "Computer buying"
                if oppChoice == 'A':
                    # If the player chose an aggressive opponent, then the computer buys cards which have the maximum
                    # attack power to offer. Firstly all the available cards in the central active area are sorted
                    # as maximum attack power to minimum attack power, and then the cards are iterated in that order to
                    # see whether the cost of the card is lesser or equal to the amount of wealth the computer player
                    # has. If yes then the card is removed from the central active area and appended to the discard pile
                    # of the computer. This process is repeated till all the cards have been checked. Lastly the card is
                    # added from the central deck to the central active area. In case there is no card available in the 
                    # main deck then the size of the central active area is reduced.
                    while True:
                        bought = False
                        activeCardList = central['active']
                        sortedByAttack = sorted(activeCardList, key=lambda card: card.values[0], reverse=True)
                        for counter in range (0, len(sortedByAttack)):
                            if playerComputer.getMoney() >= sortedByAttack[counter].getCost():
                                playerComputer.setMoney(playerComputer.getMoney() - sortedByAttack[counter].getCost())
                                playerComputer.setDiscard(sortedByAttack[counter])
                                print "Computer bought: %s" % sortedByAttack[counter]
                                for counter2 in range (0, len(central['active'])):
                                    if central['active'][counter2].getName() == sortedByAttack[counter].getName():
                                        central['active'].pop(counter2)
                                        if (len(central['deck']) > 0):
                                            card = central['deck'].pop()
                                            central['active'].append(card)
                                        else:
                                            central['activeSize'] = central['activeSize'] - 1
                                        break;
                                bought = True
                        if not bought:
                            # If none of the cards are bought from the central area then the supplement section is checked
                            # cards are bought.
                            for counter in range (0, len(central['supplement'])):
                                if playerComputer.getMoney() >= central['supplement'][counter].getCost():
                                    playerComputer.setMoney(playerComputer.getMoney() - central['supplement'][counter].getCost())
                                    playerComputer.setDiscard(central['supplement'][counter])
                                    central['supplement'].pop()
                                    bought = True
                                    break;
                        if not bought:
                            break;
                else:
                    # If the player chose an acquisative opponent, then the computer buys cards which have the maximum
                    # money or wealth to offer. Firstly all the available cards in the central active area are sorted
                    # as maximum wealth to minimum, and then the cards are iterated in that order to
                    # see whether the cost of the card is lesser or equal to the amount of wealth the computer player
                    # has. If yes then the card is removed from the central active area and appended to the discard pile
                    # of the computer. This process is repeated till all the cards have been checked. Lastly a card is
                    # added from the central deck to the central active area. In case there is no card available in the
                    # main deck then the size of the central active area is reduced.
                    while True:
                        bought = False
                        activeCardList = central['active']
                        sortedByMoney = sorted(activeCardList, key=lambda card: card.values[1], reverse=True)
                        for counter in range (0, len(sortedByMoney)):
                            if playerComputer.getMoney() >= sortedByMoney[counter].getCost():
                                playerComputer.setMoney(playerComputer.getMoney() - sortedByMoney[counter].getCost())
                                playerComputer.setDiscard(sortedByMoney[counter])
                                for counter2 in range (0, len(central['active'])):
                                    if central['active'][counter2].getName() == sortedByMoney[counter].getName():
                                        central['active'].pop(counter2)
                                        if (len(central['deck']) > 0):
                                            card = central['deck'].pop()
                                            central['active'].append(card)
                                        else:
                                            central['activeSize'] = central['activeSize'] - 1
                                        break;
                                bought = True
                        if not bought:
                            # If none of the cards are bought from the central area then the supplement section is checked
                            # cards are bought.
                            for counter in range (0, len(central['supplement'])):
                                if playerComputer.getMoney() >= central['supplement'][counter].getCost():
                                    playerComputer.setMoney(playerComputer.getMoney() - central['supplement'][counter].getCost())
                                    playerComputer.setDiscard(central['supplement'][counter])
                                    central['supplement'].pop()
                                    bought = True
                                    break;
                        if not bought:
                            break;

                # At the end of turn for the computer, all the cards in the computer's hand and active area
                # are removed and shifted to the discard pile and the hand area is again replenished by cards
                # from the player's deck.
                setDiscardAtEOT(playerComputer)
                playerComputer.setHand()
                print "Computer turn ending"
                print "------------------------------------------------------------------"
