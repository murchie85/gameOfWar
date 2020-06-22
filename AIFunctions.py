import sys
import time
import copy
import random




def aiBuy(PRICE_TRACKER,currentNation,name):
	# decrease wealth
	# submit order
	commodity    = name
	price        = PRICE_TRACKER[commodity]['price']
	credits      = currentNation[0]['Finance']['wealth']
	aggression   = (currentNation[0]['Special']['aggression'] / 100)
	maxpurchase = int(credits // price)

	compensatedMax = round(aggression * maxpurchase)
	if compensatedMax < 1:
		currentNation[0]['Nextmoves'] = currentNation[0]['Nextmoves'] + [['pass']]
		return(currentNation)

	purchaseAmount = random.randint(1, compensatedMax)
	cost = purchaseAmount * price

	# Deduct cost & Place Order 
	currentNation[0]['Finance']['wealth'] = currentNation[0]['Finance']['wealth'] - cost
	currentNation[0]['Nextmoves']        = currentNation[0]['Nextmoves'] + [['buy',commodity, purchaseAmount]]
	return(currentNation)


def aiSell(PRICE_TRACKER,currentNation,name):
	# decrease stock
	# submit order
	commodity    = name
	price        = PRICE_TRACKER[commodity]['price']
	myStock       = currentNation[0]['Finance'][commodity]
	aggression   = (currentNation[0]['Special']['aggression'] / 100)

	compensatedMax = round(aggression * myStock)
	if compensatedMax > myStock or compensatedMax < 1:
		currentNation[0]['Nextmoves']= currentNation[0]['Nextmoves'] + [['pass']]
		return(currentNation)

	# purchase choice
	purchaseAmount = random.randint(1, compensatedMax)
	value = purchaseAmount * price

	# Deduct stock & Place Order 
	currentNation[0]['Finance'][commodity]   = currentNation[0]['Finance'][commodity] - purchaseAmount
	currentNation[0]['Nextmoves']            = currentNation[0]['Nextmoves'] + [['sell',commodity, purchaseAmount, value]]
	return(currentNation)





def setAIMoves(index,currentNation,PRICE_TRACKER):

	# Capping AI at one for now 
	moveLimit    = int(currentNation[0]['Special']['moveLimit'])
	aggression   = currentNation[0]['Special']['aggression']
	creativity   = currentNation[0]['Special']['creativity']
	materialism  = currentNation[0]['Special']['materialism']
	prudence     = currentNation[0]['Special']['prudence']
	wealth       = currentNation[0]['Finance']['wealth'] 



	for moveNumber in range(1, moveLimit):
		#----------
		# FINANCE
		#----------
		wealth       = currentNation[0]['Finance']['wealth']

		financeBias  = materialism + random.randint(0,100)
		warBias      = aggression  + random.randint(0,100)
		#scienceBias  = creativity  + random.randint(0,100)
		#politicsBias = prudence    + random.randint(0,100)
		values = (financeBias,warBias)
		bias = values.index(max(values))



		# HAS FINANCE BIAS
		if bias == 0:

			# GAMBLE
			gambleAction = random.randint(0,6)
			if gambleAction > 2:
				creditsAvailable = int(currentNation[0]['Finance']['wealth'])
				maxSpend = round((int(currentNation[0]['Special']['aggression'])/100) * creditsAvailable)
				if maxSpend > 1:
					amount = random.randint(1,maxSpend)
					currentNation[0]['Finance']['wealth'] = currentNation[0]['Finance']['wealth'] - amount
					currentNation[0]['Nextmoves']         = currentNation[0]['Nextmoves'] + [['gamble',amount]]


			# BUY
			commodity = random.choice(('gold','gems','raremetals','oil'))
			percentageDecrease = ((PRICE_TRACKER[commodity]['average'] - PRICE_TRACKER[commodity]['price'])/PRICE_TRACKER[commodity]['average'])
			# Higher materialism increases buy probability
			if percentageDecrease > 0.80:
				maxBuyProbability = 30
			elif percentageDecrease > 0.50:
				maxBuyProbability = 20
			elif percentageDecrease > 0.20:
				maxBuyProbability = 15
			else:
				maxBuyProbability = 10

			buyProbability =  (materialism / 100 ) * random.randint(0,maxBuyProbability)
			if buyProbability > 1:
				currentNation = aiBuy(PRICE_TRACKER,currentNation, commodity)



			# SELL
			commodity = random.choice(('gold','gems','raremetals','oil'))
			percentageIncrease = ((PRICE_TRACKER[commodity]['price'] - PRICE_TRACKER[commodity]['average'])/PRICE_TRACKER[commodity]['average'])
			if percentageIncrease > 0.80:
				maxSellProbabiliy = 30
			elif percentageIncrease > 0.50:
				maxSellProbabiliy = 20
			elif percentageIncrease > 0.20:
				maxSellProbabiliy = 15
			else:
				maxSellProbabiliy = 10

		# HAS WAR BIAS
		if bias == 1:
			troops     = currentNation[0]['War']['weapons']['troops']
			tanks      = currentNation[0]['War']['weapons']['tanks']
			army       = troops + tanks
			gunboats   = currentNation[0]['War']['weapons']['gunboats']
			destroyers = currentNation[0]['War']['weapons']['destroyers']
			carriers   = currentNation[0]['War']['weapons']['carriers']
			navy       = gunboats + destroyers + carriers
			jets       = currentNation[0]['War']['weapons']['jets']
			bombers    = currentNation[0]['War']['weapons']['bombers']
			airforce   = jets + bombers
			nukes      = currentNation[0]['War']['weapons']['Nukes']
		
			#--------
			# DRILL
			#--------
			# Pick a military branch, save asset details to array, place order 
			branchSelection = []
			if army > 0: 
				branchSelection.append(('army',     ('troops','tanks'),army))
			if navy > 0: 
				branchSelection.append(('navy',     ('gunboats','destroyers','carriers'),navy))
			if airforce > 0: 
				branchSelection.append(('airforce', ('jets','bombers'),airforce))
			if len(branchSelection) ==0:
				currentNation[0]['Nextmoves']= [['pass']]
				break

			branch = random.choice(branchSelection)
			#print(branch)
			units = []

			#filling an array to say what units and how many belong to this branch 
			for asset in branch[1]:
				package = (str(asset),currentNation[0]['War']['weapons'][asset])
				units.append(package)

			exposure = random.choice(('soft','medium','hard'))
			drillOrder = ['drill',branch[0],exposure, units]
			#print(str(currentNation[1]) + ' order ' + str(drillOrder))
			# Deduct units
			for unit in units:
				currentNation[0]['War']['weapons'][unit] = 0
			# Place Order
			currentNation[0]['Nextmoves'] = currentNation[0]['Nextmoves'] + [drillOrder]

	# If No moves, then pass
	if len(currentNation[0]['Nextmoves']) == 0:
		currentNation[0]['Nextmoves']= [['pass']]
		
	return(currentNation)



