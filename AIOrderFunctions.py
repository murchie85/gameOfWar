import sys
import time
import copy
import random


# TO DO ------



# Need to make buying more sophisticated rather than chosing a random commodity
# Remember to deduct might from hard drill
# Buffer drill by tech level 

def setAIMoves(index,currentNation,PRICE_TRACKER,WAR_BRIEFING,NATION_ARRAY,AI_DEBUG):

    # Capping AI at one for now 
    moveLimit    = int(currentNation[0]['Special']['moveLimit'])
    aggression   = currentNation[0]['Special']['aggression']
    creativity   = currentNation[0]['Special']['creativity']
    materialism  = currentNation[0]['Special']['materialism']
    prudence     = currentNation[0]['Special']['prudence']
    wealth       = currentNation[0]['Finance']['wealth'] 


    # Calculate bias values
    for moveNumber in range(1, moveLimit):
        wealth       = currentNation[0]['Finance']['wealth']
        financeBias  = materialism + random.randint(0,100)
        warBias      = aggression  + random.randint(0,100)
        #scienceBias  = creativity  + random.randint(0,100)
        #politicsBias = prudence    + random.randint(0,100)
        values = (financeBias,warBias)
        bias = values.index(max(values))

        if 'moves' in AI_DEBUG:
            print('+++++DEBUG+++++ MOVES')
            print('values finance, war: ' + str(values) )
            print('bias: ' + str(bias))



        # HAS FINANCE BIAS
        if bias == 0:
            # GAMBLE 
            currentNation = gamble(currentNation)
            # BUY
            currentNation = aiBuy(PRICE_TRACKER,currentNation,materialism)
            # SELL
            currentNation = aiSell(PRICE_TRACKER,currentNation,aggression,materialism)

        # HAS BIAS TOWARDS WAR
        if bias == 1:
            # TODO: Add logic
            currentNation = drill(currentNation)
            # BUILD
            currentNation = build(currentNation,WAR_BRIEFING,aggression,materialism)
            # SCRAP
            currentNation = scrap(currentNation,WAR_BRIEFING,NATION_ARRAY)
            # ESPIONAGE
            currentNation = espionage(currentNation,NATION_ARRAY,aggression,prudence,AI_DEBUG)

    # If No moves, then pass
    if len(currentNation[0]['Nextmoves']) == 0:
        currentNation[0]['Nextmoves']= [['pass']]
        
    return(currentNation)





def build(currentNation,WAR_BRIEFING,aggression,materialism):


    buildBias = 1
    if (aggression + materialism) > 150:
        buildBias = 2
    elif (aggression + materialism) > 100:
        buildBias = 3
    elif (aggression + materialism) > 75:
        buildBias = 4
    else:
        buildBias = 10


    buildProbability = random.randint(0, buildBias)
    if buildProbability == 1:
        wealth               = currentNation[0]['Finance']['wealth'] 
        aggressionAdjusted   = (currentNation[0]['Special']['aggression']) / 100
        techLevel            = currentNation[0]['Tech']['level']

        allowedAssets = []
        allowedAssets = allowedTech(techLevel)
        unit = random.choice(allowedAssets)

        price      = WAR_BRIEFING['weapons'][unit][0]
        wait       = WAR_BRIEFING['weapons'][unit][1]
        bonusMight = WAR_BRIEFING['weapons'][unit][2]

        maxpurchase = int(wealth // price)
        adjusted    = round((aggressionAdjusted * maxpurchase))

        if adjusted > 0:
            maxBuy = round(random.randint(adjusted, maxpurchase))
        elif maxpurchase > 0:
            maxBuy = round(random.randint(0,maxpurchase))
        else:
            # No money so skipping
            return(currentNation)
        
        # If they can't afford even one  
        if maxBuy < 1:
            print('cant afford')
            return(currentNation)

        purchaseAmount = random.randint(1,maxBuy)
        cost = purchaseAmount * price

        # Deduct cost & Place Order 
        currentNation[0]['Finance']['wealth'] = currentNation[0]['Finance']['wealth'] - cost
        currentNation[0]['Nextmoves'] = currentNation[0]['Nextmoves'] + [['submitted','WeaponsBuild',unit, purchaseAmount,wait,bonusMight]]
    return(currentNation)



def scrap(currentNation,WAR_BRIEFING,NATION_ARRAY):
    wealth               = currentNation[0]['Finance']['wealth'] 
    aggressionAdjusted   = (currentNation[0]['Special']['aggression']) / 100
    techLevel            = currentNation[0]['Tech']['level']
    wealthArray          = []
    allowedAssets        = []
    allowedAssets        = allowedTech(techLevel)
    unit                 = random.choice(allowedAssets)
    stock                = currentNation[0]['War']['weapons'][unit]
    scrapProbability = 10




    # Check to see if current country is poorer than 80% of average
    for country in NATION_ARRAY: wealthArray.append(country[0]['Finance']['wealth'])
    averageWealth = round((sum(wealthArray)/len(wealthArray)))
    poor          = 0.6*averageWealth
    if wealth < poor: scrapProbability = 3

    if random.randint(0,scrapProbability) == 2 and stock > 0:
        # Pick random unit to scrap
        price        = WAR_BRIEFING['weapons'][unit][0]
        reducedMight = WAR_BRIEFING['weapons'][unit][2]
        adjusted    = round((aggressionAdjusted * stock))
        maxScrap    = round(random.randint(adjusted, stock))

        if stock < 0 or maxScrap < 0:
            print('none to scrap')
            print('stock :' + str(stock))
            print('maxscrap: ' + str(maxscrap))
            return(currentNation)

        scrapAmount = random.randint(1,maxScrap)
        valuation   = scrapAmount * price

        # Deducts units and places order 
        currentNation[0]['War']['weapons'][unit] = currentNation[0]['War']['weapons'][unit] - scrapAmount
        currentNation[0]['Nextmoves']            = currentNation[0]['Nextmoves'] + [['WeaponsScrap',unit, scrapAmount,valuation,reducedMight]]
    return(currentNation)


def allowedTech(techLevel):
    if techLevel == 0:
        allowedAssets = ['troops']
    if techLevel > 1:
        allowedAssets = ['troops','tanks']
    if techLevel > 2:
        allowedAssets = ['troops','tanks','gunboats']
    if techLevel > 3:
        allowedAssets = ['troops','tanks','gunboats','destroyers']
    if techLevel > 5:
        allowedAssets = ['troops','tanks','gunboats','destroyers','jets']
    if techLevel > 7:
        allowedAssets = ['troops','tanks','gunboats','destroyers','jets','bombers']
    if techLevel > 8:
        allowedAssets = ['troops','tanks','gunboats','destroyers','jets','bombers','carriers']
    if techLevel > 9:
        allowedAssets = ['troops','tanks','gunboats','destroyers','jets','bombers','carriers','Nukes']

    return(allowedAssets)






# Pick a military branch, save asset details to array, place order 
def drill(currentNation):

    troops     = currentNation[0]['War']['weapons']['troops']
    tanks      = currentNation[0]['War']['weapons']['tanks']
    army       = troops + tanks
    gunboats   = currentNation[0]['War']['weapons']['gunboats']
    destroyers = currentNation[0]['War']['weapons']['destroyers']
    carriers   = currentNation[0]['War']['weapons']['carriers']
    navy       = gunboats + destroyers + carriers
    jets       = currentNation[0]['War']['weapons']['jets']
    bombers    = currentNation[0]['War']['weapons']['bombers']
    airforce   = jets + bombers
    nukes      = currentNation[0]['War']['weapons']['Nukes']
        

    branchSelection = []
    if army > 0: 
        branchSelection.append(('army',     ('troops','tanks'),army))
    if navy > 0: 
        branchSelection.append(('navy',     ('gunboats','destroyers','carriers'),navy))
    if airforce > 0: 
        branchSelection.append(('airforce', ('jets','bombers'),airforce))
    if len(branchSelection) ==0:
        currentNation[0]['Nextmoves']= [['pass']]
        print('failed to drill')
        return(currentNation)

    branch = random.choice(branchSelection)
    #print(branch)
    units = []

    #filling an array to say what units and how many belong to this branch 
    for asset in branch[1]:
        package = (str(asset),currentNation[0]['War']['weapons'][asset])
        units.append(package)

    exposure = random.choice(('soft','medium','hard'))
    drillOrder = ['drill',branch[0],exposure, units]
    #print(str(currentNation[1]) + ' order ' + str(drillOrder))
    # Deduct units
    for unit in units:
        currentNation[0]['War']['weapons'][unit] = 0
    # Place Order
    currentNation[0]['Nextmoves'] = currentNation[0]['Nextmoves'] + [drillOrder]
    return(currentNation)

# Probability of purchase depends how much the price is lower than average
def aiBuy(PRICE_TRACKER,currentNation,materialism):

    commodity = random.choice(('gold','gems','raremetals','oil'))
   
    percentageDecrease = ((PRICE_TRACKER[commodity]['average'] - PRICE_TRACKER[commodity]['price'])/PRICE_TRACKER[commodity]['average'])
   
    # Higher materialism increases buy probability
    if percentageDecrease > 0.80:
        maxBuyProbability = 30
    elif percentageDecrease > 0.50:
        maxBuyProbability = 20
    elif percentageDecrease > 0.20:
        maxBuyProbability = 15
    else:
        maxBuyProbability = 10

    buyProbability =  (materialism / 100 ) * random.randint(0,maxBuyProbability)
    # make the order
    if buyProbability > 1:
        # submit order
        price        = PRICE_TRACKER[commodity]['price']
        credits      = currentNation[0]['Finance']['wealth']
        aggression   = (currentNation[0]['Special']['aggression'] / 100)
        maxpurchase = int(credits // price)

        compensatedMax = round(aggression * maxpurchase)
        if compensatedMax < 1:
            currentNation[0]['Nextmoves'] = currentNation[0]['Nextmoves'] + [['pass']]
            return(currentNation)

        purchaseAmount = random.randint(1, compensatedMax)
        cost = purchaseAmount * price

        # Deduct cost & Place Order 
        currentNation[0]['Finance']['wealth'] = currentNation[0]['Finance']['wealth'] - cost
        currentNation[0]['Nextmoves']        = currentNation[0]['Nextmoves'] + [['buy',commodity, purchaseAmount]]
        
    return(currentNation)


def aiSell(PRICE_TRACKER,currentNation,aggression,materialism):

    commodity = random.choice(('gold','gems','raremetals','oil'))
    percentageIncrease = ((PRICE_TRACKER[commodity]['price'] - PRICE_TRACKER[commodity]['average'])/PRICE_TRACKER[commodity]['average'])
   
    if percentageIncrease > 0.80:
        maxSellProbabiliy = 4
    elif percentageIncrease > 0.50:
        maxSellProbabiliy = 3
    elif percentageIncrease > 0.20:
        maxSellProbabiliy = 2
    else:
        maxSellProbabiliy = 1

    # max value is 6
    sellProbability =  round((aggression + materialism)/100) + maxSellProbabiliy

    if sellProbability > 3:
        # decrease stock
        # submit order
        price                  = PRICE_TRACKER[commodity]['price']
        myStock                = currentNation[0]['Finance'][commodity]
        aggressionPercentage   = (aggression / 100)

        compensatedMax = round(aggressionPercentage * myStock)
        if compensatedMax > myStock or compensatedMax < 1:
            return(currentNation)

        # purchase choice
        purchaseAmount = random.randint(1, compensatedMax)
        value = purchaseAmount * price
        # Deduct stock & Place Order 
        currentNation[0]['Finance'][commodity]   = currentNation[0]['Finance'][commodity] - purchaseAmount
        currentNation[0]['Nextmoves']            = currentNation[0]['Nextmoves'] + [['sell',commodity, purchaseAmount, value]]
        
    return(currentNation)


def gamble(currentNation):
    # Roughly 25% chance of having a gamble
    gambleAction = random.randint(0,10)
    if gambleAction < 3:
        creditsAvailable = int(currentNation[0]['Finance']['wealth'])
        maxSpend = round((int(currentNation[0]['Special']['aggression'])/100) * creditsAvailable)
        if maxSpend > 1:
            amount = random.randint(1,maxSpend)
            currentNation[0]['Finance']['wealth'] = currentNation[0]['Finance']['wealth'] - amount
            currentNation[0]['Nextmoves']         = currentNation[0]['Nextmoves'] + [['gamble',amount]]

    return(currentNation)



# Only attack if aggression high, prudence low, friendship low
def espionage(currentNation,NATION_ARRAY,aggression,prudence,AI_DEBUG):

    # if friendship lower than 0 - espionage is possible.
    espionageThreshold = 0
    #----------------------
    # PROBABILITY LOGIC
    #----------------------
    maxHateArray = []
    for nation in currentNation[0]['Friendship']:
        maxHateArray.append(currentNation[0]['Friendship'][nation]['level'])
    minVal = min(maxHateArray)

    targetNation = ''
    for nation in currentNation[0]['Friendship']:
        if currentNation[0]['Friendship'][nation]['level'] == minVal:
            targetNation = nation
    

    # ELIF SWITCH ATTACK PROBABILITY
    attackBias = 1
    if aggression > 70 and prudence < 30:
        attackBias = 4
    elif aggression > 70 and prudence < 50:
        attackBias = 5
    elif aggression > 65 and prudence < 50:
        attackBias = 6
    else:
        attackBias = 15

    attackProbability = random.randint(0, attackBias)


    #----------------------
    # ORDERS
    #----------------------

    # Only attack if really agressive, low prudence and frienship < 0
    if attackProbability == 1    and minVal < espionageThreshold:
        # get index 
        indexList = []
        for item in NATION_ARRAY:
            indexList.append(item[1])
        targetNationIndex = indexList.index(targetNation)

        espionageOrder = ['espionage',targetNationIndex]
        currentNation[0]['Nextmoves'] = currentNation[0]['Nextmoves'] + [espionageOrder]
        # DEBUG
        if 'espionage' in AI_DEBUG:
            print('+++++DEBUG+++++ Espionage')
            print('Current nation: ' + str(currentNation[1]))
            print('Target nation: ' + str(targetNation))
            print('Friendship: ' + str(currentNation[0]['Friendship'][targetNation]['level']))
            print('Espionage orders given..' + str(currentNation[0]['Nextmoves'] ))
    return(currentNation)


def research(currentNation):
    # Prevent AI from researching two things at the same time 
    # Make sure AI does not already have this stack completed
    return(currentNation)

