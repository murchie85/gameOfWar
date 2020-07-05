    # All Finance Menu Function

# IMPORT UNIVERSAL UTILITIES
from gameConquest_utilities import preferencePrint as preferencePrint

import sys
import time
import copy
import random

"""

TO DO 

MVP
1. Drill troops Increases might by random small amount
DRILL INCREASE MIGHTINCREASE = RANDOM * LEVEL

ONCE POLITICS IS DONE 

2. Combat Manevres increases might and political will
3. Buy assets (need money and political will)


ONCE TECH IS DONE 

1. Tech level unlocks more items 


"""


P = 'All'

# Takes the build order placed by currentNation
# Awards the unit
# Awards might proportional to mightvalue x totalMight X 1/2 the number of units ordered
# This scales the more you buy and type you buy

def build(nextMove,NATION_ARRAY,currentNation,p,index,playerNationIndex,nextMoveIndex):
    pending    = nextMove[0]
    job        = nextMove[1]
    unit       = nextMove[2]
    amount     = nextMove[3]
    wait       = nextMove[4]
    bonusMight = nextMove[5] 
    moveIndex = nextMoveIndex # Get position in country array


    # IF NOT YET READY
    # DECREMENT BUILD TIME 
    if wait > 1:
        wait = wait -1
        preferencePrint(str(str(currentNation[1]) + ' chose to build '),p,index,playerNationIndex)
        preferencePrint('------------------',p,index,playerNationIndex)
        preferencePrint(str(str(unit) + ' to build : ' + str(amount)),p,index,playerNationIndex)
        preferencePrint(str('Build Time Remaining : ' + str(wait)),p,index,playerNationIndex)
        nextMove = ['pending',job,unit,amount,wait,bonusMight]
        NATION_ARRAY[index][0]['Nextmoves'][moveIndex] = nextMove
        return(NATION_ARRAY)

    # IF READY (currently at 2 cus lazy)
    if wait < 2:
        # Reward Unit
        NATION_ARRAY[index][0]['War']['weapons'][unit] +=  amount
        
        # Reward Mightg
        bonusAdjustment = round((NATION_ARRAY[index][0]['War']['might'] * bonusMight) * (amount/2))
        if bonusAdjustment < 1:
            bonusAdjustment = 1
        NATION_ARRAY[index][0]['War']['might'] = NATION_ARRAY[index][0]['War']['might'] + bonusAdjustment
        preferencePrint(str(str(currentNation[1]) + ' Build complete '),p,index,playerNationIndex)
        preferencePrint('------------------',p,index,playerNationIndex)
        preferencePrint(str(str(unit) + ' units built: ' + str(amount)),p,index,playerNationIndex)
        preferencePrint(str(str(unit) + ' total : ' + str(NATION_ARRAY[index][0]['War']['weapons'][unit])),p,index,playerNationIndex)
        preferencePrint(str('Might gained : ' + str(bonusAdjustment)),p,index,playerNationIndex)
        preferencePrint(str('Might total  : ' + str(currentNation[0]['War']['might'])),p,index,playerNationIndex)

        # Clear out existing array element
        NATION_ARRAY[index][0]['Nextmoves'][moveIndex] = []

        return(NATION_ARRAY)

    return(NATION_ARRAY)


# Takes the scrap order placed by currentNation
# Awards money
# Deducts might proportional to mightvalue x totalMight x 1/5 the number of units scrapped

def scrap(nextMove,NATION_ARRAY,currentNation,p,index,playerNationIndex):
    job           = nextMove[0]
    unit          = nextMove[1]
    amount        = nextMove[2]
    valuation     = nextMove[3]
    reducedMight  = nextMove[4]

    preferencePrint(str(str(currentNation[1]) + ' chose to scrap'),p,index,playerNationIndex)
    preferencePrint('------------------',p,index,playerNationIndex)
    preferencePrint(str(str(unit) + ' to scrap : ' + str(amount)),p,index,playerNationIndex)

    # Award Credits and reduce might
    NATION_ARRAY[index][0]['Finance']['wealth'] +=  valuation
    Adjustment = round((NATION_ARRAY[index][0]['War']['might'] * reducedMight) * (amount/5))
    NATION_ARRAY[index][0]['War']['might'] -=  Adjustment
    
    preferencePrint(str('Might lost    : -' + str(Adjustment)),p,index,playerNationIndex)
    preferencePrint(str('Might total   : ' + str(currentNation[0]['War']['might'])),p,index,playerNationIndex)
    preferencePrint(str(str(currentNation[1]) + ' was paid ' + str(valuation)),p,index,playerNationIndex)
    preferencePrint(str('Credits total : ' + str(currentNation[0]['Finance']['wealth'])),p,index,playerNationIndex)
    return(NATION_ARRAY)





def drill(nextMove,NATION_ARRAY,currentNation,p,index,playerNationIndex):
    move      = nextMove[0]
    branch    = nextMove[1]
    intensity = nextMove[2]
    units     = nextMove[3]
    might     = NATION_ARRAY[index][0]['War']['might']
    credits   = NATION_ARRAY[index][0]['Finance']['wealth']
    techLevel = NATION_ARRAY[index][0]['Tech']['level']
    #['drill',branch,'soft',units]
    #units = [('troops',troops),('tanks',tanks)]


    # RETURN UNITS
    for unit, quantity in units:
        NATION_ARRAY[index][0]['War']['weapons'][unit] = quantity

    preferencePrint('',p,index,playerNationIndex)
    preferencePrint(str(str(currentNation[1]) + ' chose to train their ' + str(branch)),p,index,playerNationIndex)
    preferencePrint('================================',p,index,playerNationIndex)
    preferencePrint(str('Intensity: ' + str(intensity)),p,index,playerNationIndex)

    if intensity == 'soft':
        bonusMight = round((random.randint(1,15) / 100) * might)
        NATION_ARRAY[index][0]['War']['might'] += bonusMight

        preferencePrint(str('Might gained    : ' + str(bonusMight)),p,index,playerNationIndex)
        preferencePrint(str('New Might Total : ' + str(NATION_ARRAY[index][0]['War']['might'])),p,index,playerNationIndex)
        return(NATION_ARRAY)

    if intensity == 'medium':

        # WIN MIGTH
        bonusMight = round((random.randint(10,25) / 100) * might)
        NATION_ARRAY[index][0]['War']['might'] +=  bonusMight
        # WIN CREDITS
        bonusCredits = round((random.randint(1,10) / 100) * credits)
        NATION_ARRAY[index][0]['Finance']['wealth'] +=   bonusCredits

        preferencePrint(str(str(NATION_ARRAY[index][-1]) + ' impressed the top leadership and won financial support.'),p,index,playerNationIndex)
        preferencePrint(str('Credits gained    : ' + str(NATION_ARRAY[index][0]['Finance']['wealth'])),p,index,playerNationIndex)

        # LOSE A PORTION OF UNITS 
        lossProbability = random.randint(0,8)
        lossAmount = 0.25
        if lossProbability == 3:
            for unit, quantity in units:
                original = quantity
                if quantity < 1:
                    continue
                if random.randint(0,1) == 1:
                    loss = round(quantity * lossAmount)
                    if loss == quantity:
                        quantity = quantity - 1
                    else:
                        quantity = round(quantity * (1-lossAmount))
                    preferencePrint(str(str(unit) + ' lost in combat excercise '),p,index,playerNationIndex)
                    preferencePrint(str(str(original - quantity) + ' ' + str(unit) +  ' lost'),p,index,playerNationIndex)
                    preferencePrint(str(str(quantity) + ' remaining'),p,index,playerNationIndex)
                NATION_ARRAY[index][0]['War']['weapons'][unit] = quantity
        preferencePrint(str('Might gained    : ' + str(bonusMight)),p,index,playerNationIndex)
        preferencePrint(str('New Might Total : ' + str(NATION_ARRAY[index][0]['War']['might'])),p,index,playerNationIndex)
        return(NATION_ARRAY)


    if intensity == 'hard':
        # GAIN MIGHT
        bonusMight = round((random.randint(20,40) / 100) * might)
        NATION_ARRAY[index][0]['War']['might'] +=   bonusMight
        # GAIN CREDITS
        bonusCredits = round((random.randint(5,15) / 100) * credits)
        NATION_ARRAY[index][0]['Finance']['wealth'] += bonusCredits

        preferencePrint(str('Credits gained    : ' + str(NATION_ARRAY[index][0]['Finance']['wealth'])),p,index,playerNationIndex)

        # LOSE A PORTION OF UNITS 
        lossProbability = random.randint(0,4)
        lossAmount = 0.25
        if lossProbability == 3:
            preferencePrint(str('XXXX UNITS LOST IN TRAINING XXXX'),p,index,playerNationIndex)
            for unit, quantity in units:
                original = quantity
                if quantity < 1:
                    continue
                if random.randint(0,1) == 1:
                    loss = round(quantity * lossAmount)
                    if loss == quantity:
                        quantity = quantity - 1
                    else:
                        quantity = round(quantity * (1-lossAmount))
                    preferencePrint(str(str(unit) + ' lost in combat excercise '),p,index,playerNationIndex)
                    preferencePrint(str(str(original - quantity) + ' ' + str(unit) +  ' lost'),p,index,playerNationIndex)
                    preferencePrint(str(str(quantity) + ' remaining'),p,index,playerNationIndex)
                NATION_ARRAY[index][0]['War']['weapons'][unit] = quantity

        preferencePrint(str('Might gained    : ' + str(bonusMight)),p,index,playerNationIndex)
        preferencePrint(str('New Might Total : ' + str(NATION_ARRAY[index][0]['War']['might'])),p,index,playerNationIndex)
        preferencePrint(str(''),p,index,playerNationIndex)

        # WIN BONUS UNITS
        winProbability = random.randint(0,5)
        winProbability = 5;
        if winProbability == 5:

            # Update to include techlevel & Eon
            allowedAssets = allowedTech(techLevel)
            bonus = random.choice(allowedAssets)
            preferencePrint(str('**BONUS** The brass have gifted ' + str(NATION_ARRAY[index][1]) + ' ' + str(bonus[1]) + ' ' + str(bonus[0])),p,index,playerNationIndex)
            NATION_ARRAY[index][0]['War']['weapons'][bonus[0]] +=  bonus[1]

        return(NATION_ARRAY)


    return(NATION_ARRAY)


# Target country loses next moves (via sabotage flag in array)
# Perpertrator gains x% might
# x% chance perpertrator gets captured resulting in loss of friendship.
def espionage(nextMove,NATION_ARRAY,currentNation,p,index,playerNationIndex,debug):
    nationChoice = nextMove[1]
    bonusPercent = random.randint(1,10)

    if debug == 'y':
        print('debug next moves')
        print('next move')
        print(nextMove)
        #print('nation array')
        #print(NATION_ARRAY[nationChoice])
    NATION_ARRAY[nationChoice][0]['Nextmoves'] = ['sabotaged']


    currentNation[0]
    print()
    preferencePrint(str(str(NATION_ARRAY[nationChoice][1]) + ' has been infiltrated by an unknown advisary'),p,index,playerNationIndex)
    preferencePrint('===========================================',p,index,playerNationIndex)
    preferencePrint(str(str(NATION_ARRAY[nationChoice][1]) + ' current actions sabotaged and will miss a round.'),p,index,playerNationIndex)
    
    if currentNation[1] == NATION_ARRAY[playerNationIndex][1]:
        preferencePrint(str(str(currentNation[1]) + ' gained ' + str(bonusPercent) + '% might.' ),p,index,playerNationIndex)
        preferencePrint(str(str(currentNation[1]) + ' original might value: ' + str(currentNation[0]['War']['might'])),p,index,playerNationIndex)
    
    currentNation[0]['War']['might'] = round(currentNation[0]['War']['might'] + (currentNation[0]['War']['might'] * (bonusPercent/100)))
    if currentNation[1] == NATION_ARRAY[playerNationIndex][1]:
        preferencePrint(str(str(currentNation[1]) + '      new might value: ' + str(currentNation[0]['War']['might'])),p,index,playerNationIndex)

    discoverRisk = random.randint(0,5)
    if discoverRisk == 2:
        preferencePrint('',p,index,playerNationIndex)
        preferencePrint(str(str(NATION_ARRAY[nationChoice][1]) + ' captured the insurgent from ' + str(currentNation[1])),p,index,playerNationIndex)
        preferencePrint('===========================================',p,index,playerNationIndex)
        preferencePrint(str(str(NATION_ARRAY[nationChoice][1]) + ' friendship with ' + str(currentNation[1] + ' has decreased as a result.')),p,index,playerNationIndex)
        preferencePrint(str(str(NATION_ARRAY[nationChoice][1]) + ' original friendship value: ' + str(NATION_ARRAY[nationChoice][0]['Friendship'][currentNation[1]]['level'])),p,index,playerNationIndex)
        NATION_ARRAY[nationChoice][0]['Friendship'][currentNation[1]]['level'] = NATION_ARRAY[nationChoice][0]['Friendship'][currentNation[1]]['level'] - random.randint(1,18)
        preferencePrint(str(str(NATION_ARRAY[nationChoice][1]) + ' new friendship value: ' + str(NATION_ARRAY[nationChoice][0]['Friendship'][currentNation[1]]['level'])),p,index,playerNationIndex)


    return(NATION_ARRAY)





def allowedTech(techLevel):

    # update to make troops whatever is that number in warbriefing
    if techLevel == 0:
        allowedAssets = [('troops',random.randint(1,100))]
    if techLevel > 1:
        allowedAssets = [('troops',random.randint(1,100)),('tanks',random.randint(1,20))]
    if techLevel > 2:
        allowedAssets = [('troops',random.randint(1,100)),('tanks',random.randint(1,20)),('gunboats',random.randint(1,100))]
    if techLevel > 3:
        allowedAssets = [('troops',random.randint(1,100)),('tanks',random.randint(1,20)),('gunboats',random.randint(1,100)),('destroyers',random.randint(1,20))]
    if techLevel > 5:
        allowedAssets = [('troops',random.randint(1,100)),('tanks',random.randint(1,20)),('gunboats',random.randint(1,100)),('destroyers',random.randint(1,20)),('jets',random.randint(1,5))]
    if techLevel > 7:
        allowedAssets = [('troops',random.randint(1,100)),('tanks',random.randint(1,20)),('gunboats',random.randint(1,100)),('destroyers',random.randint(1,20)),('jets',random.randint(1,5)),('bombers',random.randint(1,3))]
    if techLevel > 8:
        allowedAssets = [('troops',random.randint(1,100)),('tanks',random.randint(1,20)),('gunboats',random.randint(1,100)),('destroyers',random.randint(1,20)),('jets',random.randint(1,5)),('bombers',random.randint(1,3)),('carriers',random.randint(1,2))]
    if techLevel > 9:
        allowedAssets = [('troops',random.randint(1,100)),('tanks',random.randint(1,20)),('gunboats',random.randint(1,100)),('destroyers',random.randint(1,20)),('jets',random.randint(1,5)),('bombers',random.randint(1,3)),('carriers',random.randint(1,2)),('Nukes',1)]

    return(allowedAssets)


def promotion(currentNation,p,index,playerNationIndex):
    warRank = ['Private', 'Lieutenant', 'Captain', 'Major', 'Commander', 'General', 'Supreme Commander']
    might   = currentNation[0]['War']['might']
    rank   = currentNation[0]['War']['level']
    if might > 150 and rank == warRank[0]:
        currentNation[0]['War']['level'] = warRank[1]
        rank   = currentNation[0]['Finance']['level']
        currentNation[0]['Special']['notes'].append('warLevel') 
        preferencePrint(str(currentNation[1] ) + ' levelled up! New War rank is ' + str(currentNation[0]['War']['level']),p,index,playerNationIndex)

    if might > 300 and rank == warRank[1]:
        currentNation[0]['War']['level'] = warRank[2]
        rank   = currentNation[0]['Finance']['level']
        currentNation[0]['Special']['notes'].append('warLevel') 
        preferencePrint(str(currentNation[1] ) + ' levelled up! New War rank is ' + str(currentNation[0]['War']['level']),p,index,playerNationIndex)

    if might > 500 and rank == warRank[2]:
        currentNation[0]['War']['level'] = warRank[3]
        rank   = currentNation[0]['Finance']['level']
        currentNation[0]['Special']['notes'].append('warLevel') 
        preferencePrint(str(currentNation[1] ) + ' levelled up! New War rank is ' + str(currentNation[0]['War']['level']),p,index,playerNationIndex)

    if might > 800 and rank == warRank[3]:
        currentNation[0]['War']['level'] = warRank[4]
        rank   = currentNation[0]['Finance']['level']
        currentNation[0]['Special']['notes'].append('warLevel') 
        preferencePrint(str(currentNation[1] ) + ' levelled up! New War rank is ' + str(currentNation[0]['War']['level']),p,index,playerNationIndex)

    if might > 2000 and rank == warRank[4]:
        currentNation[0]['War']['level'] = warRank[5]
        rank   = currentNation[0]['Finance']['level']
        currentNation[0]['Special']['notes'].append('warLevel') 
        preferencePrint(str(currentNation[1] ) + ' levelled up! New War rank is ' + str(currentNation[0]['War']['level']),p,index,playerNationIndex)

    if might > 5000 and rank == warRank[5]:
        currentNation[0]['War']['level'] = warRank[6]
        rank   = currentNation[0]['Finance']['level']
        currentNation[0]['Special']['notes'].append('warLevel') 
        preferencePrint(str(currentNation[1] ) + ' levelled up! New War rank is ' + str(currentNation[0]['War']['level']),p,index,playerNationIndex)
    return(currentNation)

def firepower(currentNation,p,index,playerNationIndex):
    warRank = ['Private', 'Lieutenant', 'Captain', 'Major', 'Commander', 'General', 'Supreme Commander']
    might   = currentNation[0]['War']['might']
    rank   = currentNation[0]['War']['level']

    return(currentNation)
