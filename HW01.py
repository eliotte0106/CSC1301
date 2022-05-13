"""
Georgia Institute of Technology - CS1301
HW01 - Functions and Expressions
Name: Jihong Park
Collaboration Statement: none
"""

#########################################

"""
Function Name: bake()
Parameters: cakes (int), cupcakes (int), cookies (int)
Returns: None
"""
def bake(cakes, cupcakes, cookies):
     # all inputs must be positive integers
    if (cakes < 0) or (cupcakes < 0) or (cookies < 0):
        return
    total = (cakes * 100) + (cupcakes * 70) + (cookies * 45) #total cooking time
    hours = total // 60 # hours
    minutes = total % 60 # mins
    print("It will take {0} hours and {1} minutes to make {2} cakes, {3} cupcakes, and {4} cookies.".format(hours,minutes,cakes,cupcakes,cookies))

#########################################

"""
Function Name: cakeVolume()
Parameters: radius (int), height (int)
Returns: None
"""
def cakeVolume(radius, height):
    volume = 3.14 * (radius ** 2) * height #volume of a cylinder equation
    volume = round(volume,2) #round up to 2 decimal points
    print("The volume of the cake is {}.".format(volume))

#########################################

"""
Function Name: celebrate()
Parameters: pizzas (int), pastas (int), burgers (int), tipPercent (int)
Returns: None
"""
def celebrate(pizzas, pastas, burgers, tipPercent):
    # assume all the inputs are positive integers
    if (pizzas < 0) or (pastas < 0) or (burgers < 0) or (tipPercent < 0):
        return
    for_food = (pizzas * 14) + (pastas * 10) + (burgers * 7) # food price
    tips = for_food * (tipPercent / 100) # tips
    total = for_food + tips # total
    total = round(total,2) #round up
    tips = round(tips,2) # round up
    print("You paid ${0} and tipped ${1}.".format(total,tips))

#########################################

"""
Function Name: bookstore()
Parameters: daysBorrowed (int)
Returns: None
"""
def bookstore(daysBorrowed):
    if daysBorrowed < 0:#only positive input
        return
    #because after 14 days, fine will be charged
    fine = (daysBorrowed - 14) * 0.25 # total fine
    print("Your total amount due is ${}.".format(fine))

#########################################

"""
Function Name: monthlyAllowance()
Parameters: allowance (int), savingsPercentage (int)
Returns: None
"""
def monthlyAllowance(allowance, savingsPercentage):
    #positve integer inputs only
    if (allowance < 0) or (savingsPercentage < 0):
        return
    save = allowance * (savingsPercentage / 100)#for saving
    netflix_fee = 5.50#fee
    spotify_fee = 3.99#fee
    used = save + netflix_fee + spotify_fee# total used
    total_left = allowance - used #total left
    total_left = round(total_left,2)
    print("You have ${} left after savings and fees.".format(total_left))

#just for check

# bake(2,5,4)
# cakeVolume(3,4)
# celebrate(3,4,2,10)
#bookstore(-1)
# monthlyAllowance(1500,70)