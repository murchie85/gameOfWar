from gameConquest_utilities import preferencePrint as preferencePrint
from gameConquest_utilities import updateTechNames as updateTechNames

import sys
import time
import copy
import random


def processResearch(nextMove,NATION_ARRAY,TECH_MAP,currentNation,p,index,playerNationIndex,nextMoveIndex):
    pending                  = nextMove[0]
    job                      = nextMove[1]
    era                      = nextMove[2]
    choice                   = nextMove[3]
    required                 = nextMove[4]
    researchedItemName       = currentNation[0]['Tech']['researched'][choice][1]


    remaining                = required - currentNation[0]['Tech']['researched'][choice][0]
    pointsOwned              = currentNation[0]['Tech']['research points']
    pointsToSpend            = round(currentNation[0]['Tech']['research points'] * 0.2) # Test the last number, it may need reduced: spend = devcompletion speed

    # Skip this move if not enough points
    if pointsOwned < pointsToSpend:
        print('Not enough points')
        return(NATION_ARRAY)

    # Skip if already max
    if remaining < 1:
        #print('Already Maxed out')
        return(NATION_ARRAY)

    # Deduct RP 
    NATION_ARRAY[index][0]['Tech']['research points'] -= pointsToSpend
    # Update points earned
    NATION_ARRAY[index][0]['Tech']['researched'][choice][0] += pointsToSpend
    # Completion percent
    NATION_ARRAY[index][0]['Tech']['researched'][choice][2] = round((currentNation[0]['Tech']['researched'][choice][0]/required) * 100)
    #Update remaining
    remaining = required - currentNation[0]['Tech']['researched'][choice][0]
    # update
    pointsOwned              = currentNation[0]['Tech']['research points']


    preferencePrint(str(str(NATION_ARRAY[index][1]) + ' Research Update'),p,index,playerNationIndex)
    preferencePrint('------------------',p,index,playerNationIndex)
    preferencePrint(str('Researched Item: ' + str(researchedItemName)),p,index,playerNationIndex)
    #preferencePrint(str('Research points spent = ' + str(pointsToSpend)),p,index,playerNationIndex)
    #preferencePrint(str('Research: remaining   = ' + str(remaining) + ' , completion %' + str(currentNation[0]['Tech']['researched'][choice][2]) + '%'),p,index,playerNationIndex)
    #preferencePrint(str('Research: pointsOwned = ' + str(pointsOwned)),p,index,playerNationIndex)

    # process reward
    if remaining < 1:
        NATION_ARRAY[index][0]['Tech']['researched'][choice][2]  = 100
        NATION_ARRAY[index][0]['Nextmoves'][nextMoveIndex] = ''
        NATION_ARRAY = processResearchReward(NATION_ARRAY,TECH_MAP,era,choice,researchedItemName,p,index,playerNationIndex)

    else:
        # Continue the move
        nextMove = ['pending',job,era,choice,required]
        NATION_ARRAY[index][0]['Nextmoves'][nextMoveIndex] = nextMove

    preferencePrint(str('Completion ' + str(NATION_ARRAY[index][0]['Tech']['researched'][choice][2]) + '%'),p,index,playerNationIndex)
    return(NATION_ARRAY)

def processResearchReward(NATION_ARRAY,TECH_MAP,era,choice,researchedItemName,p,index,playerNationIndex):
    preferencePrint('',p,index,playerNationIndex)
    preferencePrint(str('######' +str(researchedItemName) + ' Research Complete! #########'),p,index,playerNationIndex)
    preferencePrint('',p,index,playerNationIndex)
    for item in TECH_MAP['EraBonus'][era][choice]:
        if item[0] == 'K':
            printLine = str('Knowledge boosted by ' + str(item[1]) + ' points.')
            NATION_ARRAY[index][0]['Tech']['knowledge'] += item[1]
        if item[0] == 'R':
            printLine = str('Research boosted by ' + str(item[1]) + ' points.')
            NATION_ARRAY[index][0]['Tech']['research points'] += item[1]
        if item[0] == 'W':
            printLine = str('Wealth increased by $' + str(item[1]))
            NATION_ARRAY[index][0]['Finance']['wealth'] += item[1]
        preferencePrint(printLine,p,index,playerNationIndex)
    preferencePrint('',p,index,playerNationIndex)
    return(NATION_ARRAY)


def gainResearch(nextMove,NATION_ARRAY,TECH_MAP,currentNation,p,index,playerNationIndex,nextMoveIndex):
    pending                  = nextMove[0]
    job                      = nextMove[1]
    intensity                = nextMove[2]
    investedPercent          = nextMove[3]
    rounds                   = nextMove[4]
    invested                 = nextMove[5]
    RP                       = NATION_ARRAY[index][0]['Tech']['research points']
    KP                       = NATION_ARRAY[index][0]['Tech']['knowledge']

    if intensity == 'Soft':
        bonusRP = round((0.1 * RP))
        if bonusRP < 25:
            bonusRP = 25
        bonusKP = 0
    elif intensity == 'Medium':
        bonusRP = round((0.1 * RP) + (invested/3))
        bonusKP = round((0.1 * KP) + (invested/4))
    elif intensity == 'Hard':
        bonusRP = round((0.2 * RP) + (invested/5))
        bonusKP = round((0.2 * KP) + (invested/6))
    elif intensity == 'Overtime':
        bonusRP = round((0.3 * RP) + (invested/7))
        bonusKP = round((0.3 * KP) + (invested/8))


    # IF ROUNDS STILL TO GO, REWARD BONUS AND CONTINUE PENDING
    if rounds > 0:
        rounds = rounds -1

        #ADD REWARDS
        NATION_ARRAY[index][0]['Tech']['research points'] += bonusRP
        NATION_ARRAY[index][0]['Tech']['knowledge']      += bonusKP

        nextMove = ['pending',job,intensity,investedPercent,rounds,invested]
        NATION_ARRAY[index][0]['Nextmoves'][nextMoveIndex] = nextMove


        preferencePrint(str(str(NATION_ARRAY[index][1]) + ' Research Grant'),p,index,playerNationIndex)
        preferencePrint('------------------',p,index,playerNationIndex)
        preferencePrint(str('Level ' + str(intensity)),p,index,playerNationIndex)
        preferencePrint(str('RP Bonus : +' + str(bonusRP)),p,index,playerNationIndex)
        preferencePrint(str('KP Bonus : +' + str(bonusKP)),p,index,playerNationIndex)
        preferencePrint(str('RP increased from ' + str(RP) + ' to ' + str(NATION_ARRAY[index][0]['Tech']['research points'])),p,index,playerNationIndex)
        preferencePrint(str('KP increased from ' + str(KP) + ' to ' + str(NATION_ARRAY[index][0]['Tech']['knowledge'])),p,index,playerNationIndex)
        preferencePrint(str('Rounds Remaining : ' + str(rounds)),p,index,playerNationIndex)

        # Clear out nextmove
        if rounds == 0:
            NATION_ARRAY[index][0]['Nextmoves'][nextMoveIndex] = ''
        return(NATION_ARRAY)

    else:
        NATION_ARRAY[index][0]['Nextmoves'][nextMoveIndex] = ''
        return(NATION_ARRAY)

    return(NATION_ARRAY)

def advanceEra(nextMove,NATION_ARRAY,TECH_MAP,currentNation,p,index,playerNationIndex,nextMoveIndex):

    era = currentNation[0]['Tech']['era']
    nextEra = TECH_MAP['nextEra'][era]

    NATION_ARRAY[index][0]['Tech']['era'] = nextEra
    NATION_ARRAY[index][0]['Tech']['researched'] = {'one':[0,'',0],'two':[0,'',0],'three':[0,'',0],'four':[0,'',0],'five':[0,'',0]}
    NATION_ARRAY = updateTechNames(NATION_ARRAY,TECH_MAP)
    preferencePrint('++++++++++++++++++++++++++++++++++++++++++',p,index,playerNationIndex)
    preferencePrint(str(str(NATION_ARRAY[index][1]) + ' has advanced to the ' + str(nextEra)),p,index,playerNationIndex)
    preferencePrint('++++++++++++++++++++++++++++++++++++++++++',p,index,playerNationIndex)

    return(NATION_ARRAY)
