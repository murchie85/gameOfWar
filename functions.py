# IMPORT UNIVERSAL UTILITIES
from conquest_utilities import slow_print as slow_print
from conquest_utilities import med_print as med_print
from conquest_utilities import fast_print as fast_print
from conquest_utilities import superfast_print as superfast_print
from conquest_utilities import clearScreen as clearScreen
from conquest_utilities import preferencePrint as preferencePrint
from conquest_utilities import options as options
from conquest_utilities import music as music




"""
# =======================================================================
# =======================================================================
# MENU MENU MENU MENU MENU MENU MENU MENU MENU MENU MENU MENU MENU MENU 
# =======================================================================
#                           FUNCTIONS
#     FUNCTION selectNation
#     FUNCTION stats
#     FUNCTION music
#     PROCEEDURE start game
# =======================================================================
# MENU MENU MENU MENU MENU MENU MENU MENU MENU MENU MENU MENU MENU MENU 
# =======================================================================
"""

def selectNation(NATION_ARRAY):
	clearScreen()
	NationChoice = ''
	nationSelected = ''
	while nationSelected != 'Y':
		print('')
		print('Printing nation list')
		print('')

		for x in range(0, len(NATION_ARRAY)):
			print(str(x) + '. ' + str(NATION_ARRAY[x][-1]))
		print('')
		while NationChoice not in range(0, len(NATION_ARRAY)):
			try:
				NationChoice = int(input('Please chose a country \n'))
			except:
				print("Entered incorrectly, please try again")

		fast_print('Your chosen country is : ' +    str(NATION_ARRAY[NationChoice][-1]) + '\n')
		print('')
		buffer = input('Press Enter to continue \n')
		clearScreen()
		myNation = NATION_ARRAY[NationChoice]
		myNationIndex = NationChoice
		nationSelected = 'Y'
	return(myNation,myNationIndex)


def stats(NATION_ARRAY):
	clearScreen()
	print('Printing nation list')
	print('')
	print('|  Score   |Wealth    |Tech Level|   Name   ')

	rankCounter = []
	for x in range(0, len(NATION_ARRAY)):
		rankCounter.append((NATION_ARRAY[x][0]['Score'],x))
	rankCounter.sort(reverse=True)

	for x in range(0, len(rankCounter)):
		index = rankCounter[x][1]

		score = str(NATION_ARRAY[index][0]['Score'])
		for y in range(0, (10 - len(score))): score = score + ' '

		tradeScore = str(NATION_ARRAY[index][0]['Finance']['wealth'])
		for z in range(0, (10 - len(tradeScore))): tradeScore = tradeScore + ' '

		techScore = str(NATION_ARRAY[index][0]['Tech']['level'])
		for z in range(0, (10 - len(techScore))): techScore = techScore + ' '

		print('|' + score + '|' + tradeScore + '|' + techScore + '|' + '   ' + str(NATION_ARRAY[index][-1])  )

	buffer = input('Press enter to continue \n')
	clearScreen()

