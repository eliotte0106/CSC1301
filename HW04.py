"""
Georgia Institute of Technology - CS1301
HW04 - Lists
 and Tuples
Name: Jihong Park
Collaboration Statement:
"""

#########################################

"""
Function Name: roadTrip()  
Parameters: state (str), list of tuples (list)
Returns: list of crops (list)
"""
def roadTrip(state,lst):
    result = []
    for x in lst:
        if x[1] == state and x[0] not in result:
            result.append(x[0])
    return result

# state = "GA"
# crops =[("peaches","GA")]
# print(roadTrip(state,crops))
#########################################
########## WRITE FUNCTION HERE ##########
#########################################

"""
Function Name: groceryShopping()  
Parameters: groceryList (list), priceList (list), budget (float)
Returns: purchaseList(str)
"""
def groceryShopping(groceryList,priceList,budget):
    if len(groceryList) <= 0 or len(priceList) <= 0 or (len(groceryList) != len(priceList)) or budget < 0:
        return
    result = []
    for i in range(len(groceryList)):
        if priceList[i] > budget:
            return result
        elif budget >= priceList[i]:
            result.append((groceryList[i],priceList[i]))
            budget -= priceList[i]
    return result
# groceryList = ["steak", "bacon", "cheese"]
# priceList = [10.05,5.0,1.25]
# budget = 10.0
# print(groceryShopping(groceryList,priceList,budget))


#########################################
########## WRITE FUNCTION HERE ##########
#########################################

"""
Function Name: restaurantRatings()  
Parameters: categoryList(list), restaurantList(list)
Returns: tuple(tuple)
"""
def restaurantRatings(categoryList,restaurantList):
    result = []
    rating = 0
    choice = ()
    for x in restaurantList:
        if x[2] in categoryList:
            result.append(x)
    result.reverse()
    for x in result:
        if x[1] > rating:
            choice = x
            rating = x[1]
        elif x[1] == rating:
            choice = x
            rating = x[1]

    return choice
    # if len(result) >= 1:
    #     result.sort(key = lambda x : x[1])
    #     choice = result[0]
    #     return choice
    # else:
    #     return ()
# categoryList = ["Korean","American"]     
# restaurantList = [("On the Border",3.8, "Korean"),("El Dorado",45,"Mexican")]
# print(restaurantRatings(categoryList,restaurantList))
#########################################
########## WRITE FUNCTION HERE ##########
#########################################

"""
Function Name: snackTime()  
Parameters: taList (list)
Returns: list (list)
"""
def snackTime(taList):
    result = []
    for x in taList:
        if (x[2] in range(11,15) or x[2] in range(21,24)) and [x[0]] not in result:
            result.append([x[0]])
    for x in taList:
        for i in range(len(result)):
            if x[0] in result[i]:
                result[i].append(x[1])

    return result

# taList = [("Emily", "pretzels",4),("Michael", "celery",4),("Elizabeth", "hot cheetos",4),("Emily", "fruit",4),("Corinne", "cookies",4),("Emily", "skittles",4)]
# print(snackTime(taList))
# taList = [("Corinne", "pickles",3),("Michael", "pringles",13),("Kathleen", "trail mix",21)]
# print(snackTime(taList))

#########################################
########## WRITE FUNCTION HERE ##########
#########################################


"""
Function Name: coffeeBreak()  
Parameters: list of drinks (list), budget (float)
Returns: name of drink (str)
"""
def coffeeBreak(drinks,budget):
    result = []
    for x in drinks:
        if x[2] <= budget:
            result.append(x)
    if len(result) >= 1:
        result.sort(key=lambda x: x[1])
        choice = result[len(result)-1][0]
        return choice
    return None

# drinks = [("Espresso", 75, 5.5),("Latte", 40, 4.0),("Frappuccino", 20, 3.5)]
# budget = 4.5
# print(coffeeBreak(drinks,budget))
#########################################
########## WRITE FUNCTION HERE ##########
#########################################




