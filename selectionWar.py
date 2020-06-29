# All WAR Menu Function

from gameConquest_utilities import slow_print as slow_print
from gameConquest_utilities import med_print as med_print
from gameConquest_utilities import fast_print as fast_print
from gameConquest_utilities import superfast_print as superfast_print
from gameConquest_utilities import clearScreen as clearScreen
from gameConquest_utilities	 import preferencePrint as preferencePrint


"""
# =====================================================================
# =====================================================================
# =====================================================================
#                           WAR  MENU
#     1. drill
#     2. weapons
#     2.1 buy
#     2.2 scrap
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
		print('Moves: ' + str( myNation[0]['Special']['moveLimit'] - len(myNation[0]['Nextmoves'])  + str(sum(myNation[0]['Nextmoves'], [])).count('pending')))
		print('****************************************')
		print(' ')
		print(' ')
		warSelection = str(input('Please chose an option \n')).upper()
		if warSelection == 'D':
			myNation = drillMenu(myNation,year,WAR_BRIEFING)
		if warSelection == 'W':
			myNation = weaponsMenu(myNation,year,WAR_BRIEFING)
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




def weaponsMenu(myNation,year,WAR_BRIEFING):
	flag = ''
	warSelection = ' '
	show = 'off'
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
		print('                 WEAPONS DEPOT           :X        ')
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
		if show == 'on':
			print('______________')
			print('ARMY      : ' + str(troops + tanks))
			print('--------------')
			print('Troops : ' + str(troops ))
			print('Tanks  : ' + str(tanks))
			print('')
			print('______________')
			print('NAVY      : ' + str(gunboats + destroyers + carriers))
			print('--------------')
			print('Gunboats: ' + str(gunboats))
			print('Destroyers: ' + str(destroyers))
			print('Carriers : ' + str(carriers))
			print('')
			print('______________')
			print('Airforce  : ' + str(jets + bombers))
			print('--------------')
			print('Fighter Jets: ' + str(jets))
			print('Bombers: ' + str(bombers))
		print('')
		print("""
(╯°□°)--︻╦╤─ - - - 
				""")
		showAssets(myNation,year,flag)
		print('')
		print('[B] Build')
		print('[S] Scrap')
		print('[V] View my units')
		print('[R] Return')
		print(' ')
		print(' ')
		print(' ')
		print('Moves: ' + str( myNation[0]['Special']['moveLimit'] - len(myNation[0]['Nextmoves'])  + str(sum(myNation[0]['Nextmoves'], [])).count('pending')))		
		print('****************************************')
		print(' ')
		print(' ')
		warSelection = str(input('Please chose an option \n')).upper()
		if warSelection == 'B':
			myNation = buildMenu(myNation,year,WAR_BRIEFING)
		if warSelection == 'S':
			myNation = scrapMenu(myNation,year,WAR_BRIEFING)
		if warSelection == 'V':
			show = 'on'
		if warSelection == 'T':
			fast_print('not ready')
		if warSelection == 'T':
			fast_print('not ready')
		if warSelection == 'A':
			flag = 'yes'
		if warSelection == 'R' or warSelection == '':
			return(myNation)
	return(myNation)





def buildMenu(myNation,year,WAR_BRIEFING):
	flag = ''
	buildSelection = ' '
	show = 'off'
	price = 'off'
	while buildSelection != 'XYZFFJJJJJJ':
		clearScreen()
		troops     = myNation[0]['War']['weapons']['troops']
		tanks      = myNation[0]['War']['weapons']['tanks']
		gunboats   = myNation[0]['War']['weapons']['gunboats']
		destroyers = myNation[0]['War']['weapons']['destroyers']
		carriers   = myNation[0]['War']['weapons']['carriers']
		jets       = myNation[0]['War']['weapons']['jets']
		bombers    = myNation[0]['War']['weapons']['bombers']
		nukes      = myNation[0]['War']['weapons']['Nukes']
		techLevel  = myNation[0]['Tech']['level']
		print('+++++++++++++++++++++++++++++++++++++++++++++++++++')
		print('               WEAPONS PROCUREMENT       :X        ')
		print('+++++++++++++++++++++++++++++++++++++++++++++++++++')
		print('')
		print('My Team   : ' + str(myNation[1]))
		print('Year      : ' + str(year))
		print('Might     : ' + str(myNation[0]['War']['might']) )
		print('Wealth    : ' + str(myNation[0]['Finance']['wealth']) )
		print('Tech Lv   : ' + str(techLevel) )
		print('')
		print('')
		print('Nuclear: ' + str(nukes))
		print('Total Firepower : ' + str(myNation[0]['War']['firePower']) )
		print(' ')
		print('')
		print("""
(╯°□°)--︻╦╤─ - - - 
				""")
		print('')
		print('Build')
		print('[S] Soldiers')
		print('[T] Tanks')
		print('[G] Gunboats')
		print('[D] Destroyers')
		print('[J] Jets')
		print('[B] Bombers')
		print('[A] Aircraft Cariers')
		print('[N] Nukes')
		print('')
		print('')
		if price == 'on':
			print('==============')
			print(' Pricings     ')
			print('==============')
			print('______________')
			print('ARMY         : ')
			print('--------------')
			print('Troop        = $' + str(WAR_BRIEFING['weapons']['troops'][0]))
			print('buildTime    = ' + str(WAR_BRIEFING['weapons']['troops'][1]) )
			print('MightPoints  = +' + str(WAR_BRIEFING['weapons']['troops'][2] * 100) + '%')
			print('')
			print('Tanks        = $' + str(WAR_BRIEFING['weapons']['tanks'][0]))
			print('buildTime    = ' + str(WAR_BRIEFING['weapons']['tanks'][1]) )
			print('MightPoints  = +' + str(WAR_BRIEFING['weapons']['tanks'][2] * 100) + '%')
			print('')
			print('______________')
			print('NAVY         : ')
			print('--------------')
			print('Gunboats     = $' + str(WAR_BRIEFING['weapons']['gunboats'][0]))
			print('buildTime    = ' + str(WAR_BRIEFING['weapons']['gunboats'][1]) )
			print('MightPoints  = +' + str(WAR_BRIEFING['weapons']['gunboats'][2] * 100) + '%')
			print('')
			print('Destroyers   = $' + str(WAR_BRIEFING['weapons']['destroyers'][0]))
			print('buildTime    = ' + str(WAR_BRIEFING['weapons']['destroyers'][1]) )
			print('MightPoints  = +' + str(WAR_BRIEFING['weapons']['destroyers'][2] * 100) + '%')
			print('')
			print('Carriers     = $' + str(WAR_BRIEFING['weapons']['carriers'][0]))
			print('buildTime    = ' + str(WAR_BRIEFING['weapons']['carriers'][1]) )
			print('MightPoints  = +' + str(WAR_BRIEFING['weapons']['carriers'][2] * 100) + '%')
			print('')
			print('______________')
			print('Airforce     : ')
			print('--------------')
			print('Fighter Jets = $' + str(WAR_BRIEFING['weapons']['jets'][0]))
			print('buildTime    = ' + str(WAR_BRIEFING['weapons']['jets'][1]) )
			print('MightPoints  = +' + str(WAR_BRIEFING['weapons']['jets'][2] * 100) + '%')
			print('')
			print('Bombers      = $' + str(WAR_BRIEFING['weapons']['bombers'][0]))
			print('buildTime    = ' + str(WAR_BRIEFING['weapons']['bombers'][1]) )
			print('MightPoints  = +' + str(WAR_BRIEFING['weapons']['bombers'][2] * 100) + '%')
			print('')
			print('')
			print('Nukes        = $' + str(WAR_BRIEFING['weapons']['Nukes'][0]))
			print('buildTime    = ' + str(WAR_BRIEFING['weapons']['Nukes'][1]) )
			print('MightPoints  = +' + str(WAR_BRIEFING['weapons']['Nukes'][2] * 100) + '%')
			print('')
			fast_print('Press Enter to clear ')
			price = 'off'
			print('')
		if show == 'on':
			print('______________')
			print('ARMY  ' + str(troops + tanks))
			print('--------------')
			print('Troops : ' + str(troops ))
			print('Tanks  : ' + str(tanks))
			print('')
			print('______________')
			print('NAVY  ' + str(gunboats + destroyers + carriers))
			print('--------------')
			print('Gunboats: ' + str(gunboats))
			print('Destroyers: ' + str(destroyers))
			print('Carriers : ' + str(carriers))
			print('')
			print('______________')
			print('Airforce ' + str(jets + bombers))
			print('--------------')
			print('Fighter Jets: ' + str(jets))
			print('Bombers: ' + str(bombers))
			print('')
			print('')
			print('Nukes: ' + str(nukes))
			fast_print('press Enter to clear')
			print(' ')
			show = 'off'
		print('Options')
		print('[V] View your units')
		print('[P] Get Unit pricings')
		print('[R] Return')
		print(' ')
		print(' ')
		print(' ')
		print('Moves: ' + str( myNation[0]['Special']['moveLimit'] - len(myNation[0]['Nextmoves'])  + str(sum(myNation[0]['Nextmoves'], [])).count('pending')))
		print('****************************************')
		print(' ')
		print(' ')
		# CHECK MAX MOVES SINCE INSIDE WHILE LOOP
		moveLimit = int(myNation[0]['Special']['moveLimit'] - len(myNation[0]['Nextmoves']) + str(sum(myNation[0]['Nextmoves'], [])).count('pending') )
		if moveLimit < 1: 
			input('you have used up all your moves for this round')
			return(myNation)

		buildSelection = str(input('Please chose an option \n')).upper()
		if buildSelection == 'S':
			clearScreen()
			myNation = buildUnits(myNation,year,WAR_BRIEFING,'troops')
		if buildSelection == 'T':
			clearScreen()
			if techLevel < 1:
				print('Build up your science level to unlock Tanks')
				fast_print('Your Tech level is not high enough')
				continue
			myNation = buildUnits(myNation,year,WAR_BRIEFING,'tanks')
		if buildSelection == 'G':
			clearScreen()
			if techLevel < 2:
				print('Build up your science level to unlock Gunboats')
				fast_print('Your Tech level is not high enough')
				continue 
			myNation = buildUnits(myNation,year,WAR_BRIEFING,'gunboats')
		if buildSelection == 'D':
			clearScreen()
			if techLevel < 4:
				print('Build up your science level to unlock Destroyers')
				fast_print('Your Tech level is not high enough')
				continue
			myNation = buildUnits(myNation,year,WAR_BRIEFING,'destroyers')
		if buildSelection == 'J':
			clearScreen()
			if techLevel < 6:
				print('Build up your science level to unlock Jets')
				fast_print('Your Tech level is not high enough')
				continue
			myNation = buildUnits(myNation,year,WAR_BRIEFING,'jets')
		if buildSelection == 'B':
			clearScreen()
			if techLevel < 8:
				print('Build up your science level to unlock Bombers')
				fast_print('Your Tech level is not high enough')
				continue
			myNation = buildUnits(myNation,year,WAR_BRIEFING,'bombers')
		if buildSelection == 'A':
			clearScreen()
			if techLevel < 9:
				print('Build up your science level to unlock Aircraft Carriers')
				fast_print('Your Tech level is not high enough')
				continue
			myNation = buildUnits(myNation,year,WAR_BRIEFING,'carriers')
		if buildSelection == 'N':
			clearScreen()
			if techLevel < 10:
				print('Build up your science level to unlock Nukes')
				fast_print('Your Tech level is not high enough')
				continue
			myNation = buildUnits(myNation,year,WAR_BRIEFING,'Nukes')
		if buildSelection == 'V':
			clearScreen()
			show = 'on'
		if buildSelection == 'P':
			clearScreen()
			price = 'on'
		if buildSelection == 'R' or buildSelection == '':
			return(myNation)
	return(myNation)





def buildUnits(myNation,year,WAR_BRIEFING,unit):

	price      = WAR_BRIEFING['weapons'][unit][0]
	wait       = WAR_BRIEFING['weapons'][unit][1]
	bonusMight = WAR_BRIEFING['weapons'][unit][2]
	credits    = myNation[0]['Finance']['wealth']

	maxpurchase = int(credits // price)
	print('Note* This unit as a wait time of  ' + str(wait) + ' round[s]')
	print('You can buy up to ' + str(maxpurchase) + ' ' + str(unit) + ' at a cost of $' + str(price) + ' each.' )

	try:
		purchaseAmount = int(input('Enter amount \n'))
	except:
		print("Entered incorrectly, please try again")
		return(myNation)

	cost = purchaseAmount * price

	if cost > credits:
		input('Not enough credits, sorry \n')
		return(myNation)
	if purchaseAmount < 1:
		input('Enter a correct amount \n')
		return(myNation)

	# Deduct cost & Place Order 
	myNation[0]['Finance']['wealth'] = myNation[0]['Finance']['wealth'] - cost
	myNation[0]['Nextmoves'] = myNation[0]['Nextmoves'] + [['submitted','WeaponsBuild',unit, purchaseAmount,wait,bonusMight]]

	superfast_print('Purchase order for ' + str(unit) + ' placed at a cost of ' + str(cost) + '\n')
	input('Press enter to continue \n')
	return(myNation)








def scrapMenu(myNation,year,WAR_BRIEFING):
	flag = ''
	buildSelection = ' '
	show = 'off'
	price = 'off'
	while buildSelection != 'XYZFFJJJJJJ':
		clearScreen()
		troops     = myNation[0]['War']['weapons']['troops']
		tanks      = myNation[0]['War']['weapons']['tanks']
		gunboats   = myNation[0]['War']['weapons']['gunboats']
		destroyers = myNation[0]['War']['weapons']['destroyers']
		carriers   = myNation[0]['War']['weapons']['carriers']
		jets       = myNation[0]['War']['weapons']['jets']
		bombers    = myNation[0]['War']['weapons']['bombers']
		nukes      = myNation[0]['War']['weapons']['Nukes']
		techLevel  = myNation[0]['Tech']['level']
		print('+++++++++++++++++++++++++++++++++++++++++++++++++++')
		print('                    SCRAP YARD           :X        ')
		print('+++++++++++++++++++++++++++++++++++++++++++++++++++')
		print('')
		print('My Team   : ' + str(myNation[1]))
		print('Year      : ' + str(year))
		print('Might     : ' + str(myNation[0]['War']['might']) )
		print('Wealth    : ' + str(myNation[0]['Finance']['wealth']) )
		print('Tech Lv   : ' + str(techLevel) )
		print('')
		print('')
		print('Nuclear: ' + str(nukes))
		print('Total Firepower : ' + str(myNation[0]['War']['firePower']) )
		print(' ')
		print('')
		print("""
(╯°□°)--︻╦╤─ - - - 
				""")
		print('')
		print('Build')
		print('[S] Soldiers')
		print('[T] Tanks')
		print('[G] Gunboats')
		print('[D] Destroyers')
		print('[J] Jets')
		print('[B] Bombers')
		print('[A] Aircraft Cariers')
		print('[N] Nukes')
		print('')
		print('')
		if price == 'on':
			print('==============')
			print(' Valuations   ')
			print('==============')
			print('______________')
			print('ARMY         : ')
			print('--------------')
			print('Troop        = $' + str(WAR_BRIEFING['weapons']['troops'][0]))
			print('MightPoints  = -' + str(WAR_BRIEFING['weapons']['troops'][2] * 100) + '%')
			print('')
			print('Tanks        = $' + str(WAR_BRIEFING['weapons']['tanks'][0]))
			print('MightPoints  = -' + str(WAR_BRIEFING['weapons']['tanks'][2] * 100) + '%')
			print('')
			print('______________')
			print('NAVY         : ')
			print('--------------')
			print('Gunboats     = $' + str(WAR_BRIEFING['weapons']['gunboats'][0]))
			print('MightPoints  = -' + str(WAR_BRIEFING['weapons']['gunboats'][2] * 100) + '%')
			print('')
			print('Destroyers   = $' + str(WAR_BRIEFING['weapons']['destroyers'][0]))
			print('MightPoints  = -' + str(WAR_BRIEFING['weapons']['destroyers'][2] * 100) + '%')
			print('')
			print('Carriers     = $' + str(WAR_BRIEFING['weapons']['carriers'][0]))
			print('MightPoints  = -' + str(WAR_BRIEFING['weapons']['carriers'][2] * 100) + '%')
			print('')
			print('______________')
			print('Airforce     : ')
			print('--------------')
			print('Fighter Jets = $' + str(WAR_BRIEFING['weapons']['jets'][0]))
			print('MightPoints  = -' + str(WAR_BRIEFING['weapons']['jets'][2] * 100) + '%')
			print('')
			print('Bombers      = $' + str(WAR_BRIEFING['weapons']['bombers'][0]))
			print('MightPoints  = -' + str(WAR_BRIEFING['weapons']['bombers'][2] * 100) + '%')
			print('')
			print('')
			print('Nukes        = $' + str(WAR_BRIEFING['weapons']['Nukes'][0]))
			print('MightPoints  = -' + str(WAR_BRIEFING['weapons']['Nukes'][2] * 100) + '%')
			print('')
			fast_print('Press Enter to clear ')
			print('')
			price = 'off'
		if show == 'on':
			print('______________')
			print('ARMY ' + str(troops + tanks))
			print('--------------')
			print('Troops : ' + str(troops ))
			print('Tanks  : ' + str(tanks))
			print('')
			print('______________')
			print('NAVY   ' + str(gunboats + destroyers + carriers))
			print('--------------')
			print('Gunboats: ' + str(gunboats))
			print('Destroyers: ' + str(destroyers))
			print('Carriers : ' + str(carriers))
			print('')
			print('______________')
			print('Airforce ' + str(jets + bombers))
			print('--------------')
			print('Fighter Jets: ' + str(jets))
			print('Bombers: ' + str(bombers))
			print('')
			print('')
			print('Nukes: ' + str(nukes))
			print('')
			fast_print('press Enter to clear')
			print(' ')
			show = 'off'
		print('Options')
		print('[V] View your units')
		print('[P] Get Unit scrap valuation')
		print('[R] Return')
		print(' ')
		print(' ')
		print(' ')
		print('Moves: ' + str( myNation[0]['Special']['moveLimit'] - len(myNation[0]['Nextmoves'])  + str(sum(myNation[0]['Nextmoves'], [])).count('pending')))		
		print('****************************************')
		print(' ')
		print(' ')
		# CHECK MAX MOVES SINCE INSIDE WHILE LOOP
		moveLimit = int(myNation[0]['Special']['moveLimit'] - len(myNation[0]['Nextmoves'] ) + str(sum(myNation[0]['Nextmoves'], [])).count('pending') )
		if moveLimit < 1: 
			input('you have used up all your moves for this round')
			return(myNation)


		buildSelection = str(input('Please chose an option \n')).upper()
		if buildSelection == 'S':
			clearScreen()
			if troops < 1:
				fast_print('You dont have any to scrap..')
				continue
			myNation = scrapUnits(myNation,year,WAR_BRIEFING,'troops')
		if buildSelection == 'T':
			clearScreen()
			if tanks < 1:
				fast_print('You dont have any to scrap..')
				continue
			myNation = scrapUnits(myNation,year,WAR_BRIEFING,'tanks')
		if buildSelection == 'G':
			clearScreen()
			if gunboats < 1:
				fast_print('You dont have any to scrap..')
				continue
			myNation = scrapUnits(myNation,year,WAR_BRIEFING,'gunboats')
		if buildSelection == 'D':
			clearScreen()
			if destroyers < 1:
				fast_print('You dont have any to scrap..')
				continue
			myNation = scrapUnits(myNation,year,WAR_BRIEFING,'destroyers')
		if buildSelection == 'J':
			clearScreen()
			if jets < 1:
				fast_print('You dont have any to scrap..')
				continue
			myNation = scrapUnits(myNation,year,WAR_BRIEFING,'jets')
		if buildSelection == 'B':
			clearScreen()
			if bombers < 1:
				fast_print('You dont have any to scrap..')
				continue
			myNation = scrapUnits(myNation,year,WAR_BRIEFING,'bombers')
		if buildSelection == 'A':
			clearScreen()
			if carriers < 1:
				fast_print('You dont have any to scrap..')
				continue
			myNation = scrapUnits(myNation,year,WAR_BRIEFING,'carriers')
		if buildSelection == 'N':
			clearScreen()
			if nukes < 1:
				fast_print('You dont have any to scrap..')
				continue
			myNation = scrapUnits(myNation,year,WAR_BRIEFING,'Nukes')
		if buildSelection == 'V':
			clearScreen()
			show = 'on'
		if buildSelection == 'P':
			clearScreen()
			price = 'on'
		if buildSelection == 'R' or buildSelection == '':
			return(myNation)
	return(myNation)




def scrapUnits(myNation,year,WAR_BRIEFING,unit):
	price      = WAR_BRIEFING['weapons'][unit][0]
	wait       = WAR_BRIEFING['weapons'][unit][1]
	bonusMight = WAR_BRIEFING['weapons'][unit][2]
	unitsOwned = myNation[0]['War']['weapons'][unit]

	print('Note* This unit as a wait time of  ' + str(wait) + ' round[s]')
	print('You can scrap up to ' + str(unitsOwned) + ' ' + str(unit) + ' for $' + str(price) + ' each.')

	try:
		scrapAmount = int(input('Enter amount to be scrapped \n'))
	except:
		print("Entered incorrectly, please try again")
		return(myNation)

	valuation = scrapAmount * price

	if scrapAmount > unitsOwned:
		input('you entered too much \n')
		return(myNation)
	if scrapAmount < 1:
		input('Enter an incorrect value \n')
		return(myNation)

	# Reduce units and Place Order
	myNation[0]['War']['weapons'][unit] = myNation[0]['War']['weapons'][unit] - scrapAmount
	myNation[0]['Nextmoves'] = myNation[0]['Nextmoves'] + [['WeaponsScrap',unit, scrapAmount,valuation,bonusMight]]


	superfast_print('Scrap order for ' + str(unit) + ' placed at a cost of ' + str(valuation) + '\n')
	print('You will get paid next round \n')
	print('')
	input('Press enter to continue \n')
	return(myNation)








def drill(myNation, branch,units,WAR_BRIEFING):
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
		clearScreen()
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
	buffer = input('Press enter to continue \n ')
	return(myNation)




def drillMenu(myNation,year,WAR_BRIEFING):
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
		print('Moves: ' + str( myNation[0]['Special']['moveLimit'] - len(myNation[0]['Nextmoves'])  + str(sum(myNation[0]['Nextmoves'], [])).count('pending')))
		print('****************************************')
		print(' ')
		print(' ')
		# CHECK MAX MOVES SINCE INSIDE WHILE LOOP
		moveLimit = int(myNation[0]['Special']['moveLimit'] - len(myNation[0]['Nextmoves']) + str(sum(myNation[0]['Nextmoves'], [])).count('pending') )
		if moveLimit < 1: 
			input('you have used up all your moves for this round')
			return(myNation)

		drillSelection = input('Select a divison to train \n').upper()
		clearScreen()
		if drillSelection == 'G':
			if (troops + tanks) < 1:
				input('No army assets to train... \n')
				break
			units = [('troops',troops),('tanks',tanks)]
			myNation = drill(myNation, 'army',units,WAR_BRIEFING)
		if drillSelection == 'N':
			if (gunboats + destroyers + carriers) < 1:
				input('No navy assets to train... \n')
				break
			units = [('gunboats',gunboats),('destroyers',destroyers),('carriers',carriers)]
			myNation = drill(myNation, 'navy',units,WAR_BRIEFING)
		if drillSelection == 'A':
			if (jets + bombers) < 1:
				input('No airforce assets to train... \n')
				break
			units = [('jets',jets),('bombers',bombers)]
			myNation = drill(myNation, 'Airforce',units,WAR_BRIEFING)
		if drillSelection == 'D':
			flag = 'yes'
		if drillSelection == 'R' or drillSelection == '':
			return(myNation)
	return(myNation)	

