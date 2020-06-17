
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

"""
# ---------------------------------------------------------------------
# END UTILITIES
# ---------------------------------------------------------------------
"""


maxPP = 23210
maxGDP = 19


USA           = {'Score': 0, 'Finance':{'wealth': 10} , 'Tech':{'level': 3, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmove' : 'pass'}
CHINA         = {'Score': 0, 'Finance':{'wealth': 8} , 'Tech':{'level': 4, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmove' : 'pass'}
INDIA         = {'Score': 0, 'Finance':{'wealth': 3} , 'Tech':{'level': 3, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmove' : 'pass'}
RUSSIA        = {'Score': 0, 'Finance':{'wealth': 2} , 'Tech':{'level': 2, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmove' : 'pass'}
UK            = {'Score': 0, 'Finance':{'wealth': 2} , 'Tech':{'level': 3, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmove' : 'pass'}
GERMANY       = {'Score': 0, 'Finance':{'wealth': 2} , 'Tech':{'level': 3, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmove' : 'pass'}
ITALY 		  = {'Score': 0, 'Finance':{'wealth': 2} , 'Tech':{'level': 3, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmove' : 'pass'}
SPAIN 		  = {'Score': 0, 'Finance':{'wealth': 2} , 'Tech':{'level': 3, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmove' : 'pass'}
FRANCE        = {'Score': 0, 'Finance':{'wealth': 2} , 'Tech':{'level': 3, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmove' : 'pass'}
JAPAN         = {'Score': 0, 'Finance':{'wealth': 2} , 'Tech':{'level': 3, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmove' : 'pass'}
BRAZIL        = {'Score': 0, 'Finance':{'wealth': 1} , 'Tech':{'level': 2, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmove' : 'pass'}
SOUTHKOREA    = {'Score': 0, 'Finance':{'wealth': 2} , 'Tech':{'level': 3, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmove' : 'pass'}
SOUTHAFRICA   = {'Score': 0, 'Finance':{'wealth': 1} , 'Tech':{'level': 2, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmove' : 'pass'}
PAKISTAN      = {'Score': 0, 'Finance':{'wealth': 1} , 'Tech':{'level': 1, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmove' : 'pass'}
INDONESIA     = {'Score': 0, 'Finance':{'wealth': 1} , 'Tech':{'level': 1, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmove' : 'pass'}
NIGERIA       = {'Score': 0, 'Finance':{'wealth': 1} , 'Tech':{'level': 1, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmove' : 'pass'}
MEXICO        = {'Score': 0, 'Finance':{'wealth': 1} , 'Tech':{'level': 1, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmove' : 'pass'}
EGYPT         = {'Score': 0, 'Finance':{'wealth': 1} , 'Tech':{'level': 1, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmove' : 'pass'}
VIETNAM       = {'Score': 0, 'Finance':{'wealth': 1} , 'Tech':{'level': 1, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmove' : 'pass'}
IRAN          = {'Score': 0, 'Finance':{'wealth': 1} , 'Tech':{'level': 1, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmove' : 'pass'}
KENYA         = {'Score': 0, 'Finance':{'wealth': 1} , 'Tech':{'level': 1, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmove' : 'pass'}
#TURKEY 	      = {'Score': 0, 'Finance':{'wealth': 8} , 'Tech':{'level': 0, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmove' : 'pass'}
#ETHIOPA       = {'Score': 0, 'Finance':{'wealth': 8} , 'Tech':{'level': 0, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmove' : 'pass'}
#PHILIPPINES   = {'Score': 0, 'Finance':{'wealth': 8} , 'Tech':{'level': 0, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmove' : 'pass'}
#BANGLADESH    = {'Score': 0, 'Finance':{'wealth': 8} , 'Tech':{'level': 0, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmove' : 'pass'}

NATION_ARRAY = [[USA,'USA'],[CHINA,'CHINA'],[INDIA,'INDIA'],[RUSSIA,'RUSSIA'],[UK,'UK'],[GERMANY,'GERMANY'],[ITALY,'ITALY'],[SPAIN,'SPAIN'],[FRANCE,'FRANCE'],[JAPAN,'JAPAN'],[BRAZIL,'BRAZIL'],[SOUTHKOREA,'SOUTHKOREA'],[SOUTHAFRICA,'SOUTHAFRICA'],[PAKISTAN,'PAKISTAN'],[INDONESIA,'INDONESIA'],[NIGERIA,'NIGERIA'],[MEXICO,'MEXICO'],[EGYPT,'EGYPT'],[VIETNAM,'VIETNAM'],[IRAN,'IRAN'],[KENYA,'KENYA']]


myNation = ''
buffer = ''

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
	    nationSelected = 'Y'
	return(myNation)


def stats(NATION_ARRAY):
    clearScreen()
    print('Printing nation list')
    print('')
    print('|  Score   |TradeScore|TechScore |   Name   ')

    rankCounter = []
    for x in range(0, len(NATION_ARRAY)):
        rankCounter.append((NATION_ARRAY[x][0]['Score'],x))
    rankCounter.sort()

    for x in range(0, len(rankCounter)):
        index = rankCounter[x][1]

        score = str(NATION_ARRAY[index][0]['Score'])
        for y in range(0, (10 - len(score))): score = score + ' '

        tradeScore = str(NATION_ARRAY[index][0]['Finance']['wealth'])
        for z in range(0, (10 - len(tradeScore))): tradeScore = tradeScore + ' '

        techScore = str(NATION_ARRAY[index][0]['Tech']['level'])
        for z in range(0, (10 - len(techScore))): techScore = techScore + ' '

        print('|' + score + '|' + tradeScore + '|' + techScore + '|' + '   ' + str(NATION_ARRAY[rankCounter[x][1]][-1])  )

    print('')
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
	    	myNation =selectNation(NATION_ARRAY)
	    med_print('Starting game... \n')
	    clearScreen()
	    break
	if selection == 2:
	    myNation = selectNation(NATION_ARRAY)
	if selection == 3:
	    stats(NATION_ARRAY)
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

userName = 'TEST'
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
# fast_print('The year is 1949, the devestating and costly war has finally come to an end.\nIt is your responsibility to lead ' + str(myNation[-1]) + ' greatness. \n')
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
def financeBeuro():
    clearScreen()
    financeSelection = ' '
    while financeSelection != '':
        print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
        print('        WELCOME TO THE FINANCE BEURO   😊        ')
        print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
        print('')
        print('My Team: ' + str(myNation[1]))
        print('Year: ' + str(year))
        print('')
        print('[1] Gamble')
        print('[2] Exit')
        print(' ')
        print(' ')
        print('****************************************')
        print(' ')
        print(' ')
        financeSelection = str(input('Please chose an option \n'))
        print(financeSelection)
        if financeSelection == '1':
            gambleSelect()
        if financeSelection == '2':
            print('exiting...')
            break

            

def gambleSelect():
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
    myNation[0]['Nextmove'] = 'gamble',gambleAmount
    print('You will gamble ' + str(myNation[0]['Nextmove'][1]) + ' in the next round')
    buffer = input('press any key to continue')
    




def warMinistry():
	fast_print('This feature is not ready yet...')

def politicalCabinet():
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
	    	NATION_ARRAY[index][0]['Nextmove'] = 'gamble',amount

	else:
	    NATION_ARRAY[index][0]['Nextmove'] = 'pass'
	return(NATION_ARRAY)







def action(index, currentNation,NATION_ARRAY):
    

    # PROCESS PASS
    if currentNation[0]['Nextmove'] == 'pass':
        print(str(currentNation[1]) + ' chose to pass')
        
    
    # PROCESS GAMBLE 
    if currentNation[0]['Nextmove'][0] == 'gamble':
        print(str(currentNation[1]) + ' chose to gamble')
        amount = currentNation[0]['Nextmove'][1] # the amount chosen to gamble
        originalFinanceScore = currentNation[0]['Finance']['wealth']
        winnings = random.randint((round(0.3*amount)), round(2*amount)) 

        NATION_ARRAY[index][0]['Finance']['wealth'] = (NATION_ARRAY[index][0]['Finance']['wealth'] - amount) + winnings

        difference = NATION_ARRAY[index][0]['Finance']['wealth'] - originalFinanceScore  

        if difference > 0:
        	print(str(currentNation[1]) + ' gained  +' + str(difference))
        elif difference < 0:
        	print(str(currentNation[1]) + ' lost  ' + str(difference))
        else:
        	print(str(currentNation[1]) + ' broke even  ' + str(difference))

        print('Gambled         : ' + str(amount))
        print('Winnings        : ' + str(winnings))
        print('Finance credits :' + str(NATION_ARRAY[index][0]['Finance']['wealth'] ))
    return(NATION_ARRAY)
        
        
 


def tallyScores(NATION_ARRAY):
    for x in range(0, len(NATION_ARRAY)):    
	    #SUM UP SUBSCORES
	    financeScore = NATION_ARRAY[x][0]['Finance']['wealth']
	    totalSubScores = financeScore
	    NATION_ARRAY[x][0]['Score'] = NATION_ARRAY[x][0]['Score'] + totalSubScores
    return(NATION_ARRAY)


def defaultNextStep(NATION_ARRAY):
    for x in range(0, len(NATION_ARRAY)):    
	    NATION_ARRAY[x][0]['Nextmove'] = 'pass'
    return(NATION_ARRAY)




def nextYear(year,myNation,NATION_ARRAY):
    clearScreen()
    med_print('Processing next year....')
    print('')
    for x in range(0, len(NATION_ARRAY)):
        currentNation = NATION_ARRAY[x]
        index = x

        # AI DECISIONS 
        if currentNation != myNation: 
            NATION_ARRAY = setAIMoves(index,currentNation,NATION_ARRAY) 


        # ACTION CARRIED OUT FOR ALL USERS
        NATION_ARRAY = action(index,currentNation,NATION_ARRAY)
        print('')
        print('')

    # Only talling scores at the end....may need to change
    print('Tallying scores')
    NATION_ARRAY = tallyScores(NATION_ARRAY)
    NATION_ARRAY = defaultNextStep(NATION_ARRAY)
    year = year + 1
    buffer = input('Press any button to continue')
    return(year, NATION_ARRAY)
    
 





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
    print('****************************************')
    print(' ')
    print(' ')
    menuSelection = str(input('What would you like to do ' + str(userName) + '? \n'))
    
    if menuSelection == '1':
        stats(NATION_ARRAY)
    if menuSelection == '2':
        financeBeuro()
    if menuSelection == '3':
        warMinistry()
    if menuSelection == '4':
        politicalCabinet()
    if menuSelection == '5':
        year, NATION_ARRAY = nextYear(year,myNation,NATION_ARRAY)
        
print('it should process all at same time..')















