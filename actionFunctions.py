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

import financeFunction as financeFunction
import AIFunctions as AI 




def action(index, currentNation,NATION_ARRAY,p,myNationIndex,PRICE_TRACKER):
	
	# PROCESS PASS
	for nextMove in currentNation[0]['Nextmoves']:
		preferencePrint(str(''),p,index,myNationIndex)
		if 'pass' in nextMove:
			preferencePrint(str(str(currentNation[1]) + ' chose to pass'),p,index,myNationIndex)
			
		if 'gamble' in nextMove:
			NATION_ARRAY = financeFunction.gambleAction(nextMove,NATION_ARRAY,currentNation,p,index,myNationIndex)

		if 'buy' in nextMove:
			NATION_ARRAY,PRICE_TRACKER = financeFunction.buyAction(nextMove,NATION_ARRAY,currentNation,PRICE_TRACKER,p,index,myNationIndex)

		if 'sell' in nextMove:
			NATION_ARRAY,PRICE_TRACKER = financeFunction.sellAction(nextMove,NATION_ARRAY,currentNation,PRICE_TRACKER,p,index,myNationIndex)

	return(NATION_ARRAY,PRICE_TRACKER)
		
 




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

	# ITERATE FOR EACH TEAM 
	for x in range(0, len(NATION_ARRAY)):
		currentNation = NATION_ARRAY[x]
		index = x

		# AI TEAM DECISION
		if currentNation != myNation: 
			currentNation = AI.setAIMoves(index,currentNation,PRICE_TRACKER) 

		# ACTION CARRIED OUT FOR ALL USERS
		NATION_ARRAY,PRICE_TRACKER = action(index,currentNation,NATION_ARRAY,p,myNationIndex,PRICE_TRACKER)


		# FINANCE PROMOTION
		currentNation = financeFunction.promotion(currentNation,p,index,myNationIndex)

	# Only talling scores at the end....may need to change
	print('Tallying scores')
	NATION_ARRAY = tallyScores(NATION_ARRAY)
	NATION_ARRAY = defaultNextStep(NATION_ARRAY)


	# UPDATE PRICE 
	for item, key in PRICE_TRACKER.items():
		original = previousPrices[item]['stock']
		new = key['stock']
		difference =  (new-original)/original
		volitility =  80
		difference = difference + (difference * (random.randint(10,volitility))) # inflation
		PRICE_TRACKER[item]['priceChange'] = -(round(PRICE_TRACKER[item]['price'] * difference))
		if PRICE_TRACKER[item]['priceChange'] > -1:
			PRICE_TRACKER[item]['priceChange'] = '+' + str(PRICE_TRACKER[item]['priceChange'])
		else:
			PRICE_TRACKER[item]['priceChange'] = str(PRICE_TRACKER[item]['priceChange'])


		if new > original:
			PRICE_TRACKER[item]['price'] = round(PRICE_TRACKER[item]['price']  - (PRICE_TRACKER[item]['price'] * difference)) 
		if new < original:
			difference = - difference
			PRICE_TRACKER[item]['price'] = round(PRICE_TRACKER[item]['price']  + (PRICE_TRACKER[item]['price'] * difference))  
   	
	# UPDATE HISTORY AND AVERAGE
	for item in PRICE_TRACKER:
		PRICE_TRACKER[item]['history'].append(PRICE_TRACKER[item]['price'])
		average = round(sum(PRICE_TRACKER[item]['history']) / len(PRICE_TRACKER[item]['history']))
		if PRICE_TRACKER[item]['average'] ==0: PRICE_TRACKER[item]['average'] = 1
		PRICE_TRACKER[item]['average'] = average



	# MENU
	hintSwitch = 'off'
	if myNation[0]['hints'] == 'on':
		hintSwitch = 'off'
	else: hintSwitch = 'on'

	choice = 'x'
	while choice != 'xnsdfaoiga':
		print('')
		print('----Processing Complete----')
		print('[1] View prices')
		print('[2] View Previous Prices')
		print('[3] Print Json (for developers)')
		print('[4] Switch hints ' + str(hintSwitch))
		print('[5] Change Next Year Updates')
		print('[x] Skip')
		choice = str(input('Press enter to skip \n'))
		if choice == '1':
			clearScreen()
			for item in PRICE_TRACKER:
				print('*****' + str(item) + '*******')
				print('Price          : ' + str(PRICE_TRACKER[item]['price']))
				print('Market Stock   : ' + str(PRICE_TRACKER[item]['stock']))
				print('Price Change   : ' + str(PRICE_TRACKER[item]['priceChange']))
				print('Average        : ' + str(PRICE_TRACKER[item]['average']))
			print(" ")
			input('Press enter to continue \n')
		if choice == '2':
			clearScreen()
			for item in previousPrices:
				print('*****' + str(item) + '*******')
				print('Price          : ' + str(previousPrices[item]['price']))
				print('Market Stock   : ' + str(previousPrices[item]['stock']))
				print('Price Change   : ' + str(previousPrices[item]['priceChange']))
				print('Average        : ' + str(previousPrices[item]['priceChange']))
			print(" ")
			input('Press enter to continue \n')
		if choice == '3':
			clearScreen()
			print(previousPrices)
			print(PRICE_TRACKER)
			input('Press enter to continue \n')
		if choice == '4':
			myNation[0]['hints'] = hintSwitch
			if hintSwitch == 'off':
				hintSwitch = 'on'
			else: hintSwitch = 'off'
		if choice == '5':
			p = options(p)
		if choice == 'x' or choice =='':
			break


	print('FUNCTION TO CHECK WHEN STOCK IS 10% AND PUT ALERTS')

	print(' ')
	year = year + 1
	# lazy coding...
	if hintSwitch == 'off':
		hints = ['****Hint**** \n You can change what you see in next round updates from the options menu', '****Hint**** \n Pressing enter exits or skips most menu`s or takes you back' ,'****Hint**** \n Resources like gold have a market stock, prices reflect the availability in the market.']
		print(str(random.choice(hints)))

	print('')
	print('')
	buffer = input('Press enter to continue \n')
	return(year, NATION_ARRAY,PRICE_TRACKER, p)
	


