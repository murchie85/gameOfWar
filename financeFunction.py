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



def gambleAction(nextMove,NATION_ARRAY,currentNation,p,index,myNationIndex):
	preferencePrint('',p,index,myNationIndex)
	preferencePrint(str(str(currentNation[1]) + ' chose to gamble'),p,index,myNationIndex)
	preferencePrint('---------------------',p,index,myNationIndex)
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
	return(NATION_ARRAY)


def buyAction(nextMove,NATION_ARRAY,currentNation,PRICE_TRACKER,p,index,myNationIndex):
	commodity = nextMove[1]
	amount    = nextMove[2]
	cost      = amount * PRICE_TRACKER[commodity]['price']

	preferencePrint(str(str(currentNation[1]) + ' chose to buy '),p,index,myNationIndex)
	preferencePrint('------------------',p,index,myNationIndex)
	preferencePrint(str('Credits    : ' + str(currentNation[0]['Finance']['wealth'])),p,index,myNationIndex)
	preferencePrint(str(str(commodity) + ' purchased : ' + str(amount)),p,index,myNationIndex)
	preferencePrint(str('Total Cost :' + str(cost)),p,index,myNationIndex)

	# UPDATE Reduce stock and deliver goods to user
	PRICE_TRACKER[commodity]['stock'] = PRICE_TRACKER[commodity]['stock'] - amount
	NATION_ARRAY[index][0]['Finance'][commodity] = NATION_ARRAY[index][0]['Finance'][commodity] + amount
	preferencePrint(str('New total : ' + str(NATION_ARRAY[index][0]['Finance'][commodity])),p,index,myNationIndex)
	return(NATION_ARRAY,PRICE_TRACKER)

def sellAction(nextMove,NATION_ARRAY,currentNation,PRICE_TRACKER,p,index,myNationIndex):
	commodity = nextMove[1]
	amount    = nextMove[2]
	value     = nextMove[3]
	preferencePrint(str(str(currentNation[1]) + ' chose to sell'),p,index,myNationIndex)
	preferencePrint('------------------',p,index,myNationIndex)
	preferencePrint(str('Credits    : ' + str(currentNation[0]['Finance']['wealth'])),p,index,myNationIndex)
	preferencePrint(str(str(commodity) + ' owned : ' + str(currentNation[0]['Finance'][commodity])),p,index,myNationIndex)
	preferencePrint(str(str(commodity) + ' sold  : ' +  str(amount)),p,index,myNationIndex)
	preferencePrint(str('Credits    : ' + str(currentNation[0]['Finance']['wealth'])),p,index,myNationIndex)
	

	# UPDATE Increase stock and credit user
	PRICE_TRACKER[commodity]['stock'] = PRICE_TRACKER[commodity]['stock'] + amount
	NATION_ARRAY[index][0]['Finance']['wealth'] = NATION_ARRAY[index][0]['Finance']['wealth'] + value
	preferencePrint(str(str(currentNation[1]) + ' was paid ' + str(value)),p,index,myNationIndex)
	return(NATION_ARRAY,PRICE_TRACKER)

def promotion(currentNation,p,index,myNationIndex):
	financeRank = ['PickPocket', 'Penny Pusher', 'Assistant', 'gambler', 'accountant', 'huslter', 'business magnate']
	wealth = currentNation[0]['Finance']['wealth']
	rank   = currentNation[0]['Finance']['level']
	if wealth > 5100 and rank == financeRank[0]:
		currentNation[0]['Finance']['level'] = financeRank[1]
		rank   = currentNation[0]['Finance']['level']
		currentNation[0]['Special']['notes'].append('finance') 
		preferencePrint(str(currentNation[1] ) + ' levelled up! New Finance rank is ' + str(currentNation[0]['Finance']['level']),p,index,myNationIndex)

	if wealth > 10000 and rank == financeRank[1]:
		currentNation[0]['Finance']['level'] = financeRank[2]
		rank   = currentNation[0]['Finance']['level']
		currentNation[0]['Special']['notes'].append('finance') 
		preferencePrint(str(currentNation[1] ) + ' levelled up! New Finance rank is ' + str(currentNation[0]['Finance']['level']),p,index,myNationIndex)

	if wealth > 15000 and rank == financeRank[2]:
		currentNation[0]['Finance']['level'] = financeRank[3]
		rank   = currentNation[0]['Finance']['level']
		currentNation[0]['Special']['notes'].append('finance') 
		preferencePrint(str(currentNation[1] ) + ' levelled up! New Finance rank is ' + str(currentNation[0]['Finance']['level']),p,index,myNationIndex)

	if wealth > 20000 and rank == financeRank[3]:
		currentNation[0]['Finance']['level'] = financeRank[4]
		rank   = currentNation[0]['Finance']['level']
		currentNation[0]['Special']['notes'].append('finance') 
		preferencePrint(str(currentNation[1] ) + ' levelled up! New Finance rank is ' + str(currentNation[0]['Finance']['level']),p,index,myNationIndex)

	if wealth > 30000 and rank == financeRank[4]:
		currentNation[0]['Finance']['level'] = financeRank[5]
		rank   = currentNation[0]['Finance']['level']
		currentNation[0]['Special']['notes'].append('finance') 
		preferencePrint(str(currentNation[1] ) + ' levelled up! New Finance rank is ' + str(currentNation[0]['Finance']['level']),p,index,myNationIndex)

	if wealth > 40000 and rank == financeRank[5]:
		currentNation[0]['Finance']['level'] = financeRank[6]
		rank   = currentNation[0]['Finance']['level']
		currentNation[0]['Special']['notes'].append('finance') 
		preferencePrint('****' +  str(currentNation[1] ) + ' levelled up!***** New Finance rank is ' + str(currentNation[0]['Finance']['level']),p,index,myNationIndex)
	return(currentNation)
