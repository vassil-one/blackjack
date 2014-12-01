import blackjack

def Test20PointsInPlayersHands():
	pc = 20
	numPAces = 0
	dc = 10
	numDAces = 0
	return pc, dc, 0, 0

def main():

	pc, numPAces = blackjack.DealPlayer()
	dc, numDAces = blackjack.DealDealer()
	print "Player hand is {0} and has {1} Aces.".format(pc, numPAces)
	print "Dealer hand is {0} and has {1} Aces.".format(dc, numDAces)
	print "Evaluating move for Player"
	util,move = blackjack.Eval_State(pc, dc, "player", 1, numPAces,numDAces,0)
	print "Best move for player is to {0}".format(move)

main()