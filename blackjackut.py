import blackjack

def Test20PointsInPlayersHands():
	pc = 20
	numPAces = 0
	dc = 10
	numDAces = 0
	print "Player hand is {0} and has {1} Aces.".format(pc, numPAces)
	print "Dealer hand is {0} and has {1} Aces.".format(dc, numDAces)
	print "Evaluating move for Player"
	util,move = blackjack.Eval_State(pc, dc, "player", 1, numPAces,numDAces,0)
	print "Best move for player is to {0}".format(move)
	if (move == "stand"):
		print "Test Passed"
	else:
		print "Test Failed"

def TestPlayerHasFixed(pcParam):
	pc = pcParam
	numPAces = 0
	numDAces = 0

	print "no aces"	
	for dc in range (2, 11):
		print "Player hand is {0} and has {1} Aces.".format(pc, numPAces)
		print "Dealer hand is {0} and has {1} Aces.".format(dc, numDAces)
		print "Evaluating move for Player"
		util, move = blackjack.Eval_State(pc, dc, "player",1,numPAces,numDAces,0)
		print "Best move for player is to {0}".format(move)

	print "player has an ace"
	pc = pcParam
	numPAces = 1
	numDAces = 0
	for dc in range (2, 11):
		print "Player hand is {0} and has {1} Aces.".format(pc, numPAces)
		print "Dealer hand is {0} and has {1} Aces.".format(dc, numDAces)
		print "Evaluating move for Player"
		util, move = blackjack.Eval_State(pc, dc, "player",1,numPAces,numDAces,0)
		print "Best move for player is to {0}".format(move)

	print "dealer has an ace"
	pc = pcParam
	numPAces = 0	
	numDAces = 1
	for dc in range (2, 11):
		print "Player hand is {0} and has {1} Aces.".format(pc, numPAces)
		print "Dealer hand is {0} and has {1} Aces.".format(dc, numDAces)
		print "Evaluating move for Player"
		util, move = blackjack.Eval_State(pc, dc, "player",1,numPAces,numDAces,0)
		print "Best move for player is to {0}".format(move)

def test_base():
	print "starting tests"
	TestPlayerHasFixed(9)

test_base()

