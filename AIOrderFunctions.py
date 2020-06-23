import sys
import time
import copy
import random


# TO DO ------



# Need to make buying more sophisticated rather than chosing a random commodity
# Remember to deduct might from hard drill
# Buffer drill by tech level 

def setAIMoves(index,currentNation,PRICE_TRACKER,WAR_BRIEFING,NATION_ARRAY):

	# Capping AI at one for now 
	moveLimit    = int(currentNation[0]['Special']['moveLimit'])
	aggression   = currentNation[0]['Special']['aggression']
	creativity   = currentNation[0]['Special']['creativity']
	materialism  = currentNation[0]['Special']['materialism']
	prudence     = currentNation[0]['Special']['prudence']
	wealth       = currentNation[0]['Finance']['wealth'] 
	wealthArray = []



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
			currentNation = drill(currentNation,army,navy,airforce)

			#--------
			# BUILD
			#--------
			# The more aggressive and materialistic...
			buildBias = 1
			if (aggression + materialism) > 150:
				buildBias = 2
			elif (aggression + materialism) > 100:
				buildBias = 3
			elif (aggression + materialism) > 75:
				buildBias = 4
			else:
				buildBias = 10
			buildProbability = random.randint(0, buildBias)
			if buildProbability == 1:
				currentNation = build(currentNation,WAR_BRIEFING)
			#--------
			# SCRAP
			# 25% chance to scrap if poor, 10% otherwise 
			#--------
			scrapProbability = 10
			# Check to see if current country is poorer than 80% of average
			for country in NATION_ARRAY: wealthArray.append(country[0]['Finance']['wealth'])
			averageWealth = round((sum(wealthArray)/len(wealthArray)))
			poor          = 0.8*averageWealth
			if wealth < poor: scrapProbability = 3

			if random.randint(0,scrapProbability) == 2:
				scrap(currentNation,WAR_BRIEFING)


	# If No moves, then pass
	if len(currentNation[0]['Nextmoves']) == 0:
		currentNation[0]['Nextmoves']= [['pass']]
		
	return(currentNation)





def build(currentNation,WAR_BRIEFING):

	wealth               = currentNation[0]['Finance']['wealth'] 
	aggressionAdjusted   = (currentNation[0]['Special']['aggression']) / 100
	techLevel            = currentNation[0]['Tech']['level']

	allowedAssets = []
	allowedAssets = allowedTech(techLevel)
	unit = random.choice(allowedAssets)

	price      = WAR_BRIEFING['weapons'][unit][0]
	wait       = WAR_BRIEFING['weapons'][unit][1]
	bonusMight = WAR_BRIEFING['weapons'][unit][2]

	maxpurchase = int(wealth // price)
	adjusted    = round((aggressionAdjusted * maxpurchase))

	if adjusted > 0:
		maxBuy = round(random.randint(adjusted, maxpurchase))
	else:
		maxBuy = round(random.randint(0,maxpurchase))
	


	# If they can't afford even one  
	if maxBuy < 1:
		print('cant afford')
		return(currentNation)

	purchaseAmount = random.randint(1,maxBuy)
	cost = purchaseAmount * price

	# Deduct cost & Place Order 
	currentNation[0]['Finance']['wealth'] = currentNation[0]['Finance']['wealth'] - cost
	currentNation[0]['Nextmoves'] = currentNation[0]['Nextmoves'] + [['submitted','WeaponsBuild',unit, purchaseAmount,wait,bonusMight]]
	return(currentNation)



def scrap(currentNation,WAR_BRIEFING):
	wealth               = currentNation[0]['Finance']['wealth'] 
	aggressionAdjusted   = (currentNation[0]['Special']['aggression']) / 100
	techLevel            = currentNation[0]['Tech']['level']


	allowedAssets = []
	allowedAssets = allowedTech(techLevel)
	unit = random.choice(allowedAssets)

	print(str(currentNation[1] + '** SCRAPPING**	'))
	print('unit: ' + str(unit))
	print('tech level ' + str(techLevel))
	print('agression' + str(aggressionAdjusted))

	price        = WAR_BRIEFING['weapons'][unit][0]
	reducedMight = WAR_BRIEFING['weapons'][unit][2]
	stock        = currentNation[0]['War']['weapons'][unit]
	adjusted    = round((aggressionAdjusted * stock))
	maxScrap    = round(random.randint(adjusted, stock))

	if stock < 0 or maxScrap < 0:
		print('none to scrap')
		print('stock :' + str(stock))
		print('maxscrap: ' + str(maxscrap))
		return(currentNation)

	scrapAmount = random.randint(1,maxScrap)
	valuation   = scrapAmount * price

	# Deducts units and places order 
	currentNation[0]['War']['weapons'][unit] = currentNation[0]['War']['weapons'][unit] - scrapAmount
	currentNation[0]['Nextmoves']            = currentNation[0]['Nextmoves'] + [['WeaponsScrap',unit, scrapAmount,valuation,reducedMight]]
	return(currentNation)


def allowedTech(techLevel):
	if techLevel == 0:
		allowedAssets = ['troops']
	if techLevel > 1:
		allowedAssets = ['troops','tanks']
	if techLevel > 2:
		allowedAssets = ['troops','tanks','gunboats']
	if techLevel > 3:
		allowedAssets = ['troops','tanks','gunboats','destroyers']
	if techLevel > 5:
		allowedAssets = ['troops','tanks','gunboats','destroyers','jets']
	if techLevel > 7:
		allowedAssets = ['troops','tanks','gunboats','destroyers','jets','bombers']
	if techLevel > 8:
		allowedAssets = ['troops','tanks','gunboats','destroyers','jets','bombers','carriers']
	if techLevel > 9:
		allowedAssets = ['troops','tanks','gunboats','destroyers','jets','bombers','carriers','Nukes']

	return(allowedAssets)







def drill(currentNation,army,navy,airforce):
	branchSelection = []
	if army > 0: 
		branchSelection.append(('army',     ('troops','tanks'),army))
	if navy > 0: 
		branchSelection.append(('navy',     ('gunboats','destroyers','carriers'),navy))
	if airforce > 0: 
		branchSelection.append(('airforce', ('jets','bombers'),airforce))
	if len(branchSelection) ==0:
		currentNation[0]['Nextmoves']= [['pass']]
		print('failed to drill')
		return(currentNation)

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
	return(currentNation)


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





