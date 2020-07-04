
"""
# ---------------------------------------------------------------------
#   PROGRAM SPEC 
#   NAME: gameOfWar
#   DATE OF CREATION: 16 JUNE 2020
#   PROGRAM TYPE: Python Text game
#   SUMMARY: Entry program 
#            Entry loop is while selection != 'Done':
#            Once start game is chosen, menuSelection loop begins
#            menuSelection loop doesn't end and is the whole game. 
#            Game completes once hit the year 2100 (maybe)
#           
# ---------------------------------------------------------------------
"""

"""
THINGS TO SAVE

NAME
YEAR
ARRAY
rank 
selected country 


NOTES: 

myNation is a list, with the first element pointing to the country dict 
playerNationIndex may be required

TODO

- VIEW STATS OF ANY COUNTRY ...
- VIEW AVERAGE OF TRADE
- UNLOCK MORE MUSIC At certain points
- Shop




"""


"""
# ---------------------------------------------------------------------
# UTILITIES 
# ---------------------------------------------------------------------
"""
import sys
import time
import copy
import random

# IMPORT UNIVERSAL UTILITIES
from gameConquest_utilities import slow_print as slow_print
from gameConquest_utilities import med_print as med_print
from gameConquest_utilities import fast_print as fast_print
from gameConquest_utilities import superfast_print as superfast_print
from gameConquest_utilities import clearScreen as clearScreen
from gameConquest_utilities import preferencePrint as preferencePrint
from gameConquest_utilities import options as options
from gameConquest_utilities import music as music
from gameConquest_utilities import updateTechNames as updateTechNames
from gameConquest_utilities  import checkMoves as checkMoves

# FUNCTIONS
from gameFunctionSelection import selectNation as selectNation
from gameFunctionSelection import stats as stats
from gameSetVariables      import setVariables
from gameSetVariables      import returnTechMap
from actionFunctions import action as action
from actionFunctions import nextYear as nextYear
#from AIOrderFunctions import setAIMoves as setAIMoves

# CUSTOM MENUES
import selectionFinance  as fin 
import selectionWar      as warMenu
import selectionPolitics as politics
import selectionIntro    as start
import selectionScience  as tech




"""
# ---------------------------------------------------------------------
# END UTILITIES
# ---------------------------------------------------------------------
"""

# PRice is % of remaining available 
PRICE_TRACKER = {'gold': {'price': 120, 'stock': 10000, 'priceChange': '+0', 'history':[120],'average':120},'raremetals': {'price': 60, 'stock': 2000, 'priceChange': '+0', 'history':[60],'average':60}, 'gems': {'price': 250, 'stock': 2000, 'priceChange': '+0', 'history':[250],'average':250}, 'oil': {'price': 12, 'stock': 10000, 'priceChange': '+0', 'history':[12],'average':12}}

# numbers are price, wait time, might-valuation as percentage (ADDED ON). 
WAR_BRIEFING = {'weapons':{'troops':(10,2,0.01),'tanks':(300,2,0.1),'gunboats':(100,2,0.005),'destroyers':(2000,3,0.1),'carriers':(20000,4,1),'jets':(5000,2,0.3),'bombers':(7000,3,0.35),'Nukes':(100000,4,5)}}

# WAR_BRIEFING = {'weapons':{
# 'StoneAge': {'one':(10,2,0.01,'pikeman'),'two':(300,2,0.1,'knight'),'three':(100,2,0.005,'archer'),'four':(2000,3,0.1,'catapult'),'five':(20000,4,1,'fireArchers'),'six':(5000,2,0.3,'hoursemen'),'seven':(7000,3,0.35,'mountedKnights'),'eight':(100000,4,5,'kingsGuard')}, 
# 'InformationAge':{'one':(10,2,0.01,'troops'),'two':(300,2,0.1,'tanks'),'three':(100,2,0.005,'gunboats'),'four':(2000,3,0.1,'destroyers'),'five':(20000,4,1,'carriers'),'six':(5000,2,0.3,'jets'),'seven':(7000,3,0.35,'bombers'),'eight':(100000,4,5,'Nukes')}}
# }


# Era - map for all names of each age
# EraBonus- map for bonuses awarded when completing that tech
# EraCost - Cost to level up by 1% 

TECH_MAP = returnTechMap()

NATION_ARRAY = setVariables(WAR_BRIEFING)

NATION_ARRAY = updateTechNames(NATION_ARRAY,TECH_MAP)

ARRAY_DICT = {'PRICE_TRACKER':PRICE_TRACKER,'WAR_BRIEFING':WAR_BRIEFING,'TECH_MAP':TECH_MAP,'NATION_ARRAY':NATION_ARRAY}


myNation = ''
buffer = ''
p = 'Me'

# Applies to AI move and Menu



"""
# =====================================================================
# =====================================================================
# =====================================================================
#                           START MENU
#     1. SELECT NATION OPTION
#     2. VIEW COUNTRY
#     3. VIEW RULES
#     4. VIEW CREDITS
#     5. START GAME 
# =====================================================================
# =====================================================================
# =====================================================================
"""



selection = ''
while selection != 'Done':
	clearScreen()
	print('*****************MENU*******************')
	print('')
	print('')
	print('[1] Start Game')
	print('[2] Select your Nation')
	print('[3] Country Stats')
	print('[4] Game rules')
	print('[5] Credits')
	print('[6] JukeBox')
	print('[7] Exit')
	print('')
	print('')


	try:
		selection = int(input('Please chose an option \n'))
	except:
		print("Entered incorrectly, please try again")

	if selection == 1:
		if myNation == '':
			myNation,playerNationIndex =selectNation(NATION_ARRAY)
		fast_print('Starting game... \n')
		clearScreen()
		break
	if selection == 2:
		myNation,playerNationIndex = selectNation(NATION_ARRAY)
	if selection == 3:
		stats(NATION_ARRAY)
	if selection == 4:
		fast_print('The aim of the game is to gain the most points before the year 2100. \n')
		fast_print('This can be by winning on trade, military, culture or other. \n')
		fast_print('Remember, every action has its own consequence! \n')
		fast_print('Good Luck commander! \n' )
		buffer = input('Press enter to continue \n ')
		clearScreen()
	if selection == 5:
		fast_print('All credits go to Adam McMurchie... me! . \n')
		buffer = input('Press enter to continue \n ')
		clearScreen()
	if selection == 6:
		import webbrowser
		music()
	if selection == 7:
		exit()

"""
# =======================================================================
#
#                           INTRO GAME START
#	
#     1. CHECK GAME LOADED FLAG
#     2. LOAD GAME IF FLAG SET
#     3. GET USER NAME
#     4. INTRO SCENE
# =======================================================================
"""


gameLoaded = False

if gameLoaded:
	print('Welcome back commander')


year = 1949

# MUST UNCOMENT FOR FULL GAME
userName = 'DonnerKebab'
#userName = start(userName,myNation)






"""
# =======================================================================
# =======================================================================
# MAIN MENU MAIN MENU MAIN MENU MAIN MENU MAIN MENU MAIN MENU MAIN MENU 
# =======================================================================
#                           MAIN MENU MODE 
#     1. View Leaderboard
#     2. Finance Beuro
#     3. Ministry of war
#     4. Political Cabinet
#     5. Next Year
# =======================================================================
# MAIN MENU MAIN MENU MAIN MENU MAIN MENU MAIN MENU MAIN MENU MAIN MENU
# =======================================================================
"""
def menuUpdate():
	for item in myNation[0]['Special']['notes']:
		if item == 'financeLevel':
			print(""" 
	@('_')@
				""")
			med_print('**CONGRATULATIONS!** Finance Level UP!!')

		if item == 'warLevel':
			print(""" 
	@('_')@
				""")
			med_print('**CONGRATULATIONS!** War Level UP!!')

	# Clear notifications once iterated 
	if len(myNation[0]['Special']['notes']) > 0:
		myNation[0]['Special']['notes'] = []
	

debug = 'n'
menuSelection = ' '
while menuSelection != 'E':
	clearScreen()
	print('*****************MENU*******************')
	print('')
	print('My Team: ' + str(myNation[1]))
	print('Year: ' + str(year))
	print('Wealth : ' + str(myNation[0]['Finance']['wealth']))
	print('Rank: ' + 'Junior')
	print('')
	print(""" 
            ______________
           |[]            |
           |  __________  |
           |  |        |  |
           |  | Home   |  |
           |  |________|  |
           |   ________   |
           |   [ [ ]  ]   |
           |___[_[_]__]___|

			""")
	print('[L] View Leaderboard')
	print('[F] Finance bureau')
	print('[W] Ministry of War')
	print('[P] Political Cabinet (not available)')
	print('[T] Technology Institute')
	print('[N] Next Year')
	print(' ')
	print(' ')
	menuUpdate()
	print(' ')
	print(' ')
	print('[O] Options')
	print('[X] Exit')
	print(' ')
	#print(myNation[0]['Special']['moveLimit'])
	#print(len(myNation[0]['Nextmoves']))
	#print(str( sum(myNation[0]['Nextmoves'], []) ).count('pending'))
	#print(myNation[0]['Nextmoves'])
	#print('Moves: ' + str( myNation[0]['Special']['moveLimit'] - len(myNation[0]['Nextmoves'])  + str(sum(myNation[0]['Nextmoves'], [])).count('pending')))
	print('Moves: ' + str(checkMoves(myNation,"%^")[0]) )
	print('****************************************')
	print(' ')
	print(' ')
	menuSelection = str(input('What would you like to do ' + str(userName) + '? \n')).upper()
	
	if menuSelection == 'L':
		stats(NATION_ARRAY)
	if menuSelection == 'F':
		myNation = fin.financeBeuro(myNation,year,PRICE_TRACKER,NATION_ARRAY)
	if menuSelection == 'W':
		myNation = warMenu.warMinistry(myNation,NATION_ARRAY,year,WAR_BRIEFING)
	if menuSelection == 'P':
		myNation = politics.politicalCabinet(myNation,year,PRICE_TRACKER)
	if menuSelection == 'T':
		myNation = tech.techMenu(myNation,year,PRICE_TRACKER,TECH_MAP)
	if menuSelection == 'N' or menuSelection == '':
		year, NATION_ARRAY,PRICE_TRACKER,WAR_BRIEFING,p = nextYear(year,myNation,ARRAY_DICT,playerNationIndex,p,debug)
	
	if menuSelection == 'O':
		p,debug = options(p,NATION_ARRAY,debug)
	if menuSelection == 'X':
		exit()
		


