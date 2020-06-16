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

# ---------------------------------------------------------------------
# UTILITIES 
# ---------------------------------------------------------------------
import sys
import time

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

# ---------------------------------------------------------------------
# END UTILITIES
# ---------------------------------------------------------------------



maxPP = 23210
maxGDP = 19

USA           = [round(19 / maxGDP * 10), round(19490 / maxPP * 10)]
CHINA         = [round(12 / maxGDP * 10), round(23210 / maxPP * 10)]
INDIA         = [round(3 / maxGDP * 10), round(9474 / maxPP * 10)]
RUSSIA        = [round(2 / maxGDP * 10), round(19490 / maxPP * 10)]
GERMANY       = [round(4 / maxGDP * 10), round(19490 / maxPP * 10)]
FRANCE        = [round(3 / maxGDP * 10), round(19490 / maxPP * 10)]
JAPAN         = [round(5 / maxGDP * 10), round(5443 / maxPP * 10)]
BRAZIL        = [round(2 / maxGDP * 10), round(19490 / maxPP * 10)]
SOUTHKOREA    = [round(2 / maxGDP * 10), round(19490 / maxPP * 10)]
SOUTHAFRICA   =  [round(1 / maxGDP * 10), round(19490 / maxPP * 10)]

NATION_ARRAY = [[USA,'USA'],[CHINA,'CHINA'],[INDIA,'INDIA'],[RUSSIA,'RUSSIA'],[GERMANY,'GERMANY'],[FRANCE,'FRANCE'],[JAPAN,'JAPAN'],[BRAZIL,'BRAZIL'],[SOUTHKOREA,'SOUTHKOREA'],[SOUTHAFRICA,'SOUTHAFRICA']]
# TRADE INITIALISED BY PP
# TOTAL INITIALISED BY GDP


nation = ''







# ---------------------------------------------------------------------
#                           MENU MODE 
#     1. SELECT NATION OPTION
#     2. VIEW COUNTRY
#     3. VIEW RULES
#     4. VIEW CREDITS
#     5. START GAME 
# ---------------------------------------------------------------------
print(chr(27) + "[2J")

def selectNation(NATION_ARRAY):
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
			NationChoice = int(input('Please chose a country \n'))
		fast_print('Your chosen country is : ' + 	str(NATION_ARRAY[NationChoice][-1]) + '\n')
		print('')
		input('Press any button to continue \n')
		print(chr(27) + "[2J")
		nation = NATION_ARRAY[NationChoice]
		nationSelected = 'Y'
	return(nation)

def stats(NATION_ARRAY):
	print('Printing nation list')
	print('')
	print('|  Score   |TradeScore|   Name   ')
	for x in range(0, len(NATION_ARRAY)):

		score = str(NATION_ARRAY[x][0][0])
		for y in range(0, (10 - len(score))): score = score + ' '

		tradeScore = str(NATION_ARRAY[x][0][1])
		for z in range(0, (10 - len(tradeScore))): tradeScore = tradeScore + ' '

		print('|' + score + '|' + tradeScore + '|' + '   ' + str(NATION_ARRAY[x][-1])  )

	print('')
	input('Press any button to continue \n')
	print(chr(27) + "[2J")


selection = ''
while selection != 'Done':
    print('*****************MENU*******************')
    print('')
    print('')
    print('[1] Select your Nation')
    print('[2] View Country Stats')
    print('[3] View game rules')
    print('[4] View Credits')
    print('[5] Start Game')
    print('')
    print('')
    
    selection = int(input('Please chose an option \n'))
    if selection == 1:
    	nation = selectNation(NATION_ARRAY)
    if selection == 2:
    	stats(NATION_ARRAY)
    if selection == 3:
    	fast_print('The aim of the game is to gain the most points before the year 2100. \n')
    	fast_print('This can be by winning on trade, military, culture or other. \n')
    	fast_print('Remember, every action has its own consequence! \n')
    	fast_print('Good Luck commander! \n' )
    	input('Press any button to continue \n ')
    	print(chr(27) + "[2J")
    if selection == 4:
    	fast_print('All credits go to Adam McMurchie... me! . \n')
    	input('Press any button to continue \n ')
    	print(chr(27) + "[2J")
    if selection == 5:
    	if nation == '':
    		fast_print('Nation not selected \n')
    		fast_print('Please pick a nation...\n')
    		continue
    	# print('Your nation stats are...')
    	# print(nation)
    	med_print('Starting game... \n')
    	print(chr(27) + "[2J")
    	break

# ---------------------------------------------------------------------
#                           MAIN MODE 
# ---------------------------------------------------------------------

gameLoaded = False

if gameLoaded:
	print('Welcome back commander')


year = 1949


assistant = 'Arbiter: '
fast_print('**rustle**....**clunk** ..."oh not again!" \n')
fast_print(str(assistant) + '....wait... \n')
time.sleep(0.7)
fast_print(str(assistant) +'..who the hell are you? How did you get in here? ... \n')

userName = input('Enter your name \n')
print(' ')
med_print(str(userName) + ': ... im ' + str(userName) + '\n')

fast_print(str(assistant) + 'ah, so YOU are the one. \n')
time.sleep(0.4)
fast_print(str(assistant) + 'INDIAts truly an honour to meet you ' + str(userName) +  ' please know that we all appreciate your sacrifice  \n')
fast_print(str(assistant) + 'are you ready?  \n ')
print('')
input(' Press any key to start..')
fast_print(str(assistant) + 'executing dynamic cascade sequence now, this should feel... uh..errr..  \n ')
time.sleep(0.6)
fast_print('....a little weird \n ')
time.sleep(1.50)
print(chr(27) + "[2J")
time.sleep(1.50)

for y in range(0,3):
	for x in range(0,10):
		print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
	time.sleep(0.50)
med_print('..........universe destruction in progress......\n')
for x in range(0,10):
	print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
time.sleep(0.50)
for x in range(0,10):
	print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
time.sleep(0.50)
for x in range(0,10):
	print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
med_print('....booting up universe simulation 16725 omega ........\n')
for y in range(0,3):
	for x in range(0,10):
		print('><><><>><><><>><><><>><><><>><><><>><><><>><><><>><><><')
	time.sleep(0.50)
print(chr(27) + "[2J")
fast_print('....Lead me, follow me, or get out of my way ........ \n')
print('(George S Patton)')
time.sleep(1.90)
print(chr(27) + "[2J")
for x in range(0,20):
	print(' ')
time.sleep(0.50)
print('')
y = 5
for x in range(0, 5):
	print(str(y))
	y= y-1
	time.sleep(1.20)
	print(chr(27) + "[2J")







fast_print('Good morning commander..... \n')
fast_print('')
fast_print('The year is 1949, the devestating and costly war has finally come to an end.\nIt is your responsibility to lead ' + str(nation[-1]) + ' greatness. \n')
fast_print('There are many ways to win, trade, politics, war....the path is up to you? \n')


# rank = 'Junior'




"""
THINGS TO SAVE

NAME
YEAR
ARRAY
rank 
"""

