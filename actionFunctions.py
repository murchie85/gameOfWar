# IMPORT UNIVERSAL UTILITIES
from conquest_utilities import slow_print as slow_print
from conquest_utilities import med_print as med_print
from conquest_utilities import fast_print as fast_print
from conquest_utilities import superfast_print as superfast_print
from conquest_utilities import clearScreen as clearScreen
from conquest_utilities import preferencePrint as preferencePrint
from conquest_utilities import options as options
from conquest_utilities import music as music

import sys
import time
import copy
import random




def action(index, currentNation,NATION_ARRAY,p,myNationIndex,PRICE_TRACKER):
	
	# PROCESS PASS
	for nextMove in currentNation[0]['Nextmoves']:
		preferencePrint(str(''),p,index,myNationIndex)
		if 'pass' in nextMove:
			preferencePrint(str(str(currentNation[1]) + ' chose to pass'),p,index,myNationIndex)
			
		
		# PROCESS GAMBLE 
		if 'gamble' in nextMove:
			preferencePrint('',p,index,myNationIndex)
			preferencePrint(str(str(currentNation[1]) + ' chose to gamble'),p,index,myNationIndex)
			amount = nextMove[1] # the amount chosen to gamble
			originalFinanceScore = currentNation[0]['Finance']['wealth'] + amount
			winnings = random.randint((round(0.3*amount)), round(2*amount)) 

			NATION_ARRAY[index][0]['Finance']['wealth'] = NATION_ARRAY[index][0]['Finance']['wealth'] + winnings

			difference = NATION_ARRAY[index][0]['Finance']['wealth'] - originalFinanceScore  

			if difference > 0:
				preferencePrint(str(str(currentNation[1]) + ' gained  +' + str(difference)),p,index,myNationIndex)
			elif difference < 0:
				preferencePrint(str(str(currentNation[1]) + ' lost  ' + str(difference)),p,index,myNationIndex)
			else:
				preferencePrint(str(str(currentNation[1]) + ' broke even  ' + str(difference)),p,index,myNationIndex)

			preferencePrint(str('Gambled         : ' + str(amount)),p,index,myNationIndex)
			preferencePrint(str('Winnings        : ' + str(winnings)),p,index,myNationIndex)
			preferencePrint(str('Finance credits : ' + str(NATION_ARRAY[index][0]['Finance']['wealth'] )),p,index,myNationIndex)

		if 'buy' in nextMove:
			commodity = nextMove[1]
			amount    = nextMove[2]
			cost      = amount * PRICE_TRACKER[commodity]['price']

			preferencePrint(str(str(currentNation[1]) + ' credits: ' + str(currentNation[0]['Finance']['wealth'])),p,index,myNationIndex)
			preferencePrint(str(str(currentNation[1]) + ' ' + str(commodity) + ' : ' + str(currentNation[0]['Finance'][commodity])),p,index,myNationIndex)
			preferencePrint(str(str(currentNation[1]) + ' chose to buy ' + str(amount) + ' ' + str(commodity) + ' at a cost of ' + str(cost)),p,index,myNationIndex)

			# Reduce stock and deliver goods to user
			PRICE_TRACKER[commodity]['stock'] = PRICE_TRACKER[commodity]['stock'] - amount
			NATION_ARRAY[index][0]['Finance'][commodity] = NATION_ARRAY[index][0]['Finance'][commodity] + amount
			preferencePrint(str(str(currentNation[1]) + ' now has ' + str(NATION_ARRAY[index][0]['Finance'][commodity]) + ' ' + str(commodity)),p,index,myNationIndex)



		if 'sell' in nextMove:
			commodity = nextMove[1]
			amount    = nextMove[2]
			value    = nextMove[3]
			preferencePrint(str(str(currentNation[1]) + ' chose to sell ' + str(amount) + ' ' + str(commodity )),p,index,myNationIndex)

			# Increase stock and credit user

			PRICE_TRACKER[commodity]['stock'] = PRICE_TRACKER[commodity]['stock'] + amount
			NATION_ARRAY[index][0]['Finance']['wealth'] = NATION_ARRAY[index][0]['Finance']['wealth'] + value
			preferencePrint(str(str(currentNation[1]) + ' was paid ' + str(value)),p,index,myNationIndex)

	return(NATION_ARRAY,PRICE_TRACKER)
		
 


def aiBuy(PRICE_TRACKER,currentNation,name):
	commodity    = name
	price        = PRICE_TRACKER[commodity]['price']
	credits      = currentNation[0]['Finance']['wealth']
	aggression   = (currentNation[0]['Special']['agression'] / 100)
	maxpurchase = int(credits // price)

	compensatedMax = round(aggression * maxpurchase)
	if compensatedMax < 1:
		currentNation[0]['Nextmoves']= [['pass']]
		return(currentNation)

	purchaseAmount = random.randint(1, compensatedMax)
	cost = purchaseAmount * price

	# Deduct cost & Place Order 
	currentNation[0]['Finance']['wealth'] = currentNation[0]['Finance']['wealth'] - cost
	currentNation[0]['Nextmoves'] = currentNation[0]['Nextmoves'] + [['buy',commodity, purchaseAmount]]

	return(currentNation)


def setAIMoves(index,currentNation,PRICE_TRACKER):

	# Capping AI at one for now 
	moveLimit = str(currentNation[0]['Special']['moveLimit'])
	aggression   = currentNation[0]['Special']['agression']
	innovation   = currentNation[0]['Special']['innovation']
	materialism  = currentNation[0]['Special']['materialism']
	prudence     = currentNation[0]['Special']['prudence']
	moveLimit = 1


	for moveNumber in range(0, moveLimit):

		# GAMBLE
		gambleAction = random.randint(0,6)
		if gambleAction > 2:
			creditsAvailable = int(currentNation[0]['Finance']['wealth'])

			if creditsAvailable > 1:
				amount = random.randint(1,creditsAvailable)
				currentNation[0]['Finance']['wealth'] = currentNation[0]['Finance']['wealth'] - amount
				currentNation[0]['Nextmoves']         = currentNation[0]['Nextmoves'] + [['gamble',amount]]

		# BUY IF 
		buyProbability = (materialism / 100 ) * random.randint(0,10)
		if buyProbability > 5:
			commodity = 'gold','gems','raremetals','oil'
			commodity = random.choice(commodity)
			currentNation = aiBuy(PRICE_TRACKER,currentNation, commodity)




	# If No moves, then pass
	if len(currentNation[0]['Nextmoves']) == 0:
		currentNation[0]['Nextmoves']= [['pass']]
		
	return(currentNation)






# TALLY UP SCORES FOR ALL TEAMS 
def tallyScores(NATION_ARRAY):
	for x in range(0, len(NATION_ARRAY)):    
		#SUM UP SUBSCORES
		financeScore = NATION_ARRAY[x][0]['Finance']['wealth']
		techScore = NATION_ARRAY[x][0]['Tech']['level']
		totalSubScores = financeScore + techScore
		NATION_ARRAY[x][0]['Score'] = totalSubScores
	return(NATION_ARRAY)



# DEFAULTS ALL TEAM ACTIONS TO 'PASS'
def defaultNextStep(NATION_ARRAY):
	for x in range(0, len(NATION_ARRAY)):    
		NATION_ARRAY[x][0]['Nextmoves'] = []
	return(NATION_ARRAY)



# END OF ROUND 
def nextYear(year,myNation,NATION_ARRAY,myNationIndex,PRICE_TRACKER,p):
	clearScreen()
	fast_print('Processing next year....')
	print('')

	previousPrices = copy.deepcopy (PRICE_TRACKER)

	print('Previous Array is : ' + str(previousPrices))
	# ITERATE FOR EACH TEAM 
	for x in range(0, len(NATION_ARRAY)):
		currentNation = NATION_ARRAY[x]
		index = x

		# AI TEAM DECISION
		if currentNation != myNation: 
			currentNation = setAIMoves(index,currentNation,PRICE_TRACKER) 


		# ACTION CARRIED OUT FOR ALL USERS
		NATION_ARRAY,PRICE_TRACKER = action(index,currentNation,NATION_ARRAY,p,myNationIndex,PRICE_TRACKER)

	# Only talling scores at the end....may need to change
	print('Tallying scores')
	NATION_ARRAY = tallyScores(NATION_ARRAY)
	NATION_ARRAY = defaultNextStep(NATION_ARRAY)


	# Price changes based upon amount of market stock 
	print(previousPrices)
	for item, key in PRICE_TRACKER.items():
		original = previousPrices[item]['stock']
		new = key['stock']
		difference =  (new-original)/original 
		difference = difference + (difference * (1/random.randint(8,12)))
		PRICE_TRACKER[item]['priceChange'] = -(round(PRICE_TRACKER[item]['price'] * difference))
		if new > original:
			PRICE_TRACKER[item]['price'] = round(PRICE_TRACKER[item]['price']  - (PRICE_TRACKER[item]['price'] * difference)) 
		if new < original:
			difference = - difference
			PRICE_TRACKER[item]['price'] = round(PRICE_TRACKER[item]['price']  + (PRICE_TRACKER[item]['price'] * difference))  
    
	input(PRICE_TRACKER)


	print('FUNCTION TO CHECK WHEN STOCK IS 10% AND PUT ALERTS')


	year = year + 1
	print('*Hint* You can change how much you see in the options menu')
	print('')
	print('')
	buffer = input('Press enter to continue \n')
	return(year, NATION_ARRAY,PRICE_TRACKER)
	


