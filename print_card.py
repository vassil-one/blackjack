import blackjack

def isAce(cardIndex):
	if (cardIndex == 1):
		return 1
	return 0

def main():
	for card1 in range(1,14):
		for card2 in range(1,14):			
			print "Player Hand {0},{1}".format(blackjack.GetCardSymbol(card1), blackjack.GetCardSymbol(card2))
			for dealer_card in range(1,14):
				numPAces = isAce(card1) + isAce(card2)
				numDAces = isAce(dealer_card)
				pc = blackjack.CardValue(card1) + blackjack.CardValue(card2)
				dc = blackjack.CardValue(dealer_card)
				# print "Player hand is {0} and has {1} Aces.".format(pc, numPAces)
				# print "Dealer hand is {0} and has {1} Aces.".format(dc, numDAces)
				# print "Evaluating move for Player"
				util,move = blackjack.Eval_State(pc, dc, "player", 1, numPAces,numDAces,0)
				print "{0:7}={1:6}, ".format(move, util)
			print "\n"

main()