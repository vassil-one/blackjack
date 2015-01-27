import sys,blackjack

def PlayHand(pc, numPAces, dc, numDAces,dbgLevel):
	blackjack.SetDebugLevel(dbgLevel)
	print "Debug Target Level is now: {0}".format(blackjack.GetDebugLevel())
	blackjack.PrintCardProbability()
	print "Player hand is {0} and has {1} Aces.".format(pc, numPAces)
	print "Dealer hand is {0} and has {1} Aces.".format(dc, numDAces)
	print "Evaluating move for Player"
	util,move = blackjack.Eval_State(pc, dc, "player", 1, numPAces,numDAces,0)
	print "Best move for player is to {0} with utility {1}".format(move, util)

def test_base(argv):

	dbgLevel = int(argv[1])
	PlayHand(12,0,6,0,dbgLevel)
	
test_base(sys.argv)