	# All Finance Menu Function

# IMPORT UNIVERSAL UTILITIES
from gameConquest_utilities import preferencePrint as preferencePrint

import sys
import time
import copy
import random

"""

TO DO 

MVP
1. Drill troops Increases might by random small amount
DRILL INCREASE MIGHTINCREASE = RANDOM * LEVEL

ONCE POLITICS IS DONE 

2. Combat Manevres increases might and political will
3. Buy assets (need money and political will)


ONCE TECH IS DONE 

1. Tech level unlocks more items 


"""


P = 'All'

# Takes the build order placed by currentNation
# Awards the unit
# Awards might proportional to mightvalue x totalMight X 1/2 the number of units ordered
# This scales the more you buy and type you buy

def build(nextMove,NATION_ARRAY,currentNation,p,index,myNationIndex):
	pending    = nextMove[0]
	job        = nextMove[1]
	unit       = nextMove[2]
	amount     = nextMove[3]
	wait       = nextMove[4]
	bonusMight = nextMove[5]

	preferencePrint(str(str(currentNation[1]) + ' chose to build '),p,index,myNationIndex)
	preferencePrint('------------------',p,index,myNationIndex)
	preferencePrint(str(str(unit) + ' to build : ' + str(amount)),p,index,myNationIndex)

	# IF NOT YET READY
	# DECREMENT BUILD TIME 
	if wait > 1:
		wait = wait -1
		preferencePrint(str('Build Time Remaining : ' + str(wait)),p,index,myNationIndex)
		# Get position in country array 
		for x in range(0, len(currentNation[0]['Nextmoves'])):
			if  nextMove == currentNation[0]['Nextmoves'][x]: moveIndex = x
	
		nextMove = ['pending',job,unit,amount,wait,bonusMight]
		NATION_ARRAY[index][0]['Nextmoves'][moveIndex] = nextMove
		return(NATION_ARRAY)

	# IF READY
	if wait < 2:
		# Reward Unit
		NATION_ARRAY[index][0]['War']['weapons'][unit] = NATION_ARRAY[index][0]['War']['weapons'][unit]  + amount
		preferencePrint(str(str(unit) + ' total : ' + str(NATION_ARRAY[index][0]['War']['weapons'][unit])),p,index,myNationIndex)
		
		# Reward Mightg
		bonusAdjustment = round((NATION_ARRAY[index][0]['War']['might'] * bonusMight) * (amount/2))
		if bonusAdjustment < 1:
			bonusAdjustment = 1
		NATION_ARRAY[index][0]['War']['might'] = NATION_ARRAY[index][0]['War']['might'] + bonusAdjustment
		preferencePrint(str('Might gained : ' + str(bonusAdjustment)),p,index,myNationIndex)
		preferencePrint(str('Might total  : ' + str(currentNation[0]['War']['might'])),p,index,myNationIndex)

		# Clear out existing array element
		for x in range(0, len(currentNation[0]['Nextmoves'])):
			if  nextMove == currentNation[0]['Nextmoves'][x]: 
				NATION_ARRAY[index][0]['Nextmoves'][x] = []

		return(NATION_ARRAY)

	return(NATION_ARRAY)


# Takes the scrap order placed by currentNation
# Awards money
# Deducts might proportional to mightvalue x totalMight x 1/5 the number of units scrapped

def scrap(nextMove,NATION_ARRAY,currentNation,p,index,myNationIndex):
	job           = nextMove[0]
	unit          = nextMove[1]
	amount        = nextMove[2]
	valuation     = nextMove[3]
	reducedMight  = nextMove[4]

	preferencePrint(str(str(currentNation[1]) + ' chose to scrap'),p,index,myNationIndex)
	preferencePrint('------------------',p,index,myNationIndex)
	preferencePrint(str(str(unit) + ' to scrap : ' + str(amount)),p,index,myNationIndex)

	# Award Credits and reduce might
	NATION_ARRAY[index][0]['Finance']['wealth'] = NATION_ARRAY[index][0]['Finance']['wealth'] + valuation
	Adjustment = round((NATION_ARRAY[index][0]['War']['might'] * reducedMight) * (amount/5))
	NATION_ARRAY[index][0]['War']['might'] = NATION_ARRAY[index][0]['War']['might'] - Adjustment
	
	preferencePrint(str('Might lost    : -' + str(Adjustment)),p,index,myNationIndex)
	preferencePrint(str('Might total   : ' + str(currentNation[0]['War']['might'])),p,index,myNationIndex)
	preferencePrint(str(str(currentNation[1]) + ' was paid ' + str(valuation)),p,index,myNationIndex)
	preferencePrint(str('Credits total : ' + str(currentNation[0]['Finance']['wealth'])),p,index,myNationIndex)
	return(NATION_ARRAY)





def drill(nextMove,NATION_ARRAY,currentNation,p,index,myNationIndex):
	move      = nextMove[0]
	branch    = nextMove[1]
	intensity = nextMove[2]
	units     = nextMove[3]
	might     = NATION_ARRAY[index][0]['War']['might']
	credits   = NATION_ARRAY[index][0]['Finance']['wealth']
	techLevel = NATION_ARRAY[index][0]['Tech']['level']
	#['drill',branch,'soft',units]
	#units = [('troops',troops),('tanks',tanks)]


	# Return Units 
	for unit, quantity in units:
		NATION_ARRAY[index][0]['War']['weapons'][unit] = quantity

	preferencePrint('',p,index,myNationIndex)
	preferencePrint(str(str(currentNation[1]) + ' chose to train their ' + str(branch)),p,index,myNationIndex)
	preferencePrint('================================',p,index,myNationIndex)
	preferencePrint(str('Intensity: ' + str(intensity)),p,index,myNationIndex)

	if intensity == 'soft':
		bonusMight = round((random.randint(1,15) / 100) * might)
		NATION_ARRAY[index][0]['War']['might'] = NATION_ARRAY[index][0]['War']['might']  + bonusMight
		preferencePrint(str('Might gained    : ' + str(bonusMight)),p,index,myNationIndex)
		preferencePrint(str('New Might Total : ' + str(NATION_ARRAY[index][0]['War']['might'])),p,index,myNationIndex)
		return(NATION_ARRAY)

	if intensity == 'medium':
		# WIN MIGTH
		bonusMight = round((random.randint(10,25) / 100) * might)
		NATION_ARRAY[index][0]['War']['might'] = NATION_ARRAY[index][0]['War']['might']  + bonusMight
		
		# WIN CREDITS
		bonusCredits = round((random.randint(1,10) / 100) * credits)
		NATION_ARRAY[index][0]['Finance']['wealth'] = NATION_ARRAY[index][0]['Finance']['wealth']  + bonusCredits
		preferencePrint(str(str(NATION_ARRAY[index][0]) + ' impressed the top leadership and won financial support.'),p,index,myNationIndex)
		preferencePrint(str('Credits gained    : ' + str(NATION_ARRAY[index][0]['Finance']['wealth'])),p,index,myNationIndex)

		# LOSE A PORTION OF UNITS 
		lossProbability = random.randint(0,8)
		lossAmount = 0.25
		if lossProbability == 3:
			for unit, quantity in units:
				original = quantity
				if quantity < 1:
					continue
				if random.randint(0,1) == 1:
					loss = round(quantity * lossAmount)
					if loss == quantity:
						quantity = quantity - 1
					else:
						quantity = round(quantity * (1-lossAmount))
					preferencePrint(str(str(unit) + ' lost in combat excercise '),p,index,myNationIndex)
					preferencePrint(str(str(original - quantity) + ' ' + str(unit) +  ' lost'),p,index,myNationIndex)
					preferencePrint(str(str(quantity) + ' remaining'),p,index,myNationIndex)
				NATION_ARRAY[index][0]['War']['weapons'][unit] = quantity
		preferencePrint(str('Might gained    : ' + str(bonusMight)),p,index,myNationIndex)
		preferencePrint(str('New Might Total : ' + str(NATION_ARRAY[index][0]['War']['might'])),p,index,myNationIndex)
		return(NATION_ARRAY)


	if intensity == 'hard':
		# GAIN MIGHT
		bonusMight = round((random.randint(20,40) / 100) * might)
		NATION_ARRAY[index][0]['War']['might'] = NATION_ARRAY[index][0]['War']['might']  + bonusMight
		# GAIN CREDITS
		bonusCredits = round((random.randint(5,15) / 100) * credits)
		NATION_ARRAY[index][0]['Finance']['wealth'] = NATION_ARRAY[index][0]['Finance']['wealth']  + bonusCredits
		preferencePrint(str('Credits gained    : ' + str(NATION_ARRAY[index][0]['Finance']['wealth'])),p,index,myNationIndex)

		# LOSE A PORTION OF UNITS 
		lossProbability = random.randint(0,4)
		lossAmount = 0.25
		if lossProbability == 3:
			preferencePrint(str('XXXX UNITS LOST IN TRAINING XXXX'),p,index,myNationIndex)
			for unit, quantity in units:
				original = quantity
				if quantity < 1:
					continue
				if random.randint(0,1) == 1:
					loss = round(quantity * lossAmount)
					if loss == quantity:
						quantity = quantity - 1
					else:
						quantity = round(quantity * (1-lossAmount))
					preferencePrint(str(str(unit) + ' lost in combat excercise '),p,index,myNationIndex)
					preferencePrint(str(str(original - quantity) + ' ' + str(unit) +  ' lost'),p,index,myNationIndex)
					preferencePrint(str(str(quantity) + ' remaining'),p,index,myNationIndex)
				NATION_ARRAY[index][0]['War']['weapons'][unit] = quantity

		preferencePrint(str('Might gained    : ' + str(bonusMight)),p,index,myNationIndex)
		preferencePrint(str('New Might Total : ' + str(NATION_ARRAY[index][0]['War']['might'])),p,index,myNationIndex)
		preferencePrint(str(''),p,index,myNationIndex)

		# WIN BONUS UNITS
		winProbability = random.randint(0,5)
		winProbability = 5;
		if winProbability == 5:

			allowedAssets = allowedTech(techLevel)
			bonus = random.choice(allowedAssets)
			preferencePrint(str('**BONUS** The brass have gifted ' + str(NATION_ARRAY[index][1]) + ' ' + str(bonus[1]) + ' ' + str(bonus[0])),p,index,myNationIndex)
			NATION_ARRAY[index][0]['War']['weapons'][bonus[0]] = NATION_ARRAY[index][0]['War']['weapons'][bonus[0]] + bonus[1]
		return(NATION_ARRAY)


	return(NATION_ARRAY)




def allowedTech(techLevel):
	if techLevel == 0:
		allowedAssets = [('troops',random.randint(1,100))]
	if techLevel > 1:
		allowedAssets = [('troops',random.randint(1,100)),('tanks',random.randint(1,20))]
	if techLevel > 2:
		allowedAssets = [('troops',random.randint(1,100)),('tanks',random.randint(1,20)),('gunboats',random.randint(1,100))]
	if techLevel > 3:
		allowedAssets = [('troops',random.randint(1,100)),('tanks',random.randint(1,20)),('gunboats',random.randint(1,100)),('destroyers',random.randint(1,20))]
	if techLevel > 5:
		allowedAssets = [('troops',random.randint(1,100)),('tanks',random.randint(1,20)),('gunboats',random.randint(1,100)),('destroyers',random.randint(1,20)),('jets',random.randint(1,5))]
	if techLevel > 7:
		allowedAssets = [('troops',random.randint(1,100)),('tanks',random.randint(1,20)),('gunboats',random.randint(1,100)),('destroyers',random.randint(1,20)),('jets',random.randint(1,5)),('bombers',random.randint(1,3))]
	if techLevel > 8:
		allowedAssets = [('troops',random.randint(1,100)),('tanks',random.randint(1,20)),('gunboats',random.randint(1,100)),('destroyers',random.randint(1,20)),('jets',random.randint(1,5)),('bombers',random.randint(1,3)),('carriers')]
	if techLevel > 9:
		allowedAssets = [('troops',random.randint(1,100)),('tanks',random.randint(1,20)),('gunboats',random.randint(1,100)),('destroyers',random.randint(1,20)),('jets',random.randint(1,5)),('bombers',random.randint(1,3)),('carriers'),('Nukes',random.randint(1,1))]

	return(allowedAssets)


def promotion(currentNation,p,index,myNationIndex):
	warRank = ['Private', 'Lieutenant', 'Captain', 'Major', 'Commander', 'General', 'Supreme Commander']
	might   = currentNation[0]['War']['might']
	rank   = currentNation[0]['War']['level']
	if might > 150 and rank == warRank[0]:
		currentNation[0]['War']['level'] = warRank[1]
		rank   = currentNation[0]['Finance']['level']
		currentNation[0]['Special']['notes'].append('warLevel') 
		preferencePrint(str(currentNation[1] ) + ' levelled up! New War rank is ' + str(currentNation[0]['War']['level']),p,index,myNationIndex)

	if might > 300 and rank == warRank[1]:
		currentNation[0]['War']['level'] = warRank[2]
		rank   = currentNation[0]['Finance']['level']
		currentNation[0]['Special']['notes'].append('warLevel') 
		preferencePrint(str(currentNation[1] ) + ' levelled up! New War rank is ' + str(currentNation[0]['War']['level']),p,index,myNationIndex)

	if might > 500 and rank == warRank[2]:
		currentNation[0]['War']['level'] = warRank[3]
		rank   = currentNation[0]['Finance']['level']
		currentNation[0]['Special']['notes'].append('warLevel') 
		preferencePrint(str(currentNation[1] ) + ' levelled up! New War rank is ' + str(currentNation[0]['War']['level']),p,index,myNationIndex)

	if might > 800 and rank == warRank[3]:
		currentNation[0]['War']['level'] = warRank[4]
		rank   = currentNation[0]['Finance']['level']
		currentNation[0]['Special']['notes'].append('warLevel') 
		preferencePrint(str(currentNation[1] ) + ' levelled up! New War rank is ' + str(currentNation[0]['War']['level']),p,index,myNationIndex)

	if might > 2000 and rank == warRank[4]:
		currentNation[0]['War']['level'] = warRank[5]
		rank   = currentNation[0]['Finance']['level']
		currentNation[0]['Special']['notes'].append('warLevel') 
		preferencePrint(str(currentNation[1] ) + ' levelled up! New War rank is ' + str(currentNation[0]['War']['level']),p,index,myNationIndex)

	if might > 5000 and rank == warRank[5]:
		currentNation[0]['War']['level'] = warRank[6]
		rank   = currentNation[0]['Finance']['level']
		currentNation[0]['Special']['notes'].append('warLevel') 
		preferencePrint(str(currentNation[1] ) + ' levelled up! New War rank is ' + str(currentNation[0]['War']['level']),p,index,myNationIndex)
	return(currentNation)

def firepower(currentNation,p,index,myNationIndex):
	warRank = ['Private', 'Lieutenant', 'Captain', 'Major', 'Commander', 'General', 'Supreme Commander']
	might   = currentNation[0]['War']['might']
	rank   = currentNation[0]['War']['level']

	return(currentNation)
