	# All Finance Menu Function

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
def drill(nextMove,NATION_ARRAY,currentNation,p,index,myNationIndex):
	move      = nextMove[0]
	branch    = nextMove[1]
	intensity = nextMove[2]
	units     = nextMove[3]
	might     = NATION_ARRAY[index][0]['War']['might']
	credits   = NATION_ARRAY[index][0]['Finance']['wealth']


	preferencePrint('',p,index,myNationIndex)
	preferencePrint(str(str(currentNation[1]) + ' chose to train their ' + str(branch)),p,index,myNationIndex)
	preferencePrint('================================',p,index,myNationIndex)
	preferencePrint(str('Intensity: ' + str(intensity)),p,index,myNationIndex)

	if intensity == 'soft':
		bonusMight = round((random.randint(1,15) / 100) * might)
		NATION_ARRAY[index][0]['War']['might'] = NATION_ARRAY[index][0]['War']['might']  + bonusMight
	if intensity == 'medium':
		# WIN MIGTH
		bonusMight = round((random.randint(10,25) / 100) * might)
		NATION_ARRAY[index][0]['War']['might'] = NATION_ARRAY[index][0]['War']['might']  + bonusMight
		
		# WIN CREDITS
		bonusCredits = round((random.randint(1,10) / 100) * credits)
		NATION_ARRAY[index][0]['Finance']['wealth'] = NATION_ARRAY[index][0]['Finance']['wealth']  + bonusCredits
		preferencePrint(str('Credits gained    : ' + str(NATION_ARRAY[index][0]['Finance']['wealth'])),p,index,myNationIndex)

		# LOSE A PORTION OF UNITS 
		lossProbability = random.randint(0,12)
		lossAmount = 0.35
		if lossProbability < 5:
			for unit, quantity in units:
				original = quantity
				if quantity < 1:
					continue
				if random.randint(0,1) == 1:
					loss = round(quantity * (1-lossAmount))
					if loss == quantity:
						quantity = quantity - 1
					else:
						quantity = round(quantity * (1-lossAmount))
					preferencePrint(str(str(unit) + ' lost in combat excercise '),p,index,myNationIndex)
					preferencePrint(str(str(original - quantity) + ' ' + str(unit) +  ' lost'),p,index,myNationIndex)
					preferencePrint(str(str(quantity) + ' remaining'),p,index,myNationIndex)
				NATION_ARRAY[index][0]['War']['weapons'][unit] = quantity


	if intensity == 'hard':
		# GAIN MIGHT
		bonusMight = round((random.randint(20,40) / 100) * might)
		NATION_ARRAY[index][0]['War']['might'] = NATION_ARRAY[index][0]['War']['might']  + bonusMight
		# GAIN CREDITS
		bonusCredits = round((random.randint(5,15) / 100) * credits)
		NATION_ARRAY[index][0]['Finance']['wealth'] = NATION_ARRAY[index][0]['Finance']['wealth']  + bonusCredits
		preferencePrint(str('Credits gained    : ' + str(NATION_ARRAY[index][0]['Finance']['wealth'])),p,index,myNationIndex)

		# LOSE A PORTION OF UNITS 
		lossProbability = random.randint(0,5)
		lossAmount = 0.2
		if lossProbability < 5:
			for unit, quantity in units:
				original = quantity
				if quantity < 1:
					continue
				if random.randint(0,1) == 1: # don't take all of their asset types
					loss = round(quantity * (1-lossAmount))
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


