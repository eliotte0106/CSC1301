"""
Georgia Institute of Technology - CS1301
Name: Jihong Park
HW02 - Conditionals and Loops
Collaboration Statement:
"""

#########################################

"""
Function Name: snackBar()  
Parameters: snack (str), ingredient (str), yourMoney (float)
Returns: whether you can get the snack (bool) 
"""
def snackBar(snack,ingredient,yourMoney):
    menu = [["Hotdog",("Gluten","Meat"),5.99],["Veggie Burger","Gluten",5.99]
    ,["Chili Bowl","Meat",3.99],["Chili Cheese Fries",("Meat","Dairy"),4.99]]
    result = []
    for x in menu:
        if ingredient not in x[1] and snack == x[0] and yourMoney >= x[2]:
            result.append(x)
    
    if len(result) == 1:
        return True
    else:
        return False

# print(snackBar("Hotdog","Gluten",6.50))
# print(snackBar("Chili Cheese Fries","Gluten",5.00))
# print(snackBar("Veggie Burger","Meat",7.00))
# print(snackBar("Chili Bowl","Meat",5.99))
# print(snackBar("Chili Bowl","Dairy",5.99))


"""
Function Name: waterGames()
Parameters: gameName (str), numPlayers (int), totalFriends (int)
Returns: None (NoneType)
"""
def waterGames(gameName,numPlayers,totalFriends):
    if (numPlayers/totalFriends) * 100 < 30:
        print("Let's choose something else.")
    elif (numPlayers/totalFriends) * 100 > 30 and (numPlayers/totalFriends) * 100 < 75:
        print("We will {} for a little bit!".format(gameName))
    else:
        print("Let's {}!!!".format(gameName))

# waterGames("go to the lake",3,6)
# waterGames("go water skiing",3,4)
"""
Function Name: summerShopping()
Parameters: clothingItem (str), size (str)
Returns: None (NoneType)
"""

def summerShopping(clothingItem,size):
    item = [["shorts","Blue",("S",'M')],["shorts","white","S"],["tank","Black",("M","L")]
    ,["tank","Yellow",("S","L")],["flipflops","Green",("M","L")],["flipflops","Purple",("S","L")]]

    count = 0
    for x in item:
        if clothingItem == x[0] and size in x[2]:
            count += 1
    if count > 0 :
        print("{} colors are available in this item and size.".format(count))
    else:
        print("No colors are available in this item and size.")

# summerShopping("tank","S")
# summerShopping("shorts","S")
# summerShopping("shorts","L")
"""
Function Name: stopGame()  
Parameters: initialPrice (float), finalPrice (float), percentGrowth (float)
Returns: numberOfDays (int)  
"""

def stopGame(initialPrice,finalPrice,percentGrowth):
    if initialPrice < 0 or finalPrice < 0 or percentGrowth < 0:
        return
    if finalPrice <= initialPrice:
        return 0
    numberOfDays = 1
    initial = initialPrice + initialPrice * (percentGrowth/100)
    max = initial
    while max <= finalPrice:
        max = max + max * (percentGrowth/100)
        numberOfDays += 1
    return numberOfDays

# print(stopGame(8.67,432.87,45.0))
# print(stopGame(232.0,20000.0,15.0))
# print(stopGame(2.0,10,50.0))


"""
Function Name: adventure()
Parameters: startDay (int), stopDay (int), hikeLimit(int)  
Returns: None (NoneType)
"""

def adventure(startDay,stopDay,hikeLimit):
    limit = 0
    if hikeLimit < 0:
        return
    for i in range(startDay,stopDay+1):
        if i % 12 == 0:
            print("Roadtrip!")
        elif i % 3 == 0:
            print("Hike")
            limit += 1
        if limit == hikeLimit:
            print("No more hikes")
            break
    return "yay"

#adventure(4,29,3)
# print("")
# adventure(9,25,7)


