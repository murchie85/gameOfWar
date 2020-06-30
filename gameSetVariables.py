import random 
def setVariables():
	NATION_ARRAY = []
	USA = {}
	UK = {}
	CHINA  = {}
	INDIA = {}
	RUSSIA  = {}
	GERMANY = {}
	ITALY = {}
	SPAIN  = {}
	FRANCE = {}
	JAPAN = {}
	BRAZIL = {}
	SOUTHKOREA = {}
	SOUTHAFRICA = {}
	PAKISTAN = {}
	INDONESIA = {}
	NIGERIA = {}
	MEXICO = {}
	EGYPT = {}
	VIETNAM = {}
	IRAN = {}
	KENYA = {}
	NATION_ARRAY = [[USA,'USA'],[UK,'UK'],[GERMANY,'GERMANY'],[CHINA,'CHINA'],[INDIA,'INDIA'],[RUSSIA,'RUSSIA'],[ITALY,'ITALY'],[SPAIN,'SPAIN'],[FRANCE,'FRANCE'],[JAPAN,'JAPAN'],[BRAZIL,'BRAZIL'],[SOUTHKOREA,'SOUTHKOREA'],[SOUTHAFRICA,'SOUTHAFRICA'],[PAKISTAN,'PAKISTAN'],[INDONESIA,'INDONESIA'],[NIGERIA,'NIGERIA'],[MEXICO,'MEXICO'],[EGYPT,'EGYPT'],[VIETNAM,'VIETNAM'],[IRAN,'IRAN'],[KENYA,'KENYA']]

	score        = 100
	wealth       = 500 
	gems         = 5
	raremetals   = 0
	oil          = 0
	might        = 100  
	troops       = 500
	aggression   = 0 

	for nation in NATION_ARRAY:
	    print(nation[0])
	    nation[0]['Score']    = score 
	    nation[0]['Finance']  = {'wealth': wealth,  'gold':60, 'gems':gems, 'raremetals':raremetals,  'oil':oil, 'level': 'PickPocket'}
	    nation[0]['War']      = {'might': might,    'level': 'Private', 'weapons':{'troops':troops,'tanks':0,'gunboats':0,'destroyers':0,'carriers':0,'jets':0,'bombers':0,'Nukes':0}, 'firePower':0}
	    nation[0]['Tech']     = {'knowledge' : 0,'level': 0, 'science':0, 'engineering':0}
	    nation[0]['Politics'] = {'influence':0, 'stability':0, 'backing':0}
	    nation[0]['Special']  = {'chance': 0, 'moveLimit':2, 'aggression':random.randint(0,100), 'creativity':random.randint(0,100), 'materialism':random.randint(0,100), 'prudence':random.randint(0,100), 'bonusUnits': [], 'notes': []}

	    nation[0]['Friendship'] = {}
	    for state in NATION_ARRAY:
	        if nation[1] != state[1]:
	            nation[0]['Friendship'][state[1]] = {'level': 0,'warDate': 0,'initiated': 0,'noWars': 0,'declared': 0,'attacked': 0,'lost': 0,'won': 0}

	    nation[0]['Citizens'] = {'population': 0, 'contentment': 0, 'fertility': 0}
	    nation[0]['hints']    = {'backing': 0, 'respect': 0, 'fear': 0}
	    nation[0]['Global']   = 'on'
	    nation[0]['Nextmoves'] = []
	    print(nation[0])
	    score      = score - 5
	    wealth     = wealth - 5
	    gems       = gems + 5
	    raremetals = raremetals + 5
	    oil        = oil + 5
	    might      = might - 3
	    troops     = troops -1


	# EXCEPTIONS 
	USA['Finance']['oil'] = 200
	RUSSIA['Finance']['oil'] = 200

	return(NATION_ARRAY)
