import random

debug = 0
probCard = 1/ float(13);

def PrintDebugString(str):
	if (debug == 1):
		print str

def CardValue(cardIndex):
	if (cardIndex == 1):
	    return 11;
	elif (cardIndex > 1) and (cardIndex < 11):
		return cardIndex;
	elif (cardIndex >= 11):
		return 10;
	else:
		print "fun:CardValue() Error, invalid card index {0}".format(cardIndex)

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
	else:
		print "fun:GetCardSymbol() Error, invalid card index {0}".format(cardIndex)

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
			for i in range(0, numPAces+1):
				S_val_current, move = Eval_State(pc - (i * 10), dc, "dealer", reward,numPAces-i,numDAces,level+1)
				S_val = S_val_current + S_val

			H_val = 0
			# Number cards A,2,3,4,5,6,7,8,9
			for i in range (1,10):
				H_val_current, move = Eval_State(pc + CardValue(i), dc, "player", reward, numPAces+(i==1), numDAces,level+1)
				PDSAtLevel("Level {4}:  Player hand: {0} ({1} Aces)  Dealer hand: {2} dealer ({3} Aces)".format(pc, numPAces, dc, numDAces, level),level,1)				
				PDSAtLevel("H_val for card {0} is {1}.".format(GetCardSymbol(i),H_val_current),level,1)
				H_val_current = probCard * float(H_val_current)
				H_val = H_val + H_val_current

			# Face cards and 10 - J,Q,K,10
			H_val_current, move = Eval_State(pc + CardValue(10), dc, "player", reward, numPAces, numDAces,level+1)
			H_val_current = 4 * probCard * float(H_val_current)
			H_val = H_val + H_val_current

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
			for i in range(1,10):
				H_val_current, move = Eval_State(pc, dc+CardValue(i), "dealer", reward, numPAces, numDAces+(i==1),level+1)
				H_val_current = probCard * float(H_val_current)
				H_val = H_val + H_val_current
			H_val_current, move = Eval_State(pc, dc+CardValue(10), "dealer", reward, numPAces, numDAces, level+1)
			H_val_current = 4 * probCard * float(H_val_current)
			H_val = H_val + H_val_current
			return H_val, "hit"			
		return "Invalid code path"
	print "Invalid code path"

def PDSAtLevel(str, curr_level, target_level):
	if (debug == 1):
		if (curr_level == target_level):
			print str