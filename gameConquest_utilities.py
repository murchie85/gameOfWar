
# UTILITIES 
import sys
import time

#p = 'All'

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
		time.sleep(0.01)

def clearScreen():
	for x in range(0,70):
		print('')

def preferencePrint(s,p,i,myNationIndex):
	if p == 'All':
		print(s)
	elif p == 'Me':
		if str(i) == str(myNationIndex):
			print(s)
	elif p == 'None':
		pass
	else:
		print(s)



def printupdates(p):
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

def options(p,NATION_ARRAY):
	clearScreen()
	print('***************************************************')
	print('*                  OPTIONS                        *')
	print('***************************************************')
	print('')
	print('1. Select Music')
	print('2. Change End of Round Updates')
	print('3. Developer Insights')

	selection = str(input('Please select an option \n'))
	if selection == '1':
		music()
	if selection == '2':
		p = printupdates(p)
		return(p)
	if selection == '3':
		developer(NATION_ARRAY)







def music():
	import webbrowser
	clearScreen()
	
	print('***************************************************')
	print('                🎸🎸 MUSIC  🎺🎺                  ')
	print('***************************************************')
	# print('***************************************************')
	# print('             [+][+]   MUSIC  [+][+]                ')
	# print('***************************************************')
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
	fast_print('This will open music in your webbrowser. \n' )
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


def developer(NATION_ARRAY):
	clearScreen()
	print('***************************************************')
	print('*              DEV CONSOLE                        *')
	print('***************************************************')
	print('')
	print('1. Select Country')
	print('2. Exit')

	selection = str(input('Please select an option \n'))
	countrySelected = '	'
	NationChoice = 9999
	if selection == '1':
		while countrySelected != 'Y':
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
		    countrySelected = 'Y'
		    
		for key in NATION_ARRAY[NationChoice][0].keys():
		    print(key)
		    print(NATION_ARRAY[NationChoice][0][key])
		    print('')
		    buffer = input('Press Enter to continue \n')
		    clearScreen()
		print('all')
		print(NATION_ARRAY[NationChoice])
		input()

	if selection == '2':
		fast_print('Exiting')
		clearScreen()


def checkMoves(myNation,duplicateToCheck):
    movesLeft = int(myNation[0]['Special']['moveLimit'] - len(myNation[0]['Nextmoves'] ) + str(sum(myNation[0]['Nextmoves'], [])).count('pending') )
    print('')
    if movesLeft < 1: 
        return(movesLeft,1)
    for item in myNation[0]['Nextmoves']:
        if duplicateToCheck in item:
            print('you have already carried out '  + str(duplicateToCheck) + ' in this round')
            return(movesLeft,1)
    return(movesLeft,0)

def selectCountry(NATION_ARRAY,myNation,printMessage):
    NationChoice = 9999
    countrySelected = ''
    clearScreen()
    while countrySelected != 'Y':
        print('')
        print(printMessage)
        print('')
        for x in range(0, len(NATION_ARRAY)):
            if NATION_ARRAY[x][-1] != myNation[-1]:
                print(str(x) + '. ' + str(NATION_ARRAY[x][-1]))
        print('')
        while NationChoice not in range(0, len(NATION_ARRAY)):
            try:
                 NationChoice = int(input('Please select a country. \n'))
            except:
                print("Entered incorrectly, please try again")
        if NATION_ARRAY[NationChoice][-1] == myNation[-1]:
            print('You cant select your own country ' + str(NATION_ARRAY[NationChoice][-1]) + ' nice try...')
            return(1,NationChoice)
        print('Your chosen country is : ' + str(NATION_ARRAY[NationChoice][-1]) + '\n')
        input('')
        countrySelected = 'Y'
        clearScreen()
    return(0,NationChoice)
