
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

# IMPORT UNIVERSAL UTILITIES
from conquest_utilities import slow_print as slow_print
from conquest_utilities import med_print as med_print
from conquest_utilities import fast_print as fast_print
from conquest_utilities import superfast_print as superfast_print
from conquest_utilities import clearScreen as clearScreen
from conquest_utilities import preferencePrint as preferencePrint
from conquest_utilities import options as options
from conquest_utilities import music as music

# FUNCTIONS
from functions import selectNation as selectNation
from functions import stats as stats
from actionFunctions import action as action
from actionFunctions import nextYear as nextYear
from actionFunctions import setAIMoves as setAIMoves

# CUSTOM MENUES
import finance as fin 
import warMenu as warMenu
import politics as politics




"""
# ---------------------------------------------------------------------
# END UTILITIES
# ---------------------------------------------------------------------
"""

USA           = {'Score': 0, 'Finance':{'wealth': 10000, 'gold':120, 'gems':30, 'raremetals':10, 'oil':200} , 'Tech':{'level': 3, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0, 'moveLimit':2, 'agression':70, 'innovation':80, 'materialism':70, 'prudence':30} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmoves' : []}
CHINA         = {'Score': 0, 'Finance':{'wealth': 8000,  'gold':40, 'gems':20, 'raremetals':200, 'oil':20}  , 'Tech':{'level': 4, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0, 'moveLimit':2, 'agression':70, 'innovation':30, 'materialism':90, 'prudence':60} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmoves' : []}
INDIA         = {'Score': 0, 'Finance':{'wealth': 3000,  'gold':100, 'gems':30, 'raremetals':30, 'oil':20}  , 'Tech':{'level': 3, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0, 'moveLimit':2, 'agression':40, 'innovation':30, 'materialism':20, 'prudence':50} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmoves' : []}
RUSSIA        = {'Score': 0, 'Finance':{'wealth': 2000,  'gold':50, 'gems':10, 'raremetals':20, 'oil':200}  , 'Tech':{'level': 2, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0, 'moveLimit':2, 'agression':80, 'innovation':20, 'materialism':60, 'prudence':40} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmoves' : []}
UK            = {'Score': 0, 'Finance':{'wealth': 2000,  'gold':90, 'gems':10, 'raremetals':0, 'oil':120}   , 'Tech':{'level': 3, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0, 'moveLimit':2, 'agression':60, 'innovation':70, 'materialism':65, 'prudence':50} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmoves' : []}
GERMANY       = {'Score': 0, 'Finance':{'wealth': 2000,  'gold':50, 'gems':10, 'raremetals':30, 'oil':10}   , 'Tech':{'level': 3, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0, 'moveLimit':2, 'agression':40, 'innovation':70, 'materialism':60, 'prudence':40} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmoves' : []}
ITALY 		  = {'Score': 0, 'Finance':{'wealth': 2000,  'gold':80, 'gems':20, 'raremetals':0, 'oil':30}    , 'Tech':{'level': 3, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0, 'moveLimit':2, 'agression':50, 'innovation':70, 'materialism':60, 'prudence':50} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmoves' : []}
SPAIN 		  = {'Score': 0, 'Finance':{'wealth': 2000,  'gold':90, 'gems':20, 'raremetals':10, 'oil':20}   , 'Tech':{'level': 3, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0, 'moveLimit':2, 'agression':50, 'innovation':70, 'materialism':50, 'prudence':60} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmoves' : []}
FRANCE        = {'Score': 0, 'Finance':{'wealth': 2000,  'gold':80, 'gems':50, 'raremetals':10, 'oil':10}   , 'Tech':{'level': 3, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0, 'moveLimit':2, 'agression':60, 'innovation':70, 'materialism':40, 'prudence':50} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmoves' : []}
JAPAN         = {'Score': 0, 'Finance':{'wealth': 2000,  'gold':70, 'gems':20, 'raremetals':100, 'oil':20}  , 'Tech':{'level': 3, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0, 'moveLimit':2, 'agression':30, 'innovation':70, 'materialism':40, 'prudence':40} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmoves' : []}
BRAZIL        = {'Score': 0, 'Finance':{'wealth': 1000,  'gold':30, 'gems':30, 'raremetals':30, 'oil':80}   , 'Tech':{'level': 2, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0, 'moveLimit':2, 'agression':60, 'innovation':70, 'materialism':70, 'prudence':70} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmoves' : []}
SOUTHKOREA    = {'Score': 0, 'Finance':{'wealth': 2000,  'gold':50, 'gems':20, 'raremetals':80, 'oil':10}   , 'Tech':{'level': 3, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0, 'moveLimit':2, 'agression':40, 'innovation':70, 'materialism':40, 'prudence':60} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmoves' : []}
SOUTHAFRICA   = {'Score': 0, 'Finance':{'wealth': 1000,  'gold':90, 'gems':70, 'raremetals':10, 'oil':60}   , 'Tech':{'level': 2, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0, 'moveLimit':2, 'agression':40, 'innovation':70, 'materialism':70, 'prudence':50} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmoves' : []}
PAKISTAN      = {'Score': 0, 'Finance':{'wealth': 1000,  'gold':80, 'gems':0, 'raremetals':10, 'oil':80}    , 'Tech':{'level': 1, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0, 'moveLimit':2, 'agression':70, 'innovation':70, 'materialism':100, 'prudence':40} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmoves' : []}
INDONESIA     = {'Score': 0, 'Finance':{'wealth': 1000,  'gold':40, 'gems':30, 'raremetals':40, 'oil':30}   , 'Tech':{'level': 1, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0, 'moveLimit':2, 'agression':40, 'innovation':70, 'materialism':70, 'prudence':60} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmoves' : []}
NIGERIA       = {'Score': 0, 'Finance':{'wealth': 1000,  'gold':80, 'gems':60, 'raremetals':0, 'oil':90}    , 'Tech':{'level': 1, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0, 'moveLimit':2, 'agression':40, 'innovation':70, 'materialism':80, 'prudence':55} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmoves' : []}
MEXICO        = {'Score': 0, 'Finance':{'wealth': 1000,  'gold':0,  'gems':30, 'raremetals':30, 'oil':90}   , 'Tech':{'level': 1, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0, 'moveLimit':2, 'agression':50, 'innovation':70, 'materialism':70, 'prudence':40} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmoves' : []}
EGYPT         = {'Score': 0, 'Finance':{'wealth': 1000,  'gold':120, 'gems':0, 'raremetals':0, 'oil':110}   , 'Tech':{'level': 1, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0, 'moveLimit':2, 'agression':60, 'innovation':70, 'materialism':300, 'prudence':65} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmoves' : []}
VIETNAM       = {'Score': 0, 'Finance':{'wealth': 1000,  'gold':20, 'gems':20, 'raremetals':130, 'oil':30}  , 'Tech':{'level': 1, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0, 'moveLimit':2, 'agression':40, 'innovation':70, 'materialism':70, 'prudence':45} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmoves' : []}
IRAN          = {'Score': 0, 'Finance':{'wealth': 1000,  'gold':120, 'gems':10, 'raremetals':0, 'oil':180}  , 'Tech':{'level': 1, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0, 'moveLimit':2, 'agression':70, 'innovation':70, 'materialism':20, 'prudence':50} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmoves' : []}
KENYA         = {'Score': 0, 'Finance':{'wealth': 1000,  'gold':100, 'gems':70, 'raremetals':10, 'oil':80}  , 'Tech':{'level': 1, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0, 'moveLimit':2, 'agression':50, 'innovation':70, 'materialism':70, 'prudence':45} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmoves' : []}
#TURKEY 	      = {'Score': 0, 'Finance':{'wealth': 8} , 'Tech':{'level': 0, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmove' : 'pass'}
#ETHIOPA       = {'Score': 0, 'Finance':{'wealth': 8} , 'Tech':{'level': 0, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmove' : 'pass'}
#PHILIPPINES   = {'Score': 0, 'Finance':{'wealth': 8} , 'Tech':{'level': 0, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmove' : 'pass'}
#BANGLADESH    = {'Score': 0, 'Finance':{'wealth': 8} , 'Tech':{'level': 0, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmove' : 'pass'}

# PRice is % of remaining available 
PRICE_TRACKER = {'gold': {'price': 120, 'stock': 10000, 'priceChange': 0},'raremetals': {'price': 60, 'stock': 2000, 'priceChange': 0}, 'gems': {'price': 250, 'stock': 2000, 'priceChange': 0}, 'oil': {'price': 12, 'stock': 10000, 'priceChange': 0}}

NATION_ARRAY = [[USA,'USA'],[CHINA,'CHINA'],[INDIA,'INDIA'],[RUSSIA,'RUSSIA'],[UK,'UK'],[GERMANY,'GERMANY'],[ITALY,'ITALY'],[SPAIN,'SPAIN'],[FRANCE,'FRANCE'],[JAPAN,'JAPAN'],[BRAZIL,'BRAZIL'],[SOUTHKOREA,'SOUTHKOREA'],[SOUTHAFRICA,'SOUTHAFRICA'],[PAKISTAN,'PAKISTAN'],[INDONESIA,'INDONESIA'],[NIGERIA,'NIGERIA'],[MEXICO,'MEXICO'],[EGYPT,'EGYPT'],[VIETNAM,'VIETNAM'],[IRAN,'IRAN'],[KENYA,'KENYA']]


myNation = ''
buffer = ''
p = 'All'

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
			myNation,myNationIndex =selectNation(NATION_ARRAY)
		fast_print('Starting game... \n')
		clearScreen()
		break
	if selection == 2:
		myNation,myNationIndex = selectNation(NATION_ARRAY)
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

from intro import start as start
userName = 'DonnerKebab'
userName = start(userName,myNation)






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
		stats(NATION_ARRAY)
	if menuSelection == '2':
		myNation = fin.financeBeuro(myNation,year,PRICE_TRACKER)
	if menuSelection == '3':
		myNation = warMenu.warMinistry(myNation,year,PRICE_TRACKER)
	if menuSelection == '4':
		myNation = politics.politicalCabinet(myNation,year,PRICE_TRACKER)
	if menuSelection == '5' or menuSelection == '':
		year, NATION_ARRAY,PRICE_TRACKER = nextYear(year,myNation,NATION_ARRAY,myNationIndex,PRICE_TRACKER,p)
	if menuSelection == 'O':
		p = options(p)
	if menuSelection == 'X':
		exit()
		
print('it should process all at same time..')















