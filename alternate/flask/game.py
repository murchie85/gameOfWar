
"""
# ---------------------------------------------------------------------
#   PROGRAM SPEC 
#   NAME: gameOfWar
#   DATE OF CREATION: 16 JUNE 2020
#   PROGRAM TYPE: Python Text game
#   SUMMARY: This program runs a sereis of standard if, for, while loops
#            user inputs and write to file methods. 
#            The aim of the game is for a user to play through a series
#            of time and improve their overall selected countries score. 
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
myNationIndex may be required

FEATURES TO ADD

- UNLOCK MORE MUSIC At certain points
- GOLD VALUATION LOOKS AT HOW MUCH GOLD HAS BEEN BOUGHT/SOLD OVER LAST ROUND 




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

from conquest_utilities import slow_print as slow_print
from conquest_utilities import med_print as med_print
from conquest_utilities import fast_print as fast_print
from conquest_utilities import superfast_print as superfast_print
from conquest_utilities import clearScreen as clearScreen
from conquest_utilities import preferencePrint as preferencePrint
from conquest_utilities import options as options
from conquest_utilities import music as music

# BUFFER PRINT

"""
# ---------------------------------------------------------------------
# END UTILITIES
# ---------------------------------------------------------------------
"""





USA           = {'Score': 0, 'Finance':{'wealth': 10000, 'gold':120, 'gems':30, 'raremetals':10, 'oil':200} , 'Tech':{'level': 3, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0, 'moveLimit':2} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmoves' : []}
CHINA         = {'Score': 0, 'Finance':{'wealth': 8000,  'gold':40, 'gems':20, 'raremetals':200, 'oil':20} , 'Tech':{'level': 4, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0, 'moveLimit':2} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmoves' : []}
INDIA         = {'Score': 0, 'Finance':{'wealth': 3000,  'gold':100, 'gems':30, 'raremetals':30, 'oil':20} , 'Tech':{'level': 3, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0, 'moveLimit':2} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmoves' : []}
RUSSIA        = {'Score': 0, 'Finance':{'wealth': 2000,  'gold':50, 'gems':10, 'raremetals':20, 'oil':200} , 'Tech':{'level': 2, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0, 'moveLimit':2} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmoves' : []}
UK            = {'Score': 0, 'Finance':{'wealth': 2000,  'gold':90, 'gems':10, 'raremetals':0, 'oil':120} , 'Tech':{'level': 3, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0, 'moveLimit':2} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmoves' : []}
GERMANY       = {'Score': 0, 'Finance':{'wealth': 2000,  'gold':50, 'gems':10, 'raremetals':30, 'oil':10} , 'Tech':{'level': 3, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0, 'moveLimit':2} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmoves' : []}
ITALY 		  = {'Score': 0, 'Finance':{'wealth': 2000,  'gold':80, 'gems':20, 'raremetals':0, 'oil':30} , 'Tech':{'level': 3, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0, 'moveLimit':2} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmoves' : []}
SPAIN 		  = {'Score': 0, 'Finance':{'wealth': 2000,  'gold':90, 'gems':20, 'raremetals':10, 'oil':20} , 'Tech':{'level': 3, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0, 'moveLimit':2} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmoves' : []}
FRANCE        = {'Score': 0, 'Finance':{'wealth': 2000,  'gold':80, 'gems':50, 'raremetals':10, 'oil':10} , 'Tech':{'level': 3, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0, 'moveLimit':2} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmoves' : []}
JAPAN         = {'Score': 0, 'Finance':{'wealth': 2000,  'gold':70, 'gems':20, 'raremetals':100, 'oil':20} , 'Tech':{'level': 3, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0, 'moveLimit':2} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmoves' : []}
BRAZIL        = {'Score': 0, 'Finance':{'wealth': 1000,  'gold':30, 'gems':30, 'raremetals':30, 'oil':80} , 'Tech':{'level': 2, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0, 'moveLimit':2} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmoves' : []}
SOUTHKOREA    = {'Score': 0, 'Finance':{'wealth': 2000,  'gold':50, 'gems':20, 'raremetals':80, 'oil':10} , 'Tech':{'level': 3, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0, 'moveLimit':2} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmoves' : []}
SOUTHAFRICA   = {'Score': 0, 'Finance':{'wealth': 1000,  'gold':90, 'gems':70, 'raremetals':10, 'oil':60} , 'Tech':{'level': 2, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0, 'moveLimit':2} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmoves' : []}
PAKISTAN      = {'Score': 0, 'Finance':{'wealth': 1000,  'gold':80, 'gems':0, 'raremetals':10, 'oil':80} , 'Tech':{'level': 1, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0, 'moveLimit':2} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmoves' : []}
INDONESIA     = {'Score': 0, 'Finance':{'wealth': 1000,  'gold':40, 'gems':30, 'raremetals':40, 'oil':30} , 'Tech':{'level': 1, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0, 'moveLimit':2} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmoves' : []}
NIGERIA       = {'Score': 0, 'Finance':{'wealth': 1000,  'gold':80, 'gems':60, 'raremetals':0, 'oil':90} , 'Tech':{'level': 1, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0, 'moveLimit':2} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmoves' : []}
MEXICO        = {'Score': 0, 'Finance':{'wealth': 1000,  'gold':0, 'gems':30, 'raremetals':30, 'oil':90} , 'Tech':{'level': 1, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0, 'moveLimit':2} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmoves' : []}
EGYPT         = {'Score': 0, 'Finance':{'wealth': 1000,  'gold':120, 'gems':0, 'raremetals':0, 'oil':110} , 'Tech':{'level': 1, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0, 'moveLimit':2} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmoves' : []}
VIETNAM       = {'Score': 0, 'Finance':{'wealth': 1000,  'gold':20, 'gems':20, 'raremetals':130, 'oil':30} , 'Tech':{'level': 1, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0, 'moveLimit':2} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmoves' : []}
IRAN          = {'Score': 0, 'Finance':{'wealth': 1000,  'gold':120, 'gems':10, 'raremetals':0, 'oil':180} , 'Tech':{'level': 1, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0, 'moveLimit':2} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmoves' : []}
KENYA         = {'Score': 0, 'Finance':{'wealth': 1000,  'gold':100, 'gems':70, 'raremetals':10, 'oil':80} , 'Tech':{'level': 1, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0, 'moveLimit':2} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmoves' : []}
#TURKEY 	      = {'Score': 0, 'Finance':{'wealth': 8} , 'Tech':{'level': 0, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmove' : 'pass'}
#ETHIOPA       = {'Score': 0, 'Finance':{'wealth': 8} , 'Tech':{'level': 0, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmove' : 'pass'}
#PHILIPPINES   = {'Score': 0, 'Finance':{'wealth': 8} , 'Tech':{'level': 0, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmove' : 'pass'}
#BANGLADESH    = {'Score': 0, 'Finance':{'wealth': 8} , 'Tech':{'level': 0, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmove' : 'pass'}

# PRice is % of remaining available 
PRICE_TRACKER = {'gold': {'price': 120, 'stock': 10000, 'available': 3000},'raremetals': {'price': 60, 'stock': 2000, 'available': 3000}, 'gems': {'price': 250, 'stock': 2000, 'available': 3000}, 'oil': {'price': 12, 'stock': 10000, 'available': 3000}}

NATION_ARRAY = [[USA,'USA'],[CHINA,'CHINA'],[INDIA,'INDIA'],[RUSSIA,'RUSSIA'],[UK,'UK'],[GERMANY,'GERMANY'],[ITALY,'ITALY'],[SPAIN,'SPAIN'],[FRANCE,'FRANCE'],[JAPAN,'JAPAN'],[BRAZIL,'BRAZIL'],[SOUTHKOREA,'SOUTHKOREA'],[SOUTHAFRICA,'SOUTHAFRICA'],[PAKISTAN,'PAKISTAN'],[INDONESIA,'INDONESIA'],[NIGERIA,'NIGERIA'],[MEXICO,'MEXICO'],[EGYPT,'EGYPT'],[VIETNAM,'VIETNAM'],[IRAN,'IRAN'],[KENYA,'KENYA']]


myNation = ''
buffer = ''
p = 'All'

# Applies to AI move and Menu



"""
# =======================================================================
# =======================================================================
# STARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTART
# =======================================================================
#                           FUNCTIONS
#     FUNCTION selectNation
#     FUNCTION stats
#     FUNCTION music
#     PROCEEDURE start game
# =======================================================================
# STARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTART
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


def stats():
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
			myNation,myNationIndex =selectNation(NATION_ARRAY)
		fast_print('Starting game... \n')
		clearScreen()
		break
	if selection == 2:
		myNation,myNationIndex = selectNation(NATION_ARRAY)
	if selection == 3:
		stats()
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
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
#                              END SECTION
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
"""














"""
# =======================================================================
# =======================================================================
# GAME-STARTGAME-STARTGAME-STARTGAME-STARTGAME-STARTGAME-STARTGAME-START
# =======================================================================
#
#                           INTRO GAME START
#     1. CHECK GAME LOADED FLAG
#     2. LOAD GAME IF FLAG SET
#     3. GET USER NAME
#     4. INTRO SCENE
# =======================================================================
# =======================================================================
# GAME-STARTGAME-STARTGAME-STARTGAME-STARTGAME-STARTGAME-STARTGAME-START
# =======================================================================
"""


gameLoaded = False

if gameLoaded:
	print('Welcome back commander')


year = 1949

# MUST UNCOMENT FOR FULL GAME

from intro import start as start
userName = 'DonnerKebab'
#userName = start(userName,myNation)




import finance as fin 
import warMenu as warMenu
import politics as politics











"""
# FUNCTIONS FUNCTIONS FUNCTIONS FUNCTIONS FUNCTIONS FUNCTIONS FUNCTIONS 
# =====================================================================
#                          FUNCTIONS FUNCTIONS 
# =====================================================================
# =====================================================================
"""

def setAIMoves(index,currentNation,NATION_ARRAY):

	# Capping AI at one for now 
	moveLimit = str(currentNation[0]['Special']['moveLimit'])
	moveLimit = 1

	for moveNumber in range(0, moveLimit):
		choiceArray = ['gamble', 'pass']
		chosenArray = []


		# GAMBLE
		gambleAction = random.randint(0,6)
		if gambleAction > 2:
			creditsAvailable = int(currentNation[0]['Finance']['wealth'])

			if creditsAvailable > 1:
				amount = random.randint(1,creditsAvailable)
				NATION_ARRAY[index][0]['Finance']['wealth'] = NATION_ARRAY[index][0]['Finance']['wealth'] - amount
				NATION_ARRAY[index][0]['Nextmoves'] = NATION_ARRAY[index][0]['Nextmoves'] + [['gamble',amount]]


	# If No moves, then pass
	if len(NATION_ARRAY[index][0]['Nextmoves']) == 0:
		NATION_ARRAY[index][0]['Nextmoves']= [['pass']]
		
	return(NATION_ARRAY)







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
			preferencePrint(str(str(currentNation[1]) + ' chose to buy ' + str(amount) + ' ' + str(commodity)),p,index,myNationIndex)

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
		
 







#ENDROUNDENDROUNDENDROUNDENDROUNDENDROUND 
#       EEEE N    N DD
#       E    N N  N D D
#       EEEE N  N N D  D
#       E    N  N N D  D
#       EEEE N    N DD
#ENDROUNDENDROUNDENDROUNDENDROUNDENDROUND




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
def nextYear(year,myNation,NATION_ARRAY,myNationIndex,PRICE_TRACKER):
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
			NATION_ARRAY = setAIMoves(index,currentNation,NATION_ARRAY) 


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
		if new > original:
			PRICE_TRACKER[item]['price'] = round(PRICE_TRACKER[item]['price']  - (PRICE_TRACKER[item]['price'] * difference))
		if new < original:
			difference = - difference
			PRICE_TRACKER[item]['price'] = round(PRICE_TRACKER[item]['price']  + (PRICE_TRACKER[item]['price'] * difference))

		PRICE_TRACKER[item]['price'] = round(PRICE_TRACKER[item]['price'] + (PRICE_TRACKER[item]['price'] * (1/random.randint(8,12)))) # random variation    
    
	input(PRICE_TRACKER)


	print('FUNCTION TO CHECK WHEN STOCK IS 10% AND PUT ALERTS')


	year = year + 1
	print('*Hint* You can change how much you see in the options menu')
	print('')
	print('')
	buffer = input('Press enter to continue \n')
	return(year, NATION_ARRAY,PRICE_TRACKER)
	




"""
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
#
#                              END SECTION
#
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
"""






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



menuSelection = ' '
while menuSelection != 'E':
	clearScreen()
	print('*****************MENU*******************')
	print('')
	print('My Team: ' + str(myNation[1]))
	print('Year: ' + str(year))
	print('Rank: ' + 'Junior')
	print('')
	print('[1] View Leaderboard')
	print('[2] Finance Beuro')
	print('[3] Ministry of War (not available)')
	print('[4] Political Cabinet (not available)')
	print('[5] Next Year')
	print(' ')
	print(' ')
	print('[O] Options')
	print('[X] Exit')
	print(' ')
	print('****************************************')
	print(' ')
	print(' ')
	menuSelection = str(input('What would you like to do ' + str(userName) + '? \n')).upper()
	
	if menuSelection == '1':
		stats()
	if menuSelection == '2':
		myNation = fin.financeBeuro(myNation,year,PRICE_TRACKER)
	if menuSelection == '3':
		myNation = warMenu.warMinistry(myNation,year,PRICE_TRACKER)
	if menuSelection == '4':
		myNation = politics.politicalCabinet(myNation,year,PRICE_TRACKER)
	if menuSelection == '5' or menuSelection == '':
		year, NATION_ARRAY,PRICE_TRACKER = nextYear(year,myNation,NATION_ARRAY,myNationIndex,PRICE_TRACKER)
	if menuSelection == 'O':
		p = options(p)
	if menuSelection == 'X':
		exit()
		
print('it should process all at same time..')















