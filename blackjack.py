import random

debug = 1
probCard = 1/ float(13);
Reward = 1

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

def Eval_State(pc, dc, side, reward, numPAces, numDAces, level):
	if (side == "player"):
		if ((pc - (numPAces * 10)) > 21):
			return -reward, "stand"
		else:
			S_val = 0
			S_max_val = -1000
			for i in range(1, numPAces+1):
				S_val, move = Eval_State(pc - (i * 10), dc, "dealer", reward,numPAces-i,numDAces,level+1)
				if (S_val >= S_max_val):
					S_max_val = S_val
			S_val = S_max_val

			H_val = 0
			for i in range (1,14):
				H_val_current, move = Eval_State(pc + CardValue(i), dc, "player", Reward, numPAces+(i==1), numDAces,level+1)
				H_val_current = probCard * float(H_val_current)
				H_val = H_val + H_val_current

			if (level < 2):
				print "for cards: player hand: {0} player aces {1} dealer hand {2} dealer aces {3}".format(pc, numPAces, dc, numDAces)
				print "utility of stand: {0} ".format(S_val)
				print "utility of all hits: {0}".format(H_val)

			if (S_val > H_val):
				return S_val, "stand"
			else:
				return H_val,"hit"

	elif(side == "dealer"):

		if ((dc > 21) and (numDAces > 0)):
			dc = dc - 10
			numDAces = numDAces - 1
		if (dc > 21):
			return reward, "stand"
		if (dc >= 17):
			if (pc > dc): return reward, "stand"
			if (pc < dc): return -reward, "stand"
			if (pc == dc): return 0 ,"stand"
		else:
			H_val = 0
			for i in range(1,14):
				H_val_current, move = Eval_State(pc, dc+CardValue(i), "dealer", reward, numPAces, numDAces+(i==1),level+1)
				H_val_current = probCard * float(H_val_current)
				H_val = H_val + H_val_current
		return H_val, "hit"
	print "Invalid code path"

def PrintDebugString(str):
	if (debug == 1):
		print str

def Test20PointsInPlayersHands():
	pc = 20
	numPAces = 0
	dc = 10
	numDAces = 0
	return pc, dc, 0, 0

def main():
	PrintDebugString("Initializing game...")
	PrintDebugString("Probability of each card value is {0}".format(probCard))
	pc, dc, numPAces, numDAces = Test20PointsInPlayersHands()
	print "Player hand is {0} and has {1} Aces.".format(pc, numPAces)
	print "Dealer hand is {0} and has {1} Aces.".format(dc, numDAces)
	print "Evaluating move for Player"
	util,move = Eval_State(pc, dc, "player",Reward, numPAces,numDAces,0)
	print "Best move for player is to {0}".format(move)

main()