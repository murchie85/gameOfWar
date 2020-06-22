# All WAR Menu Function

from conquest_utilities import slow_print as slow_print
from conquest_utilities import med_print as med_print
from conquest_utilities import fast_print as fast_print
from conquest_utilities import superfast_print as superfast_print
from conquest_utilities import clearScreen as clearScreen
from conquest_utilities	 import preferencePrint as preferencePrint


import warFunction as War
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
def showAssets(myNation,year,flag):
	if flag == 'yes':
		troops     = myNation[0]['War']['weapons']['troops']
		tanks      = myNation[0]['War']['weapons']['tanks']
		gunboats   = myNation[0]['War']['weapons']['gunboats']
		destroyers = myNation[0]['War']['weapons']['destroyers']
		carriers   = myNation[0]['War']['weapons']['carriers']
		jets       = myNation[0]['War']['weapons']['jets']
		bombers    = myNation[0]['War']['weapons']['bombers']
		nukes      = myNation[0]['War']['weapons']['Nukes']
		print('ARMY      : ' + str(troops + tanks))
		print('--------------')
		print('Troops : ' + str(troops ))
		print('Tanks  : ' + str(tanks))
		print('')
		print('NAVY      : ' + str(gunboats + destroyers + carriers))
		print('--------------')
		print('Gunboats: ' + str(gunboats))
		print('Destroyers: ' + str(destroyers))
		print('Carriers : ' + str(carriers))
		print('')
		print('Airforce  : ' + str(jets + bombers))
		print('--------------')
		print('Fighter Jets: ' + str(jets))
		print('Bombers: ' + str(bombers))
		print('')
		print('Nuclear: ' + str(nukes))
		print('Total Firepower : ' + str(myNation[0]['War']['firePower']) )
		print(' ')
		input('Enter to continue \n')


def warMinistry(myNation,year,WAR_BRIEFING):
	flag = ''
	warSelection = ' '
	while warSelection != 'XYZFFJJJJJJ':
		clearScreen()
		troops     = myNation[0]['War']['weapons']['troops']
		tanks      = myNation[0]['War']['weapons']['tanks']
		gunboats   = myNation[0]['War']['weapons']['gunboats']
		destroyers = myNation[0]['War']['weapons']['destroyers']
		carriers   = myNation[0]['War']['weapons']['carriers']
		jets       = myNation[0]['War']['weapons']['jets']
		bombers    = myNation[0]['War']['weapons']['bombers']
		nukes      = myNation[0]['War']['weapons']['Nukes']
		print('+++++++++++++++++++++++++++++++++++++++++++++++++++')
		print('        WELCOME TO THE MINISTRY OF WAR   :X        ')
		print('+++++++++++++++++++++++++++++++++++++++++++++++++++')
		print('')
		print('My Team   : ' + str(myNation[1]))
		print('Year      : ' + str(year))
		print('Might     : ' + str(myNation[0]['War']['might']) )
		print('Rank     : ' + str(myNation[0]['War']['level']))
		print('Firepower : ' + str(myNation[0]['War']['firePower']) )
		print(' ')
		print('')
		print("""
(╯°□°)--︻╦╤─ - - - 
				""")
		showAssets(myNation,year,flag)
		print('')
		print('[D] Drill')
		print('[W] Weapons')
		print('[C] Combat Manevres')
		print('[O] Offensive Missions')
		print('[A] Show Military Assets')
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
			myNation = drillMenu(myNation,year)
		if warSelection == 'T':
			fast_print('not ready')
		if warSelection == 'T':
			fast_print('not ready')
		if warSelection == 'T':
			fast_print('not ready')
		if warSelection == 'T':
			fast_print('not ready')
		if warSelection == 'A':
			flag = 'yes'
		if warSelection == 'R' or warSelection == '':
			return(myNation)
	return(myNation)





def drill(myNation, branch,units):
	# CHECK MAX MOVES
	movesLeft = myNation[0]['Special']['moveLimit'] - len(myNation[0]['Nextmoves'])
	print('')
	if movesLeft < 1: 
		input('you have used up all your moves for this round..')
		return(myNation)

	for item in myNation[0]['Nextmoves']:
		if 'drill' in item:
			input('you have already carried out a drill this round..')
			return(myNation)

	intensity = 'low'
	while intensity != 'XYZFFJJJJJJ':
		print('[S] Soft')
		print('[M] Medium')
		print('[H] Hard')
		print('[I] More Info')
		print('[R] Return')
		intensity = input('How hard do you want to train your ' + str(branch) + '?\n').upper()
		if intensity == 'S':
			drillOrder = ['drill',branch,'soft',units]
			break
		if intensity == 'M':
			drillOrder = ['drill',branch,'medium',units]
			break
		if intensity == 'H':
			drillOrder = ['drill',branch,'hard',units]
			break
		if intensity == 'I':
			fast_print('The harder you drill your units the more benefits you will gain, but the risk of loss also increases. \n')
			print('Soft  : Might ++, low probability of loss')
			print('Medium: Might ++, credits ++, medium probability of loss')
			print('Hard  : Might ++, credits ++ newUnits ++, high probability of loss')
			input('Enter to continue \n')
		if intensity == 'R' or intensity == '':
			return(myNation)

	


	# Deduct units
	for unit,amount in units:
		myNation[0]['War']['weapons'][unit] = 0
	# Place Order
	myNation[0]['Nextmoves'] = myNation[0]['Nextmoves'] + [drillOrder]

	print('You will drill your ' + str(branch) + ' at ' + str(drillOrder[2]) + ' intensity')
	print('Your '  + str(branch) + ' will embark on training, the units will be returned to you next round.' )
	print(drillOrder)
	print(myNation[0]['War']['weapons'])
	buffer = input('Press enter to continue \n ')
	return(myNation)




def drillMenu(myNation,year):
	drillSelection = ' '
	flag = ''
	while drillSelection != 'XYZFFJJJJJJ':
		clearScreen()
		troops     = myNation[0]['War']['weapons']['troops']
		tanks      = myNation[0]['War']['weapons']['tanks']
		gunboats   = myNation[0]['War']['weapons']['gunboats']
		destroyers = myNation[0]['War']['weapons']['destroyers']
		carriers   = myNation[0]['War']['weapons']['carriers']
		jets       = myNation[0]['War']['weapons']['jets']
		bombers    = myNation[0]['War']['weapons']['bombers']
		nukes      = myNation[0]['War']['weapons']['Nukes']


		print('+++++++++++++++++++++++++++++++++++++++++++++++++++')
		print('       !!MILITARY DRILL HEADQUARTERS!!   :X        ')
		print('+++++++++++++++++++++++++++++++++++++++++++++++++++')
		print('')
		print('My Team   : ' + str(myNation[1]))
		print('Year      : ' + str(year))
		print('Might     : ' + str(myNation[0]['War']['might']) )
		print('Rank     : ' + str(myNation[0]['War']['level']))
		print('Army      : ' + str(troops + tanks))
		print('Navy      : ' + str(gunboats + destroyers + carriers))
		print('Airforce  : ' + str(jets + bombers))
		print('Nuclear   : ' + str(nukes))
		print('Firepower : ' + str(myNation[0]['War']['firePower']) )
		print(' ')
		print(' ')
		showAssets(myNation,year,flag)
		print('')
		print('[G] Ground Forces')
		print('[N] Navy')
		print('[A] Airforce')
		print('[D] Detailed forces review')
		print('[R] Return')
		print(' ')
		print(' ')
		print(' ')
		print('Moves: ' + str(myNation[0]['Special']['moveLimit'] - len(myNation[0]['Nextmoves'])     ))
		print('****************************************')
		print(' ')
		print(' ')
		drillSelection = input('Select a divison to train \n').upper()
		if drillSelection == 'G':
			if (troops + tanks) < 1:
				input('No army assets to train... \n')
				break
			units = [('troops',troops),('tanks',tanks)]
			myNation = drill(myNation, 'army',units)
		if drillSelection == 'N':
			if (gunboats + destroyers + carriers) < 1:
				input('No navy assets to train... \n')
				break
			units = [('gunboats',gunboats),('destroyers',destroyers),('carriers',carriers)]
			myNation = drill(myNation, 'navy',units)
		if drillSelection == 'A':
			if (jets + bombers) < 1:
				input('No airforce assets to train... \n')
				break
			units = [('jets',jets),('bombers',bombers)]
			myNation = drill(myNation, 'Airforce',units)
		if drillSelection == 'D':
			flag = 'yes'
		if drillSelection == 'R' or drillSelection == '':
			return(myNation)
	return(myNation)	

