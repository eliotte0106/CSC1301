from points import *
"""
Georgia Institute of Technology - CS1301
HW05 - Modules, Dictionaries, Try/Except
Collaboration Statement:
"""

#########################################

"""
Function Name: vowelCounter()  
Parameters: cities (list)
Returns: number of vowels in each city (int)
"""

def vowelCounter(cities):
    if len(cities) < 0:
        return

    result = dict()
    count = 0

    for city in cities:
        for x in city:
            if x in "aAeEiIoOuU":
                count += 1
        result[city] = count
        count = 0

    return result
# cities = ['Atlanta', 'New York', 'Boston', 'LosAngeles']
# print(vowelCounter(cities))

#########################################
########## WRITE FUNCTION HERE ##########
#########################################

"""
Function Name: calculator()  
Parameters: dictionary of numerators and denominators (dict)
Returns: sum of valid fractions and the count of errors (tuple)
"""


def calculator(numdict):
    if len(numdict) < 0:
        return

    total = 0
    err = 0
    keys = list(numdict.keys())
    values = list(numdict.values())

    for i in range(len(keys)):
        try:
            sum = keys[i]/values[i]
            total += sum
        except:
            err += 1

    total = round(total,2)
    return (total,err)
# numDict = {1:0, 2:3, 4:5, '&':7, 0:9, 5:13}
# print(calculator(numDict))


#########################################
########## WRITE FUNCTION HERE ##########
#########################################

"""
Function Name: scavengerHunt()  
Parameters: list of animals (list)
Returns: results of the scavenger hunt (dict)
"""

def scavengerHunt(animals):
    if len(animals) < 0:
        return

    result = dict()
    point = 0
    not_found = []

    for animal in animals:
        if calculate(animal) != 0:
            point += calculate(animal)
        else:
            not_found.append(animal)
            print(not_found)

    result["Animals Not Found"] = tuple(not_found)
    result["Total Points"] = point

    return result
animals = ['Dolphin', 'Sea Lion', 'Jellyfish','Humpback Whale', 'Lion', 'Tiger','Eagle', 'Platypus']
print(scavengerHunt(animals))
    

#########################################
########## WRITE FUNCTION HERE ##########
#########################################

"""
Function Name: classRoster()  
Parameters: students mapped to their classes (dict)
Returns: classes mapped to their students (dict)
"""


def classRoster(students):
    if len(students) < 0:
        return

    result = dict()
    val = list(students.values())
    key = list(students.keys())

    for v in val:
        for sub in v:
            result[sub] = []
    
    for i in range(len(students)):
        for x in result:
            if x in val[i]:
                result[x].append(key[i])

    for x in result:
        result[x].sort()

    return result

    
    
    
# students = {'Kathleen':['cs1332','cs2050','psyc2015'],'Elizabeth':['math3012','cs2050','cs1332','cs3510'],'Emily': ['cs1301','psyc2015','cs3510']}
# print(classRoster(students))

#########################################
########## WRITE FUNCTION HERE ##########
#########################################


"""
Function Name: musicFestival()  
Parameters: festivals mapped to list of headlining artists (dict),
            artists (list), number of artists (int)
Returns: festival name mapped to number of matching artists (dict)
"""

def musicFestival(festivals,artists,num):
    if len(festivals) < 0 or len(artists) < 0 or num < 0:
        return

    result = dict()
    artist = list(festivals.values())
    name = list(festivals.keys())

    for i in range(len(festivals)):
        art_num = 0
        for x in artists:
            if x in artist[i]:
                art_num += 1
            if art_num >= num:
                result[name[i]] = art_num

    return result

# festivals = {"Music Midtown": ["Maroon 5", "MileyCyrus", "21 Savage","DaBaby", "Megan Thee Stallion", "Lauv","Machine Gun Kelly", "Jonas Brothers"],"Shaky Knees": ["The Strokes", "Mac Demarco","The Backseat Lovers", "Dominic Fike","St. Vincent"],"Lollapalooza": ["Dominic Fike", "Dayglow", "Lauv","Boy Pablo","The Backseat Lovers","Mt.Joy", "Young the Giant"]}    
# artistList = ["Declan Mckenna", "Peach Pit", "GlassAnimals", "The Backseat Lovers", "COIN", "Dominic Fike"]

# print(musicFestival(festivals,artistList,2))

#########################################
########## WRITE FUNCTION HERE ##########
#########################################




