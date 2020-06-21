# All WAR Menu Function

from conquest_utilities import slow_print as slow_print
from conquest_utilities import med_print as med_print
from conquest_utilities import fast_print as fast_print
from conquest_utilities import superfast_print as superfast_print
from conquest_utilities import clearScreen as clearScreen
from conquest_utilities	 import preferencePrint as preferencePrint


import warFunctions as War
"""
# =====================================================================
# =====================================================================
# =====================================================================
#                           WAR  MENU
#     1. Gamble
#     2. Trade
#     2.1 buy
#     2.2 sell
#     5. Exit
# =====================================================================
# =====================================================================
# =====================================================================
"""


def warMinistry(myNation,year,WAR_BRIEFING):
	warSelection = ' '
	while warSelection != 'XYZFFJJJJJJ':
		clearScreen()
		print('+++++++++++++++++++++++++++++++++++++++++++++++++++')
		print('        WELCOME TO THE MINISTRY OF WAR   :X        ')
		print('+++++++++++++++++++++++++++++++++++++++++++++++++++')
		print('')
		print('My Team: ' + str(myNation[1]))
		print('Year: ' + str(year))
		print('Might : ' + str(myNation[0]['War']['might']) )
		print('Level  : ' + str(myNation[0]['War']['level']))
		print('')
		print('[D] Drill')
		print('[W] Weapons')
		print('[C] Combat Manevres')
		print('[O] Offensive Missions')
		print('[R] Return')
		print(' ')
		print(' ')
		print(' ')
		print('Moves: ' + str(myNation[0]['Special']['moveLimit'] - len(myNation[0]['Nextmoves'])     ))
		print('****************************************')
		print(' ')
		print(' ')
		warSelection = str(input('Please chose an option \n')).upper()
		if warSelection == 'D':
			myNation = War.drill(myNation)
		if warSelection == 'T':
			print('not ready')
		if warSelection == 'T':
			print('not ready')
		if warSelection == 'T':
			print('not ready')
		if warSelection == 'T':
			print('not ready')
		if warSelection == 'R' or warSelection == '':
			return(myNation)
	return(myNation)


def gambleMenu(myNation,year):
	clearScreen()
	print('My Team: ' + str(myNation[1]))
	print('Year: ' + str(year))
	print('Trade Credits: ' + str(myNation[0]['Finance']['wealth']))
	print(' ')
	print('')
	

	# CHECK MAX MOVES
	movesLeft = myNation[0]['Special']['moveLimit'] - len(myNation[0]['Nextmoves'])
	print('moves left: ' + str(movesLeft))

	if movesLeft < 1: 
		input('you have used up all your moves for this round')
		return(myNation)

	for item in myNation[0]['Nextmoves']:
		if 'gamble' in item:
			input('you have already gambled this round')
			return(myNation)


	creditsAvailable = int(myNation[0]['Finance']['wealth'])
	gambleAmount = 0

	if creditsAvailable < 1:
		input('you do not have enough credits, sorry')	
		return(myNation)


	fast_print('How much do you wish to gamble? \n')
	while gambleAmount < 1:
		try:
			gambleAmount = int(input('Input amount between 1 and ' + str(creditsAvailable) + '\n'))
		except:
			print("Entered incorrectly, please try again")
	
	if gambleAmount > creditsAvailable:
		fast_print('Entered too much')
		return(myNation)

	# Decrement wealth now.
	myNation[0]['Finance']['wealth'] = myNation[0]['Finance']['wealth'] - gambleAmount
	myNation[0]['Nextmoves'] = myNation[0]['Nextmoves'] + [['gamble',gambleAmount]]

	print('You will gamble ' + str(gambleAmount) + ' in the next round')
	buffer = input('Press enter to continue \n ')
	skipflag = 'y'
	return(myNation)
	