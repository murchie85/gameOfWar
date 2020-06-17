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
THINGS TO SAVE

NAME
YEAR
ARRAY
rank 
selected country 
"""



# ---------------------------------------------------------------------
# UTILITIES 
# ---------------------------------------------------------------------
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


# ---------------------------------------------------------------------
# END UTILITIES
# ---------------------------------------------------------------------



maxPP = 23210
maxGDP = 19
USA           = {'score': 10, 'finance': 8, "special":{'chance': 0} , "friendship":{} , "nextmove" : 'pass'}
CHINA         = {'score': 6, 'finance': 10, "special":{'chance': 0} , "friendship":{} , "nextmove" : 'pass'}
INDIA         = {'score': 2, 'finance': 3, "special":{'chance': 0} , "friendship":{} , "nextmove" : 'pass'}
RUSSIA        = {'score': 1, 'finance': 2, "special":{'chance': 0} , "friendship":{} , "nextmove" : 'pass'}
UK            = {'score': 3, 'finance': 2, "special":{'chance': 0} , "friendship":{} , "nextmove" : 'pass'}
GERMANY       = {'score': 4, 'finance': 2, "special":{'chance': 0} , "friendship":{} , "nextmove" : 'pass'}
FRANCE        = {'score': 3, 'finance': 2, "special":{'chance': 0} , "friendship":{} , "nextmove" : 'pass'}
JAPAN         = {'score': 3, 'finance': 2, "special":{'chance': 0} , "friendship":{} , "nextmove" : 'pass'}
BRAZIL        = {'score': 1, 'finance': 1, "special":{'chance': 0} , "friendship":{} , "nextmove" : 'pass'}
SOUTHKOREA    = {'score': 1, 'finance': 1, "special":{'chance': 0} , "friendship":{} , "nextmove" : 'pass'}
SOUTHAFRICA   = {'score': 1, 'finance': 1, "special":{'chance': 0} , "friendship":{} , "nextmove" : 'pass'}

NATION_ARRAY = [[USA,'USA'],[CHINA,'CHINA'],[INDIA,'INDIA'],[RUSSIA,'RUSSIA'],[UK,'UK'],[GERMANY,'GERMANY'],[FRANCE,'FRANCE'],[JAPAN,'JAPAN'],[BRAZIL,'BRAZIL'],[SOUTHKOREA,'SOUTHKOREA'],[SOUTHAFRICA,'SOUTHAFRICA']]
NATION_DICT = {'USA':USA,'CHINA':CHINA, 'INDIA': INDIA,'RUSSIA':RUSSIA,'UK':UK,'GERMANY':GERMANY,'FRANCE':FRANCE,'JAPAN':JAPAN,'BRAZIL':BRAZIL,'SOUTHKORA':SOUTHKOREA, 'SOUTHAFRICA':SOUTHAFRICA}


# TRADE INITIALISED BY PP
# TOTAL INITIALISED BY GDP


myNation = ''
buffer = ''
buffer = ''






# ---------------------------------------------------------------------
#                           START MENU MODE 
#     1. SELECT NATION OPTION
#     2. VIEW COUNTRY
#     3. VIEW RULES
#     4. VIEW CREDITS
#     5. START GAME 
# ---------------------------------------------------------------------
clearScreen()

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
        fast_print('Your chosen country is : ' +    str(NATION_ARRAY[NationChoice][-1]) + '\n')
        print('')
        buffer = input('Press any button to continue \n')
        clearScreen()
        myNation = NATION_ARRAY[NationChoice]
        nationSelected = 'Y'
    return(myNation)

def stats(NATION_ARRAY):
    print('Printing nation list')
    print('')
    print('|  Score   |TradeScore|   Name   ')
    for x in range(0, len(NATION_ARRAY)):

        score = str(NATION_ARRAY[x][0]['score'])
        for y in range(0, (10 - len(score))): score = score + ' '

        tradeScore = str(NATION_ARRAY[x][0]['finance'])
        for z in range(0, (10 - len(tradeScore))): tradeScore = tradeScore + ' '

        print('|' + score + '|' + tradeScore + '|' + '   ' + str(NATION_ARRAY[x][-1])  )

    print('')
    buffer = input('Press any button to continue \n')
    clearScreen()


selection = ''
while selection != 'Done':
    print('*****************MENU*******************')
    print('')
    print('')
    print('[1] Select your Nation')
    print('[2] View Country Stats')
    print('[3] View game rules')
    print('[4] View Credits')
    print('[5] Play some music')
    print('[6] Start Game')
    print('')
    print('')
    
    selection = int(input('Please chose an option \n'))
    if selection == 1:
        myNation = selectNation(NATION_ARRAY)
    if selection == 2:
        stats(NATION_ARRAY)
    if selection == 3:
        fast_print('The aim of the game is to gain the most points before the year 2100. \n')
        fast_print('This can be by winning on trade, military, culture or other. \n')
        fast_print('Remember, every action has its own consequence! \n')
        fast_print('Good Luck commander! \n' )
        buffer = input('Press any button to continue \n ')
        clearScreen()
    if selection == 4:
        fast_print('All credits go to Adam McMurchie... me! . \n')
        buffer = input('Press any button to continue \n ')
        clearScreen()
    if selection == 5:
        import webbrowser
        fast_print('This will open music in your webbrowser. \n' )
        decision = input('Y/N \n').upper()
        if decision == 'Y':
            webbrowser.open('https://youtu.be/H8w_Q57RQJc')
        clearScreen()
    if selection == 6:
        if myNation == '':
            fast_print('Nation not selected \n')
            fast_print('Please pick a nation...\n')
            continue
        # print('Your nation stats are...')
        # print(myNation)
        med_print('Starting game... \n')
        clearScreen()
        break

# ---------------------------------------------------------------------
#                           MAIN MODE 
# ---------------------------------------------------------------------

gameLoaded = False

if gameLoaded:
    print('Welcome back commander')


year = 1949

# MUST UNCOMENT FOR FULL GAME


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
# med_print('..........universe destruction in progress......\n')
# for x in range(0,10):
#     print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
# time.sleep(0.50)
# for x in range(0,10):
#     print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
# time.sleep(0.50)
# for x in range(0,10):
#     print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
# med_print('....booting up universe simulation #16725 omega .......\n')
# for y in range(0,3):
#     for x in range(0,10):
#         print('><><><>><><><>><><><>><><><>><><><>><><><>><><><>><><><')
#     time.sleep(0.50)
# time.sleep(0.580)
# for y in range(0,3):
#     for x in range(0,10):
#         print('asklfdj;l;j;adfj;kj;afdkjaklsdjfaghaldg;asdkjf;lkja;ajd')
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


# ---------------------------------------------------------------------
#                           MAIN FUNCTIONS
# ---------------------------------------------------------------------







def AIaction(index,currentNation,NATION_ARRAY):

    gambleAction = random.randint(0,4)
    if gambleAction > 2:
        amount = 999999999999
        creditsAvailable = int(currentNation[0]['finance'])
        if creditsAvailable < 1:
            flag = 1
        amount = random.randint(1,creditsAvailable)
        NATION_ARRAY[index][0]['nextmove'] = 'gamble',amount
        #print(str(currentNation[1]) + ' will gamble ' +  str(amount))
    else:
        NATION_ARRAY[index][0]['nextmove'] = 'pass'
    return(NATION_ARRAY)


def action(index, currentNation,NATION_ARRAY):
    
    if currentNation[0]['nextmove'] == 'pass':
        print(str(currentNation[1]) + ' chose to pass')
        
        
    if currentNation[0]['nextmove'][0] == 'gamble':
        print(str(currentNation[1]) + ' chose to gamble')
        amount = currentNation[0]['nextmove'][1] # the amount chosen to gamble
        winnings = random.randint((round(0.3*amount)), round(2*amount)) 
        print(str(currentNation[1]) + ' won an ammount of ' + str(winnings))
        print('Original amount gambled was ' + str(amount))
        
        
        NATION_ARRAY[index][0]['finance'] = (NATION_ARRAY[index][0]['finance'] - amount) + winnings
        print(str(currentNation[1]) + ' finance changed to ' + str(NATION_ARRAY[index][0]['finance'] ))
    return(NATION_ARRAY)
        
        

def gamble():
    clearScreen()
    print('My Team: ' + str(myNation[1]))
    print('Year: ' + str(year))
    print('Trade Credits: ' + str(myNation[0]['finance']))
    print(' ')
    print('')
    
    amount = 999999999999
    flag = 0
    creditsAvailable = int(myNation[0]['finance'])
    if creditsAvailable < 1:
        print('you do not have enough credits, sorry')
        flag = 1

    fast_print('How much do you wish to gamble? \n')
    while amount > creditsAvailable and flag ==0:
        try:
            amount = int(input('Input amount between 1 and ' + str(creditsAvailable) + '\n'))
        except:
            print("Entered incorrectly, please try again")
    
    myNation[0]['nextmove'] = 'gamble',amount
    print('You will gamble ' + str(myNation[0]['nextmove'][1]) + ' in the next round')
    buffer = input('press any key to continue')
    

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
            gamble()
        if financeSelection == '2':
            print('exiting...')
            break

            

def nextYear(year,myNation,NATION_ARRAY):
    clearScreen()
    med_print('Processing next year....')
    print('')
    for x in range(0, len(NATION_ARRAY)):
        currentNation = NATION_ARRAY[x]
        index = x

        # AI DECISIONS 
        if currentNation != myNation: 
            NATION_ARRAY = AIaction(index,currentNation,NATION_ARRAY) 
        NATION_ARRAY = action(index,currentNation,NATION_ARRAY)
        print('')
        print('')
    year = year + 1
    buffer = input('Press any button to continue')
    return(year, NATION_ARRAY)
    
 

# ---------------------------------------------------------------------
#                           MAIN MENU
# ---------------------------------------------------------------------


menuSelection = ' '
while menuSelection != '':
    clearScreen()
    print('*****************MENU*******************')
    print('')
    print('My Team: ' + str(myNation[1]))
    print('Year: ' + str(year))
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
    menuSelection = str(input('Please chose an option \n'))
    
    if menuSelection == '1':
        stats(NATION_ARRAY)
    if menuSelection == '2':
        financeBeuro()
    if menuSelection == '5':
        year, NATION_ARRAY = nextYear(year,myNation,NATION_ARRAY)
        
print('it should process all at same time..')




