# This is the compilation of all unit tests for the Card Building Deck Game
from dbc import *
import unittest

class DBCTest (unittest.TestCase):
    
    def test01_InitialiseCentralActiveArea(self):
        """
        To check whether the Central Active area is being initialised
        correctly or not
        """
        
        print "========================================================================================================"
        print "Test 01: This will check whether the Central Active Area of the game is initialised at the start or not."
        initialiseCentralActiveArea(central)
        deckSize = len(central['deck'])
        self.assertEqual(deckSize, 31)
        activeSize = len(central['active'])
        self.assertEqual(activeSize, 5)
        print "Test 01 completed"
        print "========================================================================================================"
    
    def test02_SameInitialPlayerCondition(self):
        """
        To check whether the initial player conditions and values
        are set to be the same or not.
        """

        print "Test 02: This will check whether the initial player parameters are set for both players or not."
        self.assertEqual(player.getMoney(), opponent.getMoney())
        self.assertEqual(player.getAttack(), opponent.getAttack())
        self.assertEqual(player.getHealth(), opponent.getHealth())
        self.assertEqual(player.getDeck(), opponent.getDeck())
        print "Test 02 completed"
        print "========================================================================================================"

    def test03_PlayAllCards(self):
        """
        To check whether the player's active area is filled with exactly
        the number of cards which is the maximum hand size for a player,
        when the Play All Cards option is selected.
        Also whether the wealth and attack power are correctl being updated
        is checked
        """

        print "Test 03: This will check whether all the card slots present in the player's active area will be \nfilled with cards when the \"Play All\" option is selected by the player."
        playAllCards(player)
        length = len(player.getActive())
        self.assertEqual(length, 5)
        self.assertEqual(player.getMoney(), 3)
        self.assertEqual(player.getAttack(), 2)
        print "Test 03 completed"
        print "========================================================================================================"

    def test04_ReduceOpponentHealth(self):
        """
        To check whether the opponent's health is reduced correctly on attack.
        """

        print "Test 04: This will check whether the opponent's health is correctly reduced or not when the player \nselects the \"Attack\" option."
        reduceOpponentHealth(player, opponent)
        opponentHealth = opponent.getHealth()
        self.assertEqual(opponentHealth, 28)
        print "Test 04 completed"
        print "========================================================================================================"

    def test05_DiscardAtEOT(self):
        """
        To check whether at end of turn of a player, all cards from the player's hand
        and active area are shifted to the discard pile or not.
        """
        
        print "Test 05: This will check whether all cards in the player's Hand and Active area are removed and \nappended in the discard pile or not when a player chooses the \"End Turn\" option."
        player.setHand()
        setDiscardAtEOT(player)
        handSize = len(player.getHand())
        activeSize = len(player.getActive())
        discardSize = len(player.getDiscard())
        self.assertEqual(handSize, 0)
        self.assertEqual(activeSize, 0)
        self.assertEqual(discardSize, 10)
        print "Test 05 completed"
        print "========================================================================================================"

    def test06_BuyCardForPlayer(self):
        """
        To check whether a card when bought by a player, it is added to the player's
        discard pile after being removed from the central active area or not.
        """

        print "Test 06: This will check whether the card that a player chooses to buy is removed from the central \n active area and appended to the player's discard pile of cards or not."
        player.setHand()
        player.setMoney(10);
        card = central['active'][1]
        buyCardForPlayer(player, 1, central['active'], 'central', central)
	poppedCard = player.getDiscard().pop()
        self.assertEqual(card, poppedCard)
        print "Test 06 completed"
        print "========================================================================================================"

    def test07_CheckForResult(self):
        """
        To check whether the game is ended when one of the player's health is reduced to
        zero.
        """

        print "Test 07: This will check whether the game announces the winner and stops further turns of players when \none of the player's health is reduced to 0 or lesser or not."
        player.setHealth(0)
        opponent.setHealth(10)
        result = checkForResult(player, opponent)
        self.assertEqual(result, "end")
        print "Test 07 completed"
        print "========================================================================================================"

if __name__ == '__main__':

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

    # Initialising all player environments. Firstly as all players are initially provided with the same
    # set of cards, the player initial deck is created. Then the Player objects are created. The attributes
    # of the players are intialised. The initial deck is set and the Hand is also set by transferring cards
    # equal to the maximum number of cards which can be placed in the hand area, from the player deck to
    # the hand area.
    playerInitialDeck = [8 * [serf], 2 * [squire]]

    player = Player('Player', playerInitialDeck)
    player.setHand()
    opponent = Player('Opponent', playerInitialDeck)
    opponent.setHand()

    unittest.TestLoader.sortTestMethodsUsing = None
    unittest.main()
