# All WAR Menu Function

from gameConquest_utilities import slow_print as slow_print
from gameConquest_utilities import med_print as med_print
from gameConquest_utilities import fast_print as fast_print
from gameConquest_utilities import superfast_print as superfast_print
from gameConquest_utilities import clearScreen as clearScreen
from gameConquest_utilities  import preferencePrint as preferencePrint
from gameConquest_utilities  import checkMoves as checkMoves
from gameConquest_utilities  import selectCountry as selectCountry


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
        clearScreen()
        flag = 'no'
    return(flag)

def showFriendship(myNation,friendshipFlag):
    if friendshipFlag == 'Y':
        print(str(myNation[1]) + ' INTERNATIONAL RELATIONS')
        print('---------------------------------------------')
        for nation in myNation[0]['Friendship'].keys():
            paddingLen = 15 - len(nation)
            padding = ''
            for x in range(0,paddingLen): padding = padding + ' '

            print(str(nation) + str(padding) + ': Friendship Level = ' + str(myNation[0]['Friendship'][nation]['level']))
        input('Enter to continue \n')
        clearScreen()
        friendshipFlag = 'N'
    return(friendshipFlag)
        





def warMinistry(myNation,NATION_ARRAY,year,WAR_BRIEFING):
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
        flag = showAssets(myNation,year,flag)
        print('')
        print('[C] Combat Manevres')
        print('[W] Weapons')
        print('[O] Offensive Missions')
        print(' ')
        print(' ')
        print(' ')
        print(' ')
        print('[A] Show Military Assets')
        print('[R] Return')
        print(' ')
        print(' ')
        print(' ')
        print('Moves: ' + str(checkMoves(myNation,"%^")[0]) )
        print('****************************************')
        print(' ')
        print(' ')
        warSelection = str(input('Please chose an option \n')).upper()
        if warSelection == 'C':
            myNation = manoeuvresMenu(myNation,year,WAR_BRIEFING)
        if warSelection == 'W':
            myNation = weaponsMenu(myNation,year,WAR_BRIEFING)
        if warSelection == 'O':
            myNation = missionsMenu(myNation,NATION_ARRAY,year,WAR_BRIEFING)
        if warSelection == 'T':
            fast_print('not ready')
        if warSelection == 'T':
            fast_print('not ready')
        if warSelection == 'A':
            flag = 'yes'
        if warSelection == 'R' or warSelection == '':
            return(myNation)
    return(myNation)






"""
# =====================================================================
# =====================================================================
# =====================================================================
#      WEAPON WEAPONS WEAPON WEAPONS WEAPON WEAPONS WEAPON WEAPONS 
#    WEAPON WEAPONS WEAPON WEAPONS WEAPON WEAPONS WEAPON WEAPONS WEAPON WEAPONS 
#    WEAPON WEAPONS WEAPON WEAPONS WEAPON WEAPONS WEAPON WEAPONS WEAPON WEAPONS 
#     WEAPON WEAPONS WEAPON WEAPONS WEAPON WEAPONS WEAPON WEAPONS WEAPON WEAPONS 
#     WEAPON WEAPONS WEAPON WEAPONS WEAPON WEAPONS WEAPON WEAPONS WEAPON WEAPONS 
#    WEAPON WEAPONS WEAPON WEAPONS WEAPON WEAPONS WEAPON WEAPONS WEAPON WEAPONS 
# =====================================================================
# =====================================================================
# =====================================================================
"""





def weaponsMenu(myNation,year,WAR_BRIEFING):
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
        print('')
        print("""
(╯°□°)--︻╦╤─ - - - 
                """)
        flag = showAssets(myNation,year,flag)
        print('')
        print('[B] Build')
        print('[S] Scrap')
        print(' ')
        print(' ')
        print('[V] View my units')
        print('[R] Return')
        print(' ')
        print(' ')
        print(' ')
        print('Moves: ' + str(checkMoves(myNation,"%^")[0]) )
        print('****************************************')
        print(' ')
        print(' ')
        # CHECK MAX MOVES SINCE INSIDE WHILE LOOP
        returnCode = checkMoves(myNation,'%^')[1]
        if returnCode > 0: 
            fast_print('All moves used up')
            return(myNation)
        warSelection = str(input('Please chose an option \n')).upper()
        if warSelection == 'B':
            myNation = buildMenu(myNation,year,WAR_BRIEFING)
        if warSelection == 'S':
            myNation = scrapMenu(myNation,year,WAR_BRIEFING)
        if warSelection == 'T':
            fast_print('not ready')
        if warSelection == 'T':
            fast_print('not ready')
        if warSelection == 'V':
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
        print('Moves: ' + str(checkMoves(myNation,"%^")[0]) )
        print('****************************************')
        print(' ')
        print(' ')
        # CHECK MAX MOVES SINCE INSIDE WHILE LOOP
        returnCode = checkMoves(myNation,'%^')[1]
        if returnCode > 0: 
            fast_print('All moves used up')
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
        print('Moves: ' + str(checkMoves(myNation,"%^")[0]) )
        print('****************************************')
        print(' ')
        print(' ')
        # CHECK MAX MOVES SINCE INSIDE WHILE LOOP
        returnCode = checkMoves(myNation,'%^')[1]
        if returnCode > 0: return(myNation)


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




def manoeuvresMenu(myNation,year,WAR_BRIEFING):
    manoeuvresSelection = ' '
    flag = ''
    while manoeuvresSelection != 'XYZFFJJJJJJ':
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
        print('       !!MILITARY MANOEUVRES HQ!!        :X        ')
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
        flag = showAssets(myNation,year,flag)
        print('')
        print('[D] Drill and train your forces')
        print('[J] Joint manoeuvres')
        print('[I] Intimidation manoeuvres')
        print(' ')
        print(' ')
        print('[D] Detailed forces review')
        print('[R] Return')
        print(' ')
        print(' ')
        print(' ')
        print('Moves: ' + str(checkMoves(myNation,"%^")[0]) )
        print('****************************************')
        print(' ')
        print(' ')
        # CHECK MAX MOVES SINCE INSIDE WHILE LOOP
        returnCode = checkMoves(myNation,'%^')[1]
        if returnCode > 0: 
            fast_print('All moves used up')
            return(myNation)

        manoeuvresSelection = input('Select an option \n').upper()
        clearScreen()
        if manoeuvresSelection == 'D':
            myNation = drillMenu(myNation,year,WAR_BRIEFING)
        if manoeuvresSelection == 'J':
            print('Not ready')
        if manoeuvresSelection == 'I':
            print('Not ready')
        if manoeuvresSelection == 'D':
            flag = 'yes'
        if manoeuvresSelection == 'R' or manoeuvresSelection == '':
            return(myNation)
    return(myNation)    


"""
# =====================================================================
# =====================================================================
# =====================================================================
#     DRILL DRILL DRILL DRILL DRILL DRILL DRILL DRILL DRILL DRILL DRILL DRILL 
#     DRILL DRILL DRILL DRILL DRILL DRILL DRILL DRILL DRILL DRILL DRILL DRILL 
#    DRILL DRILL DRILL DRILL DRILL DRILL DRILL DRILL DRILL DRILL DRILL DRILL 
#     DRILL DRILL DRILL DRILL DRILL DRILL DRILL DRILL DRILL DRILL DRILL DRILL 
#     DRILL DRILL DRILL DRILL DRILL DRILL DRILL DRILL DRILL DRILL DRILL DRILL 
#    DRILL DRILL DRILL DRILL DRILL DRILL DRILL DRILL DRILL DRILL DRILL DRILL 
# =====================================================================
# =====================================================================
# =====================================================================
"""





def drill(myNation, branch,units,WAR_BRIEFING):
    print('')
    # CHECK MAX MOVES 
    returnCode = checkMoves(myNation,'drill')[1]
    if returnCode > 0: 
        fast_print('All moves used up, or already drilling this round.')
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
        flag = showAssets(myNation,year,flag)
        print('')
        print('[G] Ground Forces')
        print('[N] Navy')
        print('[A] Airforce')
        print(' ')
        print(' ')
        print('[D] Detailed forces review')
        print('[R] Return')
        print(' ')
        print(' ')
        print(' ')
        print('Moves: ' + str(checkMoves(myNation,"%^")[0]) )
        print('****************************************')
        print(' ')
        print(' ')
        # CHECK MAX MOVES SINCE INSIDE WHILE LOOP
        returnCode = checkMoves(myNation,'%^')[1]
        if returnCode > 0: 
            fast_print('All moves used up')
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





"""
# =====================================================================
# =====================================================================
# =====================================================================
#     MISSION MISSION MISSION MISSION MISSION MISSION MISSION MISSION MISSION MISSION 
#     MISSION MISSION MISSION MISSION MISSION MISSION MISSION MISSION MISSION MISSION 
#      MISSION MISSION MISSION MISSION MISSION MISSION MISSION MISSION MISSION MISSION 
#     MISSION MISSION MISSION MISSION MISSION MISSION MISSION MISSION MISSION MISSION 
#      MISSION MISSION MISSION MISSION MISSION MISSION MISSION MISSION MISSION MISSION 
#     MISSION MISSION MISSION MISSION MISSION MISSION MISSION MISSION MISSION MISSION 
# =====================================================================
# =====================================================================
# =====================================================================
"""

def missionsMenu(myNation,NATION_ARRAY,year,WAR_BRIEFING):
    flag = ''
    friendshipFlag = ''
    missionSelection = ' '
    while missionSelection != 'XYZFFJJJJJJ':
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
        print('                 MISSION PLANNING        :X        ')
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
        flag = showAssets(myNation,year,flag)
        friendshipFlag = showFriendship(myNation,friendshipFlag)
        print('')
        print('[E] Espionage')
        print('[C] Covert Operations')
        print('[T] Tactical Strike')
        print('[D] Declare War')
        print(' ')
        print(' ')
        print(' ')
        print('[F] Show Friendships (Internaitonal Relations)')
        print('[S] Show Military Assets')
        print('[H] Help & Explanation')
        print('[R] Return')
        print(' ')
        print(' ')
        print(' ')
        print('Moves: ' + str(checkMoves(myNation,"%^")[0]) )
        print('****************************************')
        print(' ')
        print(' ')
        returnCode = checkMoves(myNation,'%^')[1]
        if returnCode > 0: 
            fast_print('All moves used up')
            return(myNation)
        missionSelection = str(input('Please chose an option \n')).upper()
        if missionSelection == 'E':
            myNation = espionage(myNation,NATION_ARRAY,WAR_BRIEFING)
        if missionSelection == 'C':
            myNation = covert(myNation,NATION_ARRAY,WAR_BRIEFING)
        if missionSelection == 'T':
            fast_print('not ready')
        if missionSelection == 'D':
            fast_print('not ready')
        if missionSelection == 'F':
            friendshipFlag = 'Y'
        if missionSelection == 'S':
            flag = 'yes'
        if missionSelection == 'H':
            print('*****Explanation of Options *****')
            print('')
            print('ESPIONAGE: Obtains intel about enemy, a small amount of points and forces them to skip a round. May incur loss in friendship if found out.')
            print('COVERT OPERATIONS: Damage an enemy moderately, possibility of stealing resources, May incur signiciant loss in friendship if found out.')
            print('TACTICAL STRIKE: Damage an enemy severely, signiciant drop in friendship and possible repercussions.')
            print('DECLARE WAR: Forces the enemy into a round by round battle of attrition, only military moves can be carried out. You can win, lose, surrender or offer a truce. Will lose some global backing.')
            print('***All Options depend on your frienship levels with the nation state.')
            print('')
            input('Enter to continue')
        if missionSelection == 'R' or missionSelection == '':
            return(myNation)
    return(myNation)



def covert(myNation,NATION_ARRAY,WAR_BRIEFING):
    covertThreshold = -20
    # CHECK MAX MOVES
    returnCode = checkMoves(myNation,'covert')[1]
    if returnCode > 0: return(myNation)
    
    returnCode,NationChoice = selectCountry(NATION_ARRAY,myNation,'****CHOOSE A TARGET****')
    if returnCode > 0: return(myNation)
    
    # CHECK FRIENDSHIP 
    if myNation[0]['Friendship'][NATION_ARRAY[NationChoice][-1]]['level'] > covertThreshold:
        print('Sorry, your friendship with ' + str(NATION_ARRAY[NationChoice][-1]) + ' is ' + str(myNation[0]['Friendship'][NATION_ARRAY[NationChoice][-1]]['level']) + '.  \n Covert operations are only available when friendship deteriorates below < ' + str(covertThreshold) + '. \n Please check international relations option to view friendship levels.')
        input('')
        return(myNation)

    covertOrder = ''
    covertChoice = ""
    while covertChoice != 'XYZFFJJJJJJ':
        print('[E] Economy')
        print('[M] Military')
        print('[S] Science')
        print('[P] Politics')
        print(' ')
        print(' ')
        print('[I] More Info')
        print('[R] Return')
        covertChoice = input('What branch of the ' + str(NationChoice) + ' government do you wish to attack? \n').upper()
        clearScreen()
        if covertChoice == 'E':
            covertOrder = ['covert',NationChoice,'economy']
            break
        if covertChoice == 'M':
            covertOrder = ['covert',NationChoice,'military']
            break
        if covertChoice == 'S':
            covertOrder = ['covert',NationChoice,'science']
            break
        if covertChoice == 'P':
            covertOrder = ['covert',NationChoice,'politics']
            break
        if covertChoice == 'I':
            fast_print('Covert lets you steal and damage enemy assets significantly, this gains benefits but can be risky and lead to war \n')
            print('Depending on what branch you target, will result in corresponding gains i.e. . \n')
            print('As your rank increases you can chose to target a specific branch of the government. \n')
            print('Military  : Might ++')
            print('******IF YOUR GAMBIT FAILS, THE CONSEQUENCES COULD BE SEVERE****')
            input('Enter to continue \n')
        if covertChoice == 'R' or covertChoice == '':
            return(myNation)

    myNation[0]['Nextmoves'] = myNation[0]['Nextmoves'] + [covertOrder]

    return(myNation)


def espionage(myNation,NATION_ARRAY,WAR_BRIEFING):
    # CHECK MAX MOVES
    returnCode = checkMoves(myNation,'covert')[1]
    if returnCode > 0: return(myNation)
    # SELECT COUNTRY
    returnCode,NationChoice = selectCountry(NATION_ARRAY,myNation,'****CHOOSE A TARGET****')
    if returnCode > 0: return(myNation)
    
    # CHECK FRIENDSHIP EXCEEDS THRESHOLD
    espionageThreshold = 0
    if myNation[0]['Friendship'][NATION_ARRAY[NationChoice][-1]]['level'] > espionageThreshold:
        print('Sorry, your friendship with ' + str(NATION_ARRAY[NationChoice][-1]) + ' is ' + str(myNation[0]['Friendship'][NATION_ARRAY[NationChoice][-1]]['level']) + '. Espionage is only available when friendship deteriorates below < ' + str(espionageThreshold) + '. \n Please check international relations option to view friendship levels.')
        input('')
        return(myNation)

    # espionageOrder = ''
    # espionageChoice = ""
    # while covertChoice != 'XYZFFJJJJJJ':
    #     print('[E] Economy')
    #     print('[M] Military')
    #     print('[S] Science')
    #     print('[P] Politics')
    #     print('[I] More Info')
    #     print('[R] Return')
    #     espionageChoice = input('What branch of the ' + str(NationChoice) + ' government do you wish to infiltrate? \n').upper()
    #     clearScreen()
    #     if espionageChoice == 'E':
    #         espionageOrder = ['espionage',NationChoice,'economy']
    #         break
    #     if espionageChoice == 'M':
    #         espionageOrder = ['espionage',NationChoice,'military']
    #         break
    #     if espionageChoice == 'S':
    #         espionageOrder = ['espionage',NationChoice,'science']
    #         break
    #     if espionageChoice == 'P':
    #         espionageOrder = ['espionage',NationChoice,'politics']
    #         break
    #     if espionageChoice == 'I':
    #         fast_print('Espionage lets you steal enemy assets, this gains benefits but can be risky and lead to war \n')
    #         print('Depending on what branch you target, will result in corresponding gains i.e. . \n')
    #         print('As your rank increases you can chose to target a specific branch of the government. \n')
    #         print('Military  : Might ++')
    #         print('******IF YOUR GAMBIT FAILS, THE CONSEQUENCES COULD BE SEVERE****')
    #         input('Enter to continue \n')
    #     if espionageChoice == 'R' or espionageChoice == '':
    #         return(myNation)

    espionageOrder = ['espionage',NationChoice]
    myNation[0]['Nextmoves'] = myNation[0]['Nextmoves'] + [espionageOrder]
    input('Espionage orders given..')

    return(myNation)








 

