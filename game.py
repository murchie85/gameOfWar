
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
import random

# BUFFER PRINT

def slow_print(s):
	for c in s:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.2)


def med_print(s):
	for c in s:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.10)

def fast_print(s):
	for c in s:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.03)

def superfast_print(s):
	for c in s:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.005)

def clearScreen():
	for x in range(0,70):
		print('')

def preferencePrint(s,p,i):
	if p == 'All':
		print(s)
	if p == 'Me':
		if str(i) == str(myNationIndex):
			print(s)
	if p == 'None':
		pass

"""
# ---------------------------------------------------------------------
# END UTILITIES
# ---------------------------------------------------------------------
"""





USA           = {'Score': 20, 'Finance':{'wealth': 10, 'gold':120, 'gems':30, 'raremetals':10, 'oil':200} , 'Tech':{'level': 3, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmove' : 'pass'}
CHINA         = {'Score': 19, 'Finance':{'wealth': 8,  'gold':40, 'gems':20, 'raremetals':200, 'oil':20} , 'Tech':{'level': 4, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmove' : 'pass'}
INDIA         = {'Score': 18, 'Finance':{'wealth': 3,  'gold':1000, 'gems':30, 'raremetals':30, 'oil':20} , 'Tech':{'level': 3, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmove' : 'pass'}
RUSSIA        = {'Score': 17, 'Finance':{'wealth': 2,  'gold':50, 'gems':10, 'raremetals':20, 'oil':200} , 'Tech':{'level': 2, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmove' : 'pass'}
UK            = {'Score': 16, 'Finance':{'wealth': 2,  'gold':90, 'gems':10, 'raremetals':0, 'oil':120} , 'Tech':{'level': 3, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmove' : 'pass'}
GERMANY       = {'Score': 15, 'Finance':{'wealth': 2,  'gold':50, 'gems':10, 'raremetals':30, 'oil':10} , 'Tech':{'level': 3, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmove' : 'pass'}
ITALY 		  = {'Score': 14, 'Finance':{'wealth': 2,  'gold':80, 'gems':20, 'raremetals':0, 'oil':30} , 'Tech':{'level': 3, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmove' : 'pass'}
SPAIN 		  = {'Score': 13, 'Finance':{'wealth': 2,  'gold':90, 'gems':20, 'raremetals':10, 'oil':20} , 'Tech':{'level': 3, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmove' : 'pass'}
FRANCE        = {'Score': 12, 'Finance':{'wealth': 2,  'gold':80, 'gems':50, 'raremetals':10, 'oil':10} , 'Tech':{'level': 3, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmove' : 'pass'}
JAPAN         = {'Score': 11, 'Finance':{'wealth': 2,  'gold':70, 'gems':20, 'raremetals':100, 'oil':20} , 'Tech':{'level': 3, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmove' : 'pass'}
BRAZIL        = {'Score': 10, 'Finance':{'wealth': 1,  'gold':30, 'gems':30, 'raremetals':30, 'oil':80} , 'Tech':{'level': 2, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmove' : 'pass'}
SOUTHKOREA    = {'Score': 9, 'Finance':{'wealth': 2,  'gold':50, 'gems':20, 'raremetals':80, 'oil':10} , 'Tech':{'level': 3, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmove' : 'pass'}
SOUTHAFRICA   = {'Score': 8, 'Finance':{'wealth': 1,  'gold':90, 'gems':120, 'raremetals':10, 'oil':60} , 'Tech':{'level': 2, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmove' : 'pass'}
PAKISTAN      = {'Score': 7, 'Finance':{'wealth': 1,  'gold':80, 'gems':0, 'raremetals':10, 'oil':80} , 'Tech':{'level': 1, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmove' : 'pass'}
INDONESIA     = {'Score': 6, 'Finance':{'wealth': 1,  'gold':40, 'gems':30, 'raremetals':40, 'oil':30} , 'Tech':{'level': 1, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmove' : 'pass'}
NIGERIA       = {'Score': 5, 'Finance':{'wealth': 1,  'gold':80, 'gems':110, 'raremetals':0, 'oil':90} , 'Tech':{'level': 1, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmove' : 'pass'}
MEXICO        = {'Score': 4, 'Finance':{'wealth': 1,  'gold':0, 'gems':30, 'raremetals':30, 'oil':90} , 'Tech':{'level': 1, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmove' : 'pass'}
EGYPT         = {'Score': 3, 'Finance':{'wealth': 1,  'gold':120, 'gems':0, 'raremetals':0, 'oil':110} , 'Tech':{'level': 1, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmove' : 'pass'}
VIETNAM       = {'Score': 2, 'Finance':{'wealth': 1,  'gold':20, 'gems':20, 'raremetals':130, 'oil':30} , 'Tech':{'level': 1, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmove' : 'pass'}
IRAN          = {'Score': 1, 'Finance':{'wealth': 1,  'gold':120, 'gems':10, 'raremetals':0, 'oil':180} , 'Tech':{'level': 1, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmove' : 'pass'}
KENYA         = {'Score': 1, 'Finance':{'wealth': 1,  'gold':100, 'gems':100, 'raremetals':10, 'oil':80} , 'Tech':{'level': 1, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmove' : 'pass'}
#TURKEY 	      = {'Score': 0, 'Finance':{'wealth': 8} , 'Tech':{'level': 0, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmove' : 'pass'}
#ETHIOPA       = {'Score': 0, 'Finance':{'wealth': 8} , 'Tech':{'level': 0, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmove' : 'pass'}
#PHILIPPINES   = {'Score': 0, 'Finance':{'wealth': 8} , 'Tech':{'level': 0, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmove' : 'pass'}
#BANGLADESH    = {'Score': 0, 'Finance':{'wealth': 8} , 'Tech':{'level': 0, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmove' : 'pass'}

SYSTEM_TRACKER = {'gold': {'price': 100, 'stock': 10000},'raremetals': {'price': 100, 'stock': 10000}, 'gems': {'price': 100, 'stock': 10000}, 'oil': {'price': 100, 'stock': 10000}}

NATION_ARRAY = [[USA,'USA'],[CHINA,'CHINA'],[INDIA,'INDIA'],[RUSSIA,'RUSSIA'],[UK,'UK'],[GERMANY,'GERMANY'],[ITALY,'ITALY'],[SPAIN,'SPAIN'],[FRANCE,'FRANCE'],[JAPAN,'JAPAN'],[BRAZIL,'BRAZIL'],[SOUTHKOREA,'SOUTHKOREA'],[SOUTHAFRICA,'SOUTHAFRICA'],[PAKISTAN,'PAKISTAN'],[INDONESIA,'INDONESIA'],[NIGERIA,'NIGERIA'],[MEXICO,'MEXICO'],[EGYPT,'EGYPT'],[VIETNAM,'VIETNAM'],[IRAN,'IRAN'],[KENYA,'KENYA']]


myNation = ''
buffer = ''
p = 'All'

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




"""
# ---------------------------------------------------------------------
# SUB MENU SUB MENU SUB MENU SUB MENU SUB MENU SUB MENU SUB MENU SUB MENU
# ---------------------------------------------------------------------
#                      SUB MENU
# ---------------------------------------------------------------------
# SUB MENU SUB MENU SUB MENU SUB MENU SUB MENU SUB MENU SUB MENU SUB MENU
# ---------------------------------------------------------------------
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
		buffer = input('Press any button to continue \n')
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

	buffer = input('Press any button to continue \n')
	clearScreen()


def music():
	import webbrowser
	clearScreen()
	fast_print('This will open music in your webbrowser. \n' )
	print('')
	print('1. Game Music')
	print('2. SciFi Chill')
	print('3. LO FI')
	print('4. Trappin')
	print('5. Relaxed Gaming Music')
	print('6. 70s Japanese')
	print('7. Asian Pop')
	print('8. Exit')
	print('')
	print('')

	decision = str(input('Please select an option. \n'))

	if decision == '1':
		fast_print('Opening browser window, remember to come back!')
		webbrowser.open('https://youtu.be/H8w_Q57RQJc')
	if decision == '2':
		fast_print('Opening browser window, remember to come back!')
		webbrowser.open('https://youtu.be/B0PGvSA5f7k')
	if decision == '3':
		fast_print('Opening browser window, remember to come back!')
		webbrowser.open('https://youtu.be/_fVjJmX2GYs')
	if decision == '4':
		fast_print('Opening browser window, remember to come back!')
		webbrowser.open('https://youtu.be/rehF0Df2DIc')
	if decision == '5':
		fast_print('Opening browser window, remember to come back!')
		webbrowser.open('https://youtu.be/tghXpPpHHJ4')
	if decision == '6':
		fast_print('Opening browser window, remember to come back!')
		webbrowser.open('https://youtu.be/E4s-hxY80pA')
	if decision == '7':
		fast_print('Opening browser window, remember to come back!')	
		webbrowser.open('https://www.youtube.com/watch?v=w0dMz8RBG7g&list=PL0B70C9C2654CEED6&index=2Asian Classic')
	if decision == '8':
		fast_print('Exiting')
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
		med_print('Starting game... \n')
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
		buffer = input('Press any button to continue \n ')
		clearScreen()
	if selection == 5:
		fast_print('All credits go to Adam McMurchie... me! . \n')
		buffer = input('Press any button to continue \n ')
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

userName = 'DonnerKebab'
# assistant = 'Arbiter: '
# fast_print('**rustle**....**clunk** ..."oh not again!" \n')
# fast_print(str(assistant) + '....wait... \n')
# time.sleep(0.7)
# fast_print(str(assistant) +'..who the hell are you? How did you get in here? ... \n')

# userName = input('Enter your name \n')
# print(' ')
# med_print(str(userName) + ': ... im ' + str(userName) + '\n')

# fast_print(str(assistant) + 'ah, so YOU are the one. \n')
# time.sleep(0.4)
# fast_print(str(assistant) + 'Its truly an honour to meet you ' + str(userName) +  ' please know that we all appreciate your sacrifice  \n')
# fast_print(str(assistant) + '...are you ready?  \n ')
# print('')
# input(' Press any key to start..')
# fast_print(str(assistant) + 'executing dynamic cascade sequence now, this should feel... uh..uh....  \n ')
# time.sleep(0.6)
# fast_print('....a little weird \n ')
# time.sleep(1.50)
# clearScreen()
# time.sleep(1.50)

# for y in range(0,3):
#     for x in range(0,10):
#         print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
#     time.sleep(0.50)
# fast_print('..........universe destruction in progress......\n')
# for x in range(0,10):
#     print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
# time.sleep(0.50)
# for x in range(0,10):
#     print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
# time.sleep(0.50)
# for x in range(0,10):
#     print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
# fast_print('....booting up universe simulation #16725 omega .......\n')
# for y in range(0,3):
#     for x in range(0,10):
#         print('><><><>><><><>><><><>><><><>><><><>><><><>><><><>><><><')
#     time.sleep(0.50)
# time.sleep(0.580)
# for y in range(0,3):
#     for x in range(0,5):
#         print('asklfdj;l;j;adfj;kj;afdkjaklsdjfaghaldg;asdkjf;lkja;ajd')
#     time.sleep(0.30)
#     for x in range(0,5):
#         print('skakdf 9873472393khgfas lalsdjhf lkladf iuhwer 82348989')
#     time.sleep(0.30)
#     for x in range(0,5):
#         print('sweir;nvda;eradf jasd;klfjasfjghlaadsljfh lasdhfhdlafdd')
#     time.sleep(0.50)
# for y in range(0,3):
#     for x in range(0,10):
#         print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
#     time.sleep(0.50)
# clearScreen()
# time.sleep(1.10)
# med_print('....Lead me, follow me, or get out of my way ........ \n')
# print('(George S Patton)')
# time.sleep(1.90)
# clearScreen()
# for x in range(0,20):
#     print(' ')
# time.sleep(0.50)
# print('')
# y = 5
# for x in range(0, 5):
#     print(str(y))
#     y= y-1
#     time.sleep(1.20)
#     clearScreen()



# fast_print('Good morning commander ' + str(userName) + '..... \n')
# fast_print('')
# time.sleep(0.80)
# fast_print('The year is 1949, the devestating and costly war has finally come to an end.\nIt is your responsibility to lead ' + str(myNation[-1]) + ' to greatness. \n')
# time.sleep(0.80)
# fast_print('There are many ways to win, trade, politics, war....the path is up to you? \n')
# time.sleep(1.50)

"""
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
#                              END SECTION
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
"""























"""
# =======================================================================
# =======================================================================
# MAIN MENU MAIN MENU MAIN MENU MAIN MENU MAIN MENU MAIN MENU MAIN MENU 
# =======================================================================
#                           MAIN MENU MODE 
#     1. SELECT NATION OPTION
#     2. VIEW COUNTRY
#     3. VIEW RULES
#     4. VIEW CREDITS
#     5. START GAME 
# =======================================================================
# MAIN MENU MAIN MENU MAIN MENU MAIN MENU MAIN MENU MAIN MENU MAIN MENU
# =======================================================================
"""





"""
# SUBMENUSUBMENUSUBMENUSUBMENUSUBMENUSUBMENUSUBMENUSUBMENUSUBMENUSUBMENU
# =====================================================================
#                           SUB MENU
# =====================================================================
# =====================================================================
"""

"""
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#                           FINANCEBEURO
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
"""
def financeBeuro(NATION_ARRAY):
	clearScreen()
	financeSelection = ' '
	while financeSelection != '':
		print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
		print('        WELCOME TO THE FINANCE BEURO   😊        ')
		print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
		print('')
		print('My Team: ' + str(myNation[1]))
		print('Wealth : ' + str(myNation[0]['Finance']['wealth']) )
		print('Year: ' + str(year))
		print('')
		print('[1] Gamble')
		print('[2] Trade Exchange')
		print('[3] Exit')
		print(' ')
		print(' ')
		print('****************************************')
		print(' ')
		print(' ')
		financeSelection = str(input('Please chose an option \n'))
		print(financeSelection)
		if financeSelection == '1':
			skipflag = gambleSelect(NATION_ARRAY)
		if financeSelection == '2':
			skipflag = tradeSelect(NATION_ARRAY)
		if financeSelection == '3':
			print('exiting...')
			break
	return(NATION_ARRAY)

			

def gambleSelect(NATION_ARRAY):
	clearScreen()
	print('My Team: ' + str(myNation[1]))
	print('Year: ' + str(year))
	print('Trade Credits: ' + str(myNation[0]['Finance']['wealth']))
	print(' ')
	print('')
	
	
	flag = 0
	creditsAvailable = int(myNation[0]['Finance']['wealth'])
	gambleAmount = 0

	if creditsAvailable < 1:
		print('you do not have enough credits, sorry')
		flag = 1

	if flag == 1:
		print('you do not have enough credits, exiting, sorry')
		return

	fast_print('How much do you wish to gamble? \n')
	while gambleAmount < 1:
		try:
			gambleAmount = int(input('Input amount between 1 and ' + str(creditsAvailable) + '\n'))
		except:
			print("Entered incorrectly, please try again")
	
	if gambleAmount > creditsAvailable:
		fast_print('Entered too much')
		return

	# Decrement wealth now.
	myNation[0]['Finance']['wealth'] = myNation[0]['Finance']['wealth'] - gambleAmount
	myNation[0]['Nextmove'] = 'gamble',gambleAmount
	print('You will gamble ' + str(myNation[0]['Nextmove'][1]) + ' in the next round')
	buffer = input('press any key to continue')
	skipflag = 'y'
	return(skipflag)
	



def buy(NATION_ARRAY):
	clearScreen()
	financeSelection = ' '
	while financeSelection != '':
		print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
		print('         💰💰💰  BUY BUY BUY      💰💰💰💰     ')
		print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
		print('')
		print('My Team: ' + str(myNation[1]))
		print('Year: ' + str(year))
		print('Wealth : ' + str(myNation[0]['Finance']['wealth']))
		print('Stash: ' + str(myNation[0]['Finance']['gold']) + ' : ' + str(myNation[0]['Finance']['gems']) + ' : ' + str(myNation[0]['Finance']['raremetals'])  + ' : ' + str(myNation[0]['Finance']['oil'])  ) 
		print('')
		print('Gold        : ' + '$200')
		print('Gems        : ' + '$300')
		print('Rare Metals : ' + '$20')
		print('Oil         : ' + '$10')
		print('')
		print('[1] Buy Gold')
		print('[2] Buy Gems')
		print('[3] Buy Metals')
		print('[4] Buy Oil')
		print('')
		print('')
		print('[R] Return')
		print('[M] Main Menu')
		print(' ')
		print(' ')
		print('***************************************************')
		print(' ')
		print(' ')
		financeSelection = str(input('Please chose an option \n'))
		print(financeSelection)
		if financeSelection == '1':

			# buy funcion 
			# (item, price, credits)
			# max = round(credits/price) down
			# input('How many do you want to buy? ' )
			fast_print('Bought Gold')
			print('')
		if financeSelection == '2':
			fast_print('Bought Gems')
			print('')
		if financeSelection == '3':
			print('exiting...')
			break
		if financeSelection == 'R' or financeSelection == 'r':
			break
		if financeSelection == 'M' or financeSelection == 'm':
			print('exiting...')
			return('M') 





def tradeSelect(NATION_ARRAY):
	clearScreen()
	financeSelection = ' '
	while financeSelection != '':
		print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
		print('         💰💰💰  TRADE EXCHANGE   💰💰💰💰     ')
		print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
		print('')
		print('My Team: ' + str(myNation[1]))
		print('Year: ' + str(year))
		print('Wealth : ' + str(myNation[0]['Finance']['wealth']))
		print('')
		print('Gold        : ' + str(myNation[0]['Finance']['gold']))
		print('Gems        : ' + str(myNation[0]['Finance']['gems']))
		print('Rare Metals : ' + str(myNation[0]['Finance']['raremetals']))
		print('Oil         : ' + str(myNation[0]['Finance']['oil']))
		print('')
		print('[1] Buy')
		print('[2] Sell')
		print('[3] Exit')
		print(' ')
		print(' ')
		print('***************************************************')
		print(' ')
		print(' ')
		financeSelection = str(input('Please chose an option \n'))
		print(financeSelection)
		if financeSelection == '1':
			flag = buy(NATION_ARRAY)
		if financeSelection == '2':
			fast_print('Chose to sell')
		if financeSelection == '3' or flag == 'M':
			print('exiting...')
			break













def warMinistry(NATION_ARRAY):
		print('+++++++++++++++++++++++++++++++++++++++++++++++++++')
		print('        WELCOME TO THE MINISTRY OF WAR   😊        ')
		print('+++++++++++++++++++++++++++++++++++++++++++++++++++')
		print('')
		print('My Team: ' + str(myNation[1]))
		print('Year: ' + str(year))
		print('')
		print('[1] Purchase Weapons')
		print('[2] Exit')
		print(' ')
		print(' ')
		print('****************************************')
		print(' ')
		print(' ')

def politicalCabinet(NATION_ARRAY):
	fast_print('This feature is not ready yet...')









"""
# END-SUBMENU END-SUBMENU END-SUBMENU END-SUBMENU END-SUBMENU END-SUBMENU 
# =====================================================================
#                          END  SUB MENU END
# =====================================================================
# =====================================================================
"""




"""
# ---------------------------------------------------------------------
#                           MAIN FUNCTIONS
# ---------------------------------------------------------------------
"""


def setAIMoves(index,currentNation,NATION_ARRAY):


	choiceArray = ['gamble', 'pass']

	# GAMBLE
	gambleAction = random.randint(0,4)
	# 25% CHANCE AI WILL GAMBLE
	if gambleAction > 2:
		amount = 999999999999
		creditsAvailable = int(currentNation[0]['Finance']['wealth'])

		# IF AI HAS NO CREDITS TO GAMBLE PASS, else make the gamble
		if creditsAvailable < 1:
			NATION_ARRAY[index][0]['Nextmove'] = 'pass'
		else:
			amount = random.randint(1,creditsAvailable)
			NATION_ARRAY[index][0]['Finance']['wealth'] = NATION_ARRAY[index][0]['Finance']['wealth'] - amount
			NATION_ARRAY[index][0]['Nextmove'] = 'gamble',amount

	else:
		NATION_ARRAY[index][0]['Nextmove'] = 'pass'
	return(NATION_ARRAY)







def action(index, currentNation,NATION_ARRAY,p):
	
	# PROCESS PASS
	if currentNation[0]['Nextmove'] == 'pass':
		preferencePrint(str(str(currentNation[1]) + ' chose to pass'),p,index)
		
	
	# PROCESS GAMBLE 
	if currentNation[0]['Nextmove'][0] == 'gamble':
		preferencePrint(str(str(currentNation[1]) + ' chose to gamble'),p,index)
		amount = currentNation[0]['Nextmove'][1] # the amount chosen to gamble
		originalFinanceScore = currentNation[0]['Finance']['wealth'] + amount
		winnings = random.randint((round(0.3*amount)), round(2*amount)) 

		NATION_ARRAY[index][0]['Finance']['wealth'] = NATION_ARRAY[index][0]['Finance']['wealth'] + winnings

		difference = NATION_ARRAY[index][0]['Finance']['wealth'] - originalFinanceScore  

		if difference > 0:
			preferencePrint(str(str(currentNation[1]) + ' gained  +' + str(difference)),p,index)
		elif difference < 0:
			preferencePrint(str(str(currentNation[1]) + ' lost  ' + str(difference)),p,index)
		else:
			preferencePrint(str(str(currentNation[1]) + ' broke even  ' + str(difference)),p,index)

		preferencePrint(str('Gambled         : ' + str(amount)),p,index)
		preferencePrint(str('Winnings        : ' + str(winnings)),p,index)
		preferencePrint(str('Finance credits : ' + str(NATION_ARRAY[index][0]['Finance']['wealth'] )),p,index)
	return(NATION_ARRAY)
		
 

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
		NATION_ARRAY[x][0]['Score'] = NATION_ARRAY[x][0]['Score'] + totalSubScores
	return(NATION_ARRAY)



# DEFAULTS ALL TEAM ACTIONS TO 'PASS'
def defaultNextStep(NATION_ARRAY):
	for x in range(0, len(NATION_ARRAY)):    
		NATION_ARRAY[x][0]['Nextmove'] = 'pass'
	return(NATION_ARRAY)



# END OF ROUND 
def nextYear(year,myNation,NATION_ARRAY):
	clearScreen()
	fast_print('Processing next year....')
	print('')

	# ITERATE FOR EACH TEAM 
	for x in range(0, len(NATION_ARRAY)):
		currentNation = NATION_ARRAY[x]
		index = x

		# AI TEAM DECISION
		if currentNation != myNation: 
			NATION_ARRAY = setAIMoves(index,currentNation,NATION_ARRAY) 


		# ACTION CARRIED OUT FOR ALL USERS
		NATION_ARRAY = action(index,currentNation,NATION_ARRAY,p)
		print('')
		print('')

	# Only talling scores at the end....may need to change
	print('Tallying scores')
	NATION_ARRAY = tallyScores(NATION_ARRAY)
	NATION_ARRAY = defaultNextStep(NATION_ARRAY)


	UPDATE_WEALTH_VALUATION = ' TO BE COMPLETED'

	year = year + 1
	print('*Hint* You can change how much you see in the options menu')
	print('')
	print('')
	buffer = input('Press any button to continue')
	return(year, NATION_ARRAY)
	




"""
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
#
#                              END SECTION
#
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
"""






def printupdates():
	print('Welcome...')
	print(' ')
	print('You can change what you want to see at the end of the round')
	print('[A]. All stats and country activities')
	print('[O]. Only my stuff')
	print('[D]. Dont show me anything' )
	p = str(input('Please select an option. \n')).upper()
	if p == 'A':
		p = 'All'
	elif p == 'O':
		p = 'Me'
	elif p == 'D':
		p = 'None'
	else:
		p = 'All'
	return(p)

def options():
	clearScreen()
	print('***************************************************')
	print('*                  OPTIONS                        *')
	print('***************************************************')
	print('')
	print('1. Select Music')
	print('2. Change End of Round Updates')

	selection = str(input('Please select an option \n'))
	if selection == '1':
		music()
	if selection == '2':
		p = printupdates()
		return(p)

"""
# =====================================================================
# =====================================================================
# =====================================================================
#                           MAIN MENU
#     1. View Leaderboard
#     2. Finance Beuro
#     3. Ministry of War (not available)
#     4. Political Cabinet (not available)
#     5. Next Year
# =====================================================================
# =====================================================================
# =====================================================================
"""


menuSelection = ' '
while menuSelection != '':
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
	print(' ')
	print('****************************************')
	print(' ')
	print(' ')
	menuSelection = str(input('What would you like to do ' + str(userName) + '? \n'))
	
	if menuSelection == '1':
		stats()
	if menuSelection == '2':
		NATION_ARRAY = financeBeuro(NATION_ARRAY)
	if menuSelection == '3':
		NATION_ARRAY = warMinistry(NATION_ARRAY)
	if menuSelection == '4':
		NATION_ARRAY = politicalCabinet(NATION_ARRAY)
	if menuSelection == '5':
		year, NATION_ARRAY = nextYear(year,myNation,NATION_ARRAY)
	if menuSelection == 'O' or menuSelection == 'o':
		p = options()
		
print('it should process all at same time..')















