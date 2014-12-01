import random

def CardValue(cardIndex):
	if (cardIndex == 1):
	    return 11;
	if (cardIndex > 1) and (cardIndex < 11):
		return cardIndex;
	if (cardIndex >= 11):
		return 10;

def GetCardSymbol(cardIndex):
	if (cardIndex > 1) and (cardIndex < 11):
		return "{0}".format(cardIndex)
	elif (cardIndex == 1):
		return "A"
	elif (cardIndex == 11):
		return "J"
	elif (cardIndex == 12):
		return "Q"
	elif (cardIndex == 13):
		return "K"

def DealCards(numCards,playerName):
	numAces = 0
	cardSum = 0
	for i in range(0,numCards):
		cardIndex = random.randint(1,13)
		print "Picked {0} for {1}".format(GetCardSymbol(cardIndex), playerName)
		if (cardIndex == 1):
			numAces = numAces + 1
		cardSum += CardValue(cardIndex)
	return cardSum, numAces

def DealPlayer():
	return DealCards(2,"player")

def DealDealer():
	return DealCards(1,"dealer")

def Eval_State():
	

def main():
	pc,numPAces = DealPlayer()
	dc,numDAces = DealDealer()
	reward = 1
	print "Player hand is {0} and has {1} Aces.".format(pc, numPAces)
	print "Dealer hand is {0} and has {1} Aces.".format(dc, numDAces)


main()